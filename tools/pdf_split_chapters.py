#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


def _require_pymupdf() -> "module":
    try:
        import fitz  # type: ignore
    except ModuleNotFoundError as exc:  # pragma: no cover
        raise SystemExit(
            "Missing dependency: PyMuPDF\n"
            "\n"
            "Create a local venv and install it:\n"
            "  python3 -m venv .venv\n"
            "  . .venv/bin/activate\n"
            "  python3 -m pip install pymupdf\n"
        ) from exc
    return fitz


def _sanitize_filename(name: str, max_len: int = 120) -> str:
    cleaned = re.sub(r"[^\w\s.-]+", "", name, flags=re.UNICODE).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    if not cleaned:
        cleaned = "chapter"
    if len(cleaned) > max_len:
        cleaned = cleaned[:max_len].rstrip()
    return cleaned


def _iter_pages(doc: "object", start_page: int, end_page_inclusive: int) -> Iterable[str]:
    # Pages are 0-indexed in PyMuPDF.
    for page_number in range(start_page, end_page_inclusive + 1):
        page = doc.load_page(page_number)
        yield page.get_text("text")


@dataclass(frozen=True)
class Chapter:
    index: int
    title: str
    level: int
    start_page_1based: int
    end_page_1based: int
    out_file: str
    char_count: int


def _chapters_from_toc(
    toc: list[list[int | str]],
    *,
    level: int,
    page_count: int,
) -> list[tuple[int, str, int, int]]:
    # PyMuPDF get_toc(simple=True) => [ [level, title, page_1based], ... ]
    filtered: list[tuple[int, str, int]] = []
    for entry in toc:
        if len(entry) < 3:
            continue
        entry_level, title, page_1based = entry[0], entry[1], entry[2]
        if not isinstance(entry_level, int) or not isinstance(title, str) or not isinstance(page_1based, int):
            continue
        if entry_level != level:
            continue
        if page_1based < 1:
            continue
        if page_1based > page_count:
            continue
        filtered.append((entry_level, title.strip(), page_1based))

    # De-dupe by same page start (keep first title).
    deduped: list[tuple[int, str, int]] = []
    seen_pages: set[int] = set()
    for entry_level, title, page_1based in filtered:
        if page_1based in seen_pages:
            continue
        seen_pages.add(page_1based)
        deduped.append((entry_level, title, page_1based))

    deduped.sort(key=lambda x: x[2])
    if not deduped:
        return []

    chapters: list[tuple[int, str, int, int]] = []
    for i, (entry_level, title, start_page_1based) in enumerate(deduped):
        next_start = deduped[i + 1][2] if i + 1 < len(deduped) else (page_count + 1)
        end_page_1based = max(start_page_1based, next_start - 1)
        chapters.append((entry_level, title, start_page_1based, end_page_1based))
    return chapters


