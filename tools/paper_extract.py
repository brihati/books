#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import mimetypes
import os
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable


DEFAULT_IMAGE_MIN_AREA = 10_000


@dataclass(frozen=True)
class ExtractedAsset:
    filename: str
    page: int
    width: int
    height: int
    extension: str
    method: str
    caption: str | None = None


def require_pymupdf() -> Any:
    try:
        import fitz  # type: ignore
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Missing dependency: PyMuPDF\n\n"
            "Install it in the local venv:\n"
            "  .venv/bin/python3 -m pip install pymupdf"
        ) from exc
    return fitz


def is_url(value: str) -> bool:
    parsed = urllib.parse.urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ensure_output_dir(out_dir: Path, *, force: bool) -> None:
    if out_dir.exists():
        if not force:
            raise FileExistsError(f"Output directory already exists: {out_dir}. Re-run with --force to overwrite.")
        if not out_dir.is_dir():
            raise NotADirectoryError(f"Output path exists and is not a directory: {out_dir}")
        shutil.rmtree(out_dir)
    (out_dir / "source").mkdir(parents=True)
    (out_dir / "content" / "pages").mkdir(parents=True)
    (out_dir / "assets").mkdir(parents=True)


def download_pdf(url: str, destination: Path, *, opener: Callable[..., Any] | None = None) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": "paper-extract/1.0"})
    open_fn = opener or urllib.request.urlopen
    try:
        with open_fn(request, timeout=60) as response:
            content_type = response.headers.get("content-type", "")
            data = response.read()
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Failed to download PDF: {url}: {exc}") from exc

    if not data.startswith(b"%PDF"):
        guessed_type = content_type.split(";")[0].strip().lower()
        if guessed_type != "application/pdf":
            raise ValueError(f"URL did not return a PDF: content-type={content_type or 'unknown'}")

    destination.write_bytes(data)
    return {"source_type": "url", "source": url, "content_type": content_type, "bytes": len(data)}


def copy_local_pdf(source: Path, destination: Path) -> dict[str, Any]:
    if not source.exists():
        raise FileNotFoundError(f"PDF file not found: {source}")
    if not source.is_file():
        raise IsADirectoryError(f"PDF input is not a file: {source}")
    if source.suffix.lower() != ".pdf":
        guessed_type, _ = mimetypes.guess_type(source.name)
        if guessed_type != "application/pdf":
            raise ValueError(f"Input does not look like a PDF: {source}")
    shutil.copy2(source, destination)
    return {"source_type": "file", "source": str(source.resolve()), "bytes": destination.stat().st_size}


def prepare_source(input_value: str, destination: Path) -> dict[str, Any]:
    if is_url(input_value):
        return download_pdf(input_value, destination)
    return copy_local_pdf(Path(input_value), destination)


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip() for line in text.splitlines()).strip()


def page_anchor(page_number: int) -> str:
    return f"<!-- page: {page_number} -->"


def markdown_image_path(asset_filename: str, *, from_pages_dir: bool = False) -> str:
    prefix = "../../assets" if from_pages_dir else "../assets"
    return f"{prefix}/{asset_filename}"


def likely_caption(page_text: str, image_index: int) -> str | None:
    caption_lines = []
    for line in page_text.splitlines():
        stripped = line.strip()
        if re.match(r"(?i)^(figure|fig\.?|table)\s+\d+", stripped):
            caption_lines.append(stripped)
    if not caption_lines:
        return None
    if image_index - 1 < len(caption_lines):
        return caption_lines[image_index - 1]
    return caption_lines[0]


def detect_references_start(page_texts: list[str]) -> tuple[int | None, bool]:
    candidates: list[int] = []
    heading_re = re.compile(r"(?im)^\s*(references|bibliography|works cited)\s*$")
    for index, text in enumerate(page_texts):
        if heading_re.search(text):
            candidates.append(index)
    if candidates:
        return candidates[-1], False

    # Fallback: papers usually put references near the end, often with bracketed or author-year citations.
    for index in range(max(0, len(page_texts) - 5), len(page_texts)):
        text = page_texts[index]
        citation_like = len(re.findall(r"(?m)^\s*(\[\d+\]|\w[\w-]+,\s+\w)", text))
        if citation_like >= 5:
            return index, True
    return None, True


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_page_markdown(
    *,
    page_number: int,
    page_text: str,
    page_assets: list[ExtractedAsset],
    from_pages_dir: bool,
) -> str:
    page_md_lines = [page_anchor(page_number), "", f"## Page {page_number}", ""]
    if page_text:
        page_md_lines.append(page_text)
        page_md_lines.append("")
    else:
        page_md_lines.append("_No selectable text extracted from this page._")
        page_md_lines.append("")

    if page_assets:
        page_md_lines.append("### Assets")
        page_md_lines.append("")
        for asset in page_assets:
            alt = asset.caption or f"Page {page_number} {asset.method}"
            page_md_lines.append(f"![{alt}]({markdown_image_path(asset.filename, from_pages_dir=from_pages_dir)})")
            if asset.caption:
                page_md_lines.append("")
                page_md_lines.append(f"Caption: {asset.caption}")
            page_md_lines.append("")

    return "\n".join(page_md_lines).rstrip() + "\n"


