from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from tools import paper_extract


class FakeResponse:
    def __init__(self, data: bytes, content_type: str = "application/pdf") -> None:
        self._data = data
        self.headers = {"content-type": content_type}

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def read(self) -> bytes:
        return self._data


class PaperExtractTests(unittest.TestCase):
    def test_detect_references_heading_near_end(self) -> None:
        start, uncertain = paper_extract.detect_references_start(
            [
                "Abstract\nThis is a paper.",
                "Conclusion\nThe final result.",
                "References\n[1] Example citation.\n[2] Another citation.",
            ]
        )

        self.assertEqual(start, 2)
        self.assertFalse(uncertain)

    def test_detect_references_fallback_is_uncertain(self) -> None:
        start, uncertain = paper_extract.detect_references_start(
            [
                "Body",
                "[1] A\n[2] B\n[3] C\n[4] D\n[5] E",
            ]
        )

        self.assertEqual(start, 1)
        self.assertTrue(uncertain)

    def test_ensure_output_dir_refuses_existing_without_force(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp) / "paper"
            out_dir.mkdir()

            with self.assertRaises(FileExistsError):
                paper_extract.ensure_output_dir(out_dir, force=False)

    def test_download_pdf_rejects_non_pdf_response(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "paper.pdf"

            with self.assertRaises(ValueError):
                paper_extract.download_pdf(
                    "https://example.com/not-pdf",
                    out,
                    opener=lambda *_args, **_kwargs: FakeResponse(b"<html></html>", "text/html"),
                )

    def test_prepare_source_uses_downloader_for_url(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "paper.pdf"
            with patch("tools.paper_extract.download_pdf") as download_mock:
                download_mock.return_value = {"source_type": "url"}

                result = paper_extract.prepare_source("https://example.com/paper.pdf", out)

            self.assertEqual(result["source_type"], "url")
            download_mock.assert_called_once()

    def test_markdown_asset_paths_match_markdown_location(self) -> None:
        self.assertEqual(paper_extract.markdown_image_path("figure.png"), "../assets/figure.png")
        self.assertEqual(
            paper_extract.markdown_image_path("figure.png", from_pages_dir=True),
            "../../assets/figure.png",
        )

    def test_run_creates_manifest_for_local_pdf(self) -> None:
        fitz = paper_extract.require_pymupdf()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "sample.pdf"
            doc = fitz.open()
            page = doc.new_page()
            page.insert_text((72, 72), "Title\n\nReferences\n[1] Example reference.")
            doc.save(source)
            doc.close()

            out_dir = root / "bundle"
            result = paper_extract.run(
                SimpleNamespace(
                    input=str(source),
                    out=out_dir,
                    force=False,
                    render_pages="none",
                    image_min_area=paper_extract.DEFAULT_IMAGE_MIN_AREA,
                )
            )

            self.assertEqual(result, 0)
            self.assertTrue((out_dir / "source" / "paper.pdf").exists())
            self.assertTrue((out_dir / "content" / "full.md").exists())
            self.assertTrue((out_dir / "content" / "pages" / "page-001.md").exists())
            manifest = json.loads((out_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["extraction"]["page_count"], 1)
            self.assertEqual(manifest["extraction"]["references_start_page"], 1)


if __name__ == "__main__":
    unittest.main()
