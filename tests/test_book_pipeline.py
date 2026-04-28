from __future__ import annotations

import io
import json
import sqlite3
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from tools.book_pipeline import cmd_build_index, cmd_import_summaries, cmd_setup, cmd_validate
from tools.book_pipeline import _write_json, _write_jsonl


class BookPipelineTests(unittest.TestCase):
    def _make_book(self, root: Path, *, canonical_summary: str | None = None, legacy_summary: str | None = None, note_rows: list[dict] | None = None) -> Path:
        book_dir = root / "book"
        for rel in ["chapters", "chunks", "notes", "prompts/summaries", "summaries", "summary", "indexes", "manifests"]:
            (book_dir / rel).mkdir(parents=True, exist_ok=True)

        chapter_id = "chapter-01-alpha"
        chapter_title = "CHAPTER 1 | ALPHA"
        chapter_path = book_dir / "chapters" / "01 - CHAPTER 1 ALPHA.txt"
        chapter_path.write_text("Alpha chapter source text.\n", encoding="utf-8")

        _write_json(
            book_dir / "manifests" / "book.json",
            {
                "book_id": "synthetic-book",
                "title": "Synthetic Book",
                "book_dir": str(book_dir),
                "chapter_count": 1,
                "chapters": [
                    {
                        "chapter_id": chapter_id,
                        "index": 1,
                        "title": chapter_title,
                        "path": str(chapter_path),
                        "start_page": 1,
                        "end_page": 2,
                        "char_count": len(chapter_path.read_text(encoding="utf-8")),
                    }
                ],
            },
        )
        _write_json(
            book_dir / "manifests" / "chunks.json",
            {
                "book_id": "synthetic-book",
                "target_chars": 7000,
                "overlap_chars": 700,
                "chunk_count": 1,
                "chapters": [{"chapter_id": chapter_id, "title": chapter_title, "chunk_count": 1}],
            },
        )

        chunk = {
            "book_id": "synthetic-book",
            "chapter_id": chapter_id,
            "chunk_id": f"{chapter_id}-chunk-001",
            "chunk_index": 1,
            "chapter_title": chapter_title,
            "source_path": str(chapter_path),
            "source_pages": "1-2",
            "char_start": 0,
            "char_end": 27,
            "text": "Alpha chapter source text.\n",
            "checksum": "deadbeefdeadbeef",
        }
        _write_jsonl(book_dir / "chunks" / f"{chapter_id}.jsonl", [chunk])

        if note_rows is not None:
            _write_jsonl(book_dir / "notes" / f"{chapter_id}.jsonl", note_rows)

        if canonical_summary is not None:
            (book_dir / "summaries" / f"{chapter_id}.md").write_text(canonical_summary, encoding="utf-8")

        if legacy_summary is not None:
            (book_dir / "summary" / "01 - Chapter 1 - Alpha.md").write_text(legacy_summary, encoding="utf-8")

        return book_dir

    def _read_summary_row(self, book_dir: Path) -> tuple[str, str, str]:
        conn = sqlite3.connect(book_dir / "indexes" / "search.sqlite")
        try:
            row = conn.execute(
                "SELECT chapter_id, body, metadata FROM docs WHERE kind = 'summary' ORDER BY rowid LIMIT 1"
            ).fetchone()
            self.assertIsNotNone(row)
            chapter_id, body, metadata = row
            return str(chapter_id), str(body), str(metadata)
        finally:
            conn.close()

    def test_validate_passes_with_populated_notes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            note_rows = [
                {
                    "book_id": "synthetic-book",
                    "chapter_id": "chapter-01-alpha",
                    "chunk_id": "chapter-01-alpha-chunk-001",
                    "source": {
                        "chapter_title": "CHAPTER 1 | ALPHA",
                        "source_path": str(root / "book" / "chapters" / "01 - CHAPTER 1 ALPHA.txt"),
                        "source_pages": "1-2",
                        "char_start": 0,
                        "char_end": 27,
                        "checksum": "deadbeefdeadbeef",
                    },
                    "summary": "A filled note summary.",
                    "key_points": ["The chapter opens with the premise."],
                    "arguments": [],
                    "examples": [],
                    "stories": [],
                    "definitions": [],
                    "names": [],
                    "dates": [],
                    "numbers": [],
                    "places": [],
                    "terms": [],
                    "quotes": [],
                    "actionable_lessons": [],
                    "open_questions": [],
                }
            ]
            book_dir = self._make_book(root, note_rows=note_rows)
            cmd_build_index(type("Args", (), {"book_dir": book_dir})())

            buf = io.StringIO()
            with redirect_stdout(buf):
                result = cmd_validate(type("Args", (), {"book_dir": book_dir, "max_chars": 12000})())

            self.assertEqual(result, 0, buf.getvalue())
            self.assertIn("Validation passed", buf.getvalue())

    def test_setup_returns_validation_failure_for_skeleton_notes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            book_dir = root / "book"
            chapters_dir = book_dir / "chapters"
            chapters_dir.mkdir(parents=True, exist_ok=True)
            (chapters_dir / "CHAPTER 1 ALPHA.txt").write_text("Alpha chapter source text.\n", encoding="utf-8")

            result = cmd_setup(
                type(
                    "Args",
                    (),
                    {
                        "book_dir": book_dir,
                        "title": "Synthetic Book",
                        "book_id": "synthetic-book",
                        "target_chars": 7000,
                        "overlap_chars": 700,
                        "force_notes": False,
                        "force_summaries": False,
                        "skip_validate": False,
                        "max_chars": 12000,
                    },
                )()
            )

            self.assertEqual(result, 1)

    def test_validate_fails_when_notes_file_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            book_dir = self._make_book(root)
            cmd_build_index(type("Args", (), {"book_dir": book_dir})())

            buf = io.StringIO()
            with redirect_stdout(buf):
                result = cmd_validate(type("Args", (), {"book_dir": book_dir, "max_chars": 12000})())

            self.assertEqual(result, 1)
            output = buf.getvalue()
            self.assertIn("missing note file for chapter chapter-01-alpha", output)
            self.assertIn("notes/chapter-01-alpha.jsonl", output)

    def test_validate_fails_on_untouched_note_skeleton(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            note_rows = [
                {
                    "book_id": "synthetic-book",
                    "chapter_id": "chapter-01-alpha",
                    "chunk_id": "chapter-01-alpha-chunk-001",
                    "source": {
                        "chapter_title": "CHAPTER 1 | ALPHA",
                        "source_path": str(root / "book" / "chapters" / "01 - CHAPTER 1 ALPHA.txt"),
                        "source_pages": "1-2",
                        "char_start": 0,
                        "char_end": 27,
                        "checksum": "deadbeefdeadbeef",
                    },
                    "summary": "",
                    "key_points": [],
                    "arguments": [],
                    "examples": [],
                    "stories": [],
                    "definitions": [],
                    "names": [],
                    "dates": [],
                    "numbers": [],
                    "places": [],
                    "terms": [],
                    "quotes": [],
                    "actionable_lessons": [],
                    "open_questions": [],
                }
            ]
            book_dir = self._make_book(root, note_rows=note_rows)
            cmd_build_index(type("Args", (), {"book_dir": book_dir})())

            buf = io.StringIO()
            with redirect_stdout(buf):
                result = cmd_validate(type("Args", (), {"book_dir": book_dir, "max_chars": 12000})())

            self.assertEqual(result, 1)
            output = buf.getvalue()
            self.assertIn("untouched note skeleton for chunk chapter-01-alpha-chunk-001", output)

    def test_validate_fails_when_search_index_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            note_rows = [
                {
                    "book_id": "synthetic-book",
                    "chapter_id": "chapter-01-alpha",
                    "chunk_id": "chapter-01-alpha-chunk-001",
                    "source": {
                        "chapter_title": "CHAPTER 1 | ALPHA",
                        "source_path": str(root / "book" / "chapters" / "01 - CHAPTER 1 ALPHA.txt"),
                        "source_pages": "1-2",
                        "char_start": 0,
                        "char_end": 27,
                        "checksum": "deadbeefdeadbeef",
                    },
                    "summary": "A filled note summary.",
                    "key_points": ["The chapter opens with the premise."],
                    "arguments": [],
                    "examples": [],
                    "stories": [],
                    "definitions": [],
                    "names": [],
                    "dates": [],
                    "numbers": [],
                    "places": [],
                    "terms": [],
                    "quotes": [],
                    "actionable_lessons": [],
                    "open_questions": [],
                }
            ]
            book_dir = self._make_book(root, note_rows=note_rows)

            buf = io.StringIO()
            with redirect_stdout(buf):
                result = cmd_validate(type("Args", (), {"book_dir": book_dir, "max_chars": 12000})())

            self.assertEqual(result, 1)
            self.assertIn("missing search index", buf.getvalue())

    def test_canonical_summary_wins_over_legacy(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            note_rows = [
                {
                    "book_id": "synthetic-book",
                    "chapter_id": "chapter-01-alpha",
                    "chunk_id": "chapter-01-alpha-chunk-001",
                    "source": {
                        "chapter_title": "CHAPTER 1 | ALPHA",
                        "source_path": str(root / "book" / "chapters" / "01 - CHAPTER 1 ALPHA.txt"),
                        "source_pages": "1-2",
                        "char_start": 0,
                        "char_end": 27,
                        "checksum": "deadbeefdeadbeef",
                    },
                    "summary": "A filled note summary.",
                    "key_points": ["The chapter opens with the premise."],
                    "arguments": [],
                    "examples": [],
                    "stories": [],
                    "definitions": [],
                    "names": [],
                    "dates": [],
                    "numbers": [],
                    "places": [],
                    "terms": [],
                    "quotes": [],
                    "actionable_lessons": [],
                    "open_questions": [],
                }
            ]
            canonical_summary = "# Canonical summary\n\nThis is the canonical chapter summary.\n"
            legacy_summary = "# Legacy summary\n\nThis is stale legacy content.\n"
            book_dir = self._make_book(
                root,
                canonical_summary=canonical_summary,
                legacy_summary=legacy_summary,
                note_rows=note_rows,
            )

            cmd_build_index(type("Args", (), {"book_dir": book_dir})())
            chapter_id, body, metadata = self._read_summary_row(book_dir)

            self.assertEqual(chapter_id, "chapter-01-alpha")
            self.assertEqual(body, canonical_summary.strip())
            self.assertIn("/summaries/chapter-01-alpha.md", json.loads(metadata)["source_path"])
            self.assertNotIn("legacy", body.lower())

    def test_legacy_summary_imports_and_indexes_when_canonical_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            note_rows = [
                {
                    "book_id": "synthetic-book",
                    "chapter_id": "chapter-01-alpha",
                    "chunk_id": "chapter-01-alpha-chunk-001",
                    "source": {
                        "chapter_title": "CHAPTER 1 | ALPHA",
                        "source_path": str(root / "book" / "chapters" / "01 - CHAPTER 1 ALPHA.txt"),
                        "source_pages": "1-2",
                        "char_start": 0,
                        "char_end": 27,
                        "checksum": "deadbeefdeadbeef",
                    },
                    "summary": "A filled note summary.",
                    "key_points": ["The chapter opens with the premise."],
                    "arguments": [],
                    "examples": [],
                    "stories": [],
                    "definitions": [],
                    "names": [],
                    "dates": [],
                    "numbers": [],
                    "places": [],
                    "terms": [],
                    "quotes": [],
                    "actionable_lessons": [],
                    "open_questions": [],
                }
            ]
            legacy_summary = "# Legacy summary\n\nThis content should be promoted.\n"
            book_dir = self._make_book(root, legacy_summary=legacy_summary, note_rows=note_rows)

            cmd_import_summaries(type("Args", (), {"book_dir": book_dir, "force": False})())
            promoted = book_dir / "summaries" / "chapter-01-alpha.md"
            self.assertTrue(promoted.exists())
            self.assertEqual(promoted.read_text(encoding="utf-8").strip(), legacy_summary.strip())

            cmd_build_index(type("Args", (), {"book_dir": book_dir})())
            chapter_id, body, metadata = self._read_summary_row(book_dir)

            self.assertEqual(chapter_id, "chapter-01-alpha")
            self.assertEqual(body, legacy_summary.strip())
            self.assertIn("/summaries/chapter-01-alpha.md", json.loads(metadata)["source_path"])


if __name__ == "__main__":
    unittest.main()