def _chapters_from_regex(
    doc: "object",
    *,
    pattern: re.Pattern[str],
    page_count: int,
    max_pages_scan: int | None,
) -> list[tuple[int, str, int, int]]:
    limit = page_count if max_pages_scan is None else min(page_count, max_pages_scan)
    starts: list[tuple[int, str]] = []
    for page_idx in range(limit):
        text = doc.load_page(page_idx).get_text("text")
        first_lines = "\n".join(text.splitlines()[:20])
        match = pattern.search(first_lines)
        if not match:
            continue
        title = match.group(0).strip()
        starts.append((page_idx + 1, title))

    # De-dupe consecutive hits on same page.
    deduped: list[tuple[int, str]] = []
    seen: set[int] = set()
    for page_1based, title in starts:
        if page_1based in seen:
            continue
        seen.add(page_1based)
        deduped.append((page_1based, title))

    deduped.sort(key=lambda x: x[0])
    if not deduped:
        return []

    chapters: list[tuple[int, str, int, int]] = []
    for i, (start_page_1based, title) in enumerate(deduped):
        next_start = deduped[i + 1][0] if i + 1 < len(deduped) else (page_count + 1)
        end_page_1based = max(start_page_1based, next_start - 1)
        chapters.append((1, title, start_page_1based, end_page_1based))
    return chapters


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Split a PDF into per-chapter plain text files.\n\n"
            "Preferred mode uses the PDF outline / Table of Contents (ToC)."
        )
    )
    parser.add_argument("pdf", type=Path, help="Path to the PDF file")
    parser.add_argument(
        "-o",
        "--out",
        type=Path,
        default=None,
        help="Output directory (default: <pdf_dir>/<pdf_stem>_chapters)",
    )
    parser.add_argument(
        "--level",
        type=int,
        default=1,
        help="ToC level to treat as chapters (default: 1)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List detected chapters and exit (no files written)",
    )
    parser.add_argument(
        "--include-title-regex",
        type=str,
        default=None,
        help="Only keep chapters whose title matches this regex (applied after detection)",
    )
    parser.add_argument(
        "--exclude-title-regex",
        type=str,
        default=None,
        help="Drop chapters whose title matches this regex (applied after detection)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite output directory if it already exists",
    )
    parser.add_argument(
        "--fallback-regex",
        action="store_true",
        help="If ToC is missing, try regex-based chapter detection",
    )
    parser.add_argument(
        "--regex",
        type=str,
        default=r"(?im)^\s*(chapter\s+[0-9]+|chapter\s+[ivxlcdm]+)\b.*$",
        help="Regex used with --fallback-regex (default matches 'Chapter 1', 'CHAPTER IV', etc.)",
    )
    parser.add_argument(
        "--max-pages-scan",
        type=int,
        default=None,
        help="Only scan first N pages for --fallback-regex (default: all)",
    )
    args = parser.parse_args()

    pdf_path: Path = args.pdf
    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}", file=sys.stderr)
        return 2

    fitz = _require_pymupdf()
    doc = fitz.open(os.fspath(pdf_path))

    out_dir = args.out
    if out_dir is None:
        out_dir = pdf_path.parent / f"{pdf_path.stem}_chapters"

    toc = doc.get_toc(simple=True)
    chapters_raw = _chapters_from_toc(toc, level=args.level, page_count=doc.page_count)
    used_mode = "toc"

    if not chapters_raw and args.fallback_regex:
        pattern = re.compile(args.regex)
        chapters_raw = _chapters_from_regex(
            doc,
            pattern=pattern,
            page_count=doc.page_count,
            max_pages_scan=args.max_pages_scan,
        )
        used_mode = "regex"

    if chapters_raw and (args.include_title_regex or args.exclude_title_regex):
        include_re = re.compile(args.include_title_regex) if args.include_title_regex else None
        exclude_re = re.compile(args.exclude_title_regex) if args.exclude_title_regex else None
        filtered: list[tuple[int, str, int, int]] = []
        for lvl, title, start_1, end_1 in chapters_raw:
            if include_re and not include_re.search(title):
                continue
            if exclude_re and exclude_re.search(title):
                continue
            filtered.append((lvl, title, start_1, end_1))
        chapters_raw = filtered

    if not chapters_raw:
        print(
            "No chapters detected.\n"
            "\n"
            "- If your PDF has a clickable outline/ToC, try a different --level.\n"
            "- If it has no outline, try --fallback-regex.\n"
            "\n"
            "Tip: list outlines with:\n"
            f"  {Path(sys.argv[0]).name} {pdf_path} --list --level 1\n",
            file=sys.stderr,
        )
        return 1

    if args.list:
        print(f"Detected chapters via: {used_mode}")
        for i, (_lvl, title, start_1, end_1) in enumerate(chapters_raw, start=1):
            print(f"{i:02d}. p{start_1}–p{end_1}: {title}")
        return 0

    if out_dir.exists():
        if not out_dir.is_dir():
            print(f"Output path exists and is not a directory: {out_dir}", file=sys.stderr)
            return 2
        if not args.force:
            print(
                f"Output directory already exists: {out_dir}\n"
                "Re-run with --force to overwrite.",
                file=sys.stderr,
            )
            return 2
        for child in out_dir.iterdir():
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                # Keep it simple; only delete expected contents.
                for p in child.rglob("*"):
                    if p.is_file():
                        p.unlink()
                for p in sorted(child.rglob("*"), reverse=True):
                    if p.is_dir():
                        p.rmdir()
                child.rmdir()

    out_dir.mkdir(parents=True, exist_ok=True)

    manifest: dict[str, object] = {
        "pdf": str(pdf_path),
        "page_count": doc.page_count,
        "mode": used_mode,
        "toc_level": args.level if used_mode == "toc" else None,
        "chapters": [],
    }

    chapters_written: list[Chapter] = []
    for idx, (lvl, title, start_1, end_1) in enumerate(chapters_raw, start=1):
        safe_title = _sanitize_filename(title)
        out_name = f"{idx:02d} - {safe_title}.txt"
        out_path = out_dir / out_name

        start_0 = start_1 - 1
        end_0 = end_1 - 1
        combined = "".join(_iter_pages(doc, start_0, end_0))
        # Normalize line endings and trim trailing whitespace.
        combined = combined.replace("\r\n", "\n").replace("\r", "\n")
        combined = "\n".join(line.rstrip() for line in combined.splitlines()).rstrip() + "\n"

        out_path.write_text(combined, encoding="utf-8")
        chapter = Chapter(
            index=idx,
            title=title,
            level=lvl,
            start_page_1based=start_1,
            end_page_1based=end_1,
            out_file=str(out_path),
            char_count=len(combined),
        )
        chapters_written.append(chapter)

    manifest["chapters"] = [asdict(ch) for ch in chapters_written]
    (out_dir / "chapters.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"Wrote {len(chapters_written)} chapter files to: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