def extract_pdf(
    pdf_path: Path,
    out_dir: Path,
    *,
    render_pages: str,
    image_min_area: int,
) -> dict[str, Any]:
    fitz = require_pymupdf()
    doc = fitz.open(os.fspath(pdf_path))
    page_texts: list[str] = []
    all_assets: list[ExtractedAsset] = []
    full_md_parts: list[str] = []
    full_txt_parts: list[str] = []

    for page_index in range(doc.page_count):
        page_number = page_index + 1
        page = doc.load_page(page_index)
        page_text = normalize_text(page.get_text("text"))
        page_texts.append(page_text)

        page_assets: list[ExtractedAsset] = []
        for image_index, image in enumerate(page.get_images(full=True), start=1):
            xref = int(image[0])
            extracted = doc.extract_image(xref)
            width = int(extracted.get("width") or 0)
            height = int(extracted.get("height") or 0)
            if width * height < image_min_area:
                continue
            extension = str(extracted.get("ext") or "png").lower()
            filename = f"page-{page_number:03d}-img-{len(page_assets) + 1:02d}.{extension}"
            asset_path = out_dir / "assets" / filename
            asset_path.write_bytes(extracted["image"])
            asset = ExtractedAsset(
                filename=filename,
                page=page_number,
                width=width,
                height=height,
                extension=extension,
                method="embedded-image",
                caption=likely_caption(page_text, image_index),
            )
            page_assets.append(asset)
            all_assets.append(asset)

        should_render = render_pages == "all" or (render_pages == "with-images" and page_assets)
        if should_render:
            matrix = fitz.Matrix(2, 2)
            pixmap = page.get_pixmap(matrix=matrix, alpha=False)
            filename = f"page-{page_number:03d}-render.png"
            pixmap.save(os.fspath(out_dir / "assets" / filename))
            asset = ExtractedAsset(
                filename=filename,
                page=page_number,
                width=int(pixmap.width),
                height=int(pixmap.height),
                extension="png",
                method="page-render",
                caption=None,
            )
            all_assets.append(asset)
            page_assets.append(asset)

        page_md = build_page_markdown(
            page_number=page_number,
            page_text=page_text,
            page_assets=page_assets,
            from_pages_dir=True,
        )
        (out_dir / "content" / "pages" / f"page-{page_number:03d}.md").write_text(page_md, encoding="utf-8")
        full_md_parts.append(
            build_page_markdown(
                page_number=page_number,
                page_text=page_text,
                page_assets=page_assets,
                from_pages_dir=False,
            )
        )
        full_txt_parts.append(f"--- Page {page_number} ---\n{page_text}\n")

    references_start, references_uncertain = detect_references_start(page_texts)
    if references_start is None:
        references_text = "References section was not detected during extraction.\n"
    else:
        references_text = "\n\n".join(
            f"--- Page {index + 1} ---\n{text}" for index, text in enumerate(page_texts[references_start:], start=references_start)
        ).strip() + "\n"

    (out_dir / "content" / "full.md").write_text("\n\n".join(part.rstrip() for part in full_md_parts) + "\n", encoding="utf-8")
    (out_dir / "content" / "full.txt").write_text("\n".join(part.rstrip() for part in full_txt_parts) + "\n", encoding="utf-8")
    (out_dir / "content" / "references.md").write_text(references_text, encoding="utf-8")
    write_json(out_dir / "assets" / "manifest.json", [asdict(asset) for asset in all_assets])

    empty_pages = [index + 1 for index, text in enumerate(page_texts) if not text.strip()]
    linked_assets = sorted({asset.filename for asset in all_assets})
    missing_assets = [filename for filename in linked_assets if not (out_dir / "assets" / filename).exists()]
    return {
        "page_count": doc.page_count,
        "metadata": dict(doc.metadata or {}),
        "asset_count": len(all_assets),
        "embedded_image_count": sum(1 for asset in all_assets if asset.method == "embedded-image"),
        "page_render_count": sum(1 for asset in all_assets if asset.method == "page-render"),
        "empty_text_pages": empty_pages,
        "references_start_page": None if references_start is None else references_start + 1,
        "references_detection_uncertain": references_uncertain,
        "validation": {
            "missing_linked_assets": missing_assets,
            "has_full_markdown": (out_dir / "content" / "full.md").exists(),
            "has_full_text": (out_dir / "content" / "full.txt").exists(),
            "has_references_file": (out_dir / "content" / "references.md").exists(),
        },
    }


def run(args: argparse.Namespace) -> int:
    out_dir = args.out.resolve()
    ensure_output_dir(out_dir, force=args.force)
    pdf_path = out_dir / "source" / "paper.pdf"
    source_info = prepare_source(args.input, pdf_path)
    extraction = extract_pdf(
        pdf_path,
        out_dir,
        render_pages=args.render_pages,
        image_min_area=args.image_min_area,
    )
    manifest = {
        "input": args.input,
        "source": source_info,
        "pdf": {
            "path": str(pdf_path),
            "sha256": sha256_file(pdf_path),
            "bytes": pdf_path.stat().st_size,
        },
        "options": {
            "render_pages": args.render_pages,
            "image_min_area": args.image_min_area,
        },
        "extraction": extraction,
        "extracted_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    }
    write_json(out_dir / "manifest.json", manifest)
    (out_dir / "extraction.log").write_text(
        "\n".join(
            [
                f"input={args.input}",
                f"out={out_dir}",
                f"pages={extraction['page_count']}",
                f"assets={extraction['asset_count']}",
                f"references_start_page={extraction['references_start_page']}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    print(out_dir)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract a study bundle from a PDF paper.")
    parser.add_argument("input", help="PDF URL or local PDF path")
    parser.add_argument("--out", type=Path, required=True, help="Output directory for the study bundle")
    parser.add_argument("--force", action="store_true", help="Overwrite the output directory if it exists")
    parser.add_argument(
        "--render-pages",
        choices=["with-images", "all", "none"],
        default="with-images",
        help="Render page screenshots for all pages, pages with images, or no pages",
    )
    parser.add_argument(
        "--image-min-area",
        type=int,
        default=DEFAULT_IMAGE_MIN_AREA,
        help="Skip embedded images smaller than this pixel area",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return run(args)
    except Exception as exc:
        print(f"paper_extract: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
