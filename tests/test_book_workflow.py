from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.book_pipeline import _write_json, _write_jsonl
from tools.book_workflow import audit_book, extract_notes, full_workflow, generate_book_skill, generate_summaries, ingest_source, preserve_book


class BookWorkflowTests(unittest.TestCase):
    def _make_book(self, root: Path) -> Path:
        book_dir = root / "book"
        chapters_dir = book_dir / "chapters"
        chapters_dir.mkdir(parents=True, exist_ok=True)

        chapter_id = "chapter-01-alpha"
        chapter_title = "CHAPTER 1 ALPHA"
        chapter_path = chapters_dir / "CHAPTER 1 ALPHA.txt"
        chapter_path.write_text("Alpha chapter source text.\n", encoding="utf-8")

        note = {
            "book_id": "synthetic-book",
            "chapter_id": chapter_id,
            "chunk_id": f"{chapter_id}-chunk-001",
            "source": {
                "chapter_title": chapter_title,
                "source_path": str(chapter_path),
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

        _write_jsonl(book_dir / "notes" / f"{chapter_id}.jsonl", [note])
        (book_dir / "summaries").mkdir(parents=True, exist_ok=True)
        (book_dir / "summaries" / f"{chapter_id}.md").write_text(
            "# Alpha\n\nThis is the canonical chapter summary.\n",
            encoding="utf-8",
        )
        (book_dir / "summary").mkdir(parents=True, exist_ok=True)
        (book_dir / "summary" / "01 - Chapter 1 - Alpha.md").write_text(
            "# Legacy alpha\n\nThis is stale legacy content.\n",
            encoding="utf-8",
        )
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
        return book_dir

    def _make_raw_book(self, root: Path) -> Path:
        book_dir = root / "raw-book"
        chapters_dir = book_dir / "chapters"
        chapters_dir.mkdir(parents=True, exist_ok=True)
        (chapters_dir / "CHAPTER 1 ALPHA.txt").write_text(
            "Alpha chapter source text.\n\nA second paragraph adds enough content for extraction.\n",
            encoding="utf-8",
        )
        return book_dir

    def _make_runner(self, root: Path, *, wrong_chunk: bool = False) -> str:
        runner_path = root / "fake_runner.py"
        runner_path.write_text(
            "\n".join(
                [
                    "import json",
                    "import re",
                    "import sys",
                    "",
                    "prompt = sys.stdin.read()",
                    "chapter_match = re.search(r'Chapter ID: ([^\\n]+)', prompt)",
                    "chunk_match = re.search(r'\\\"chunk_id\\\": \\\"([^\\\"]+)\\\"', prompt)",
                    "chapter_id = chapter_match.group(1).strip() if chapter_match else None",
                    "chunk_id = chunk_match.group(1) if chunk_match else None",
                    "if prompt.lstrip().startswith('Create a source-linked hierarchical chapter summary from these chunk notes.'):",
                    "    print(f'# {chapter_id}\\n\\nSummary for {chapter_id}.\\n\\n## Source chunk IDs used\\n- {chapter_id}-chunk-001')",
                    "    raise SystemExit(0)",
                    "payload = {",
                    "    'chapter_id': chapter_id,",
                    f"    'chunk_id': 'wrong-chunk' if {str(wrong_chunk)} else chunk_id,",
                    "    'summary': f'Filled summary for {chunk_id}.',",
                    "    'key_points': [f'Key point for {chunk_id}.'],",
                    "    'arguments': [],",
                    "    'examples': [f'Example for {chunk_id}.'],",
                    "    'stories': [],",
                    "    'definitions': [],",
                    "    'names': [],",
                    "    'dates': [],",
                    "    'numbers': [],",
                    "    'places': [],",
                    "    'terms': [],",
                    "    'quotes': [],",
                    "    'actionable_lessons': [f'Action for {chunk_id}.'],",
                    "    'open_questions': [],",
                    "}",
                    "print(json.dumps(payload))",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        return f"{sys.executable} {runner_path}"

    def test_preserve_and_generate_skill(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            book_dir = self._make_book(root)

            result = preserve_book(book_dir, title="Synthetic Book", book_id="synthetic-book")
            self.assertEqual(result, 0)
            self.assertTrue((book_dir / "indexes" / "search.sqlite").exists())
            self.assertTrue((book_dir / "prompts" / "summaries" / "chapter-01-alpha.md").exists())

            skill_dir = generate_book_skill(
                book_dir,
                skill_name="synthetic-book-coach",
                skill_root=root / "skills",
                force=True,
            )

            self.assertTrue((skill_dir / "SKILL.md").exists())
            self.assertTrue((skill_dir / "agents" / "openai.yaml").exists())
            self.assertTrue((skill_dir / "references" / "local-book-map.md").exists())

            skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("Synthetic Book", skill_text)
            self.assertIn("chapter-01-alpha", (skill_dir / "references" / "local-book-map.md").read_text(encoding="utf-8"))

    def test_ingest_pdf_invokes_splitter(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pdf_path = root / "Sample Book.pdf"
            pdf_path.write_bytes(b"%PDF-1.4\n")

            with patch("tools.book_workflow.subprocess.run") as run_mock:
                book_dir = ingest_source(pdf_path, force=True)

            self.assertEqual(book_dir, root.resolve())
            self.assertTrue((root / "chapters").exists())
            self.assertTrue(run_mock.called)
            args = run_mock.call_args.args[0]
            self.assertIn(str(pdf_path.resolve()), args)
            self.assertIn("--force", args)
            self.assertIn("--fallback-regex", args)

    def test_full_workflow_uses_existing_chapters(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            book_dir = self._make_book(root)

            target_book_dir, skill_dir = full_workflow(
                book_dir,
                book_dir=book_dir,
                title="Synthetic Book",
                book_id="synthetic-book",
                generate_skill=True,
                skill_name="synthetic-book-coach",
                skill_root=root / "skills",
                force_skill=True,
            )

            self.assertEqual(target_book_dir, book_dir.resolve())
            self.assertIsNotNone(skill_dir)
            self.assertTrue((book_dir / "manifests" / "chunks.json").exists())
            self.assertTrue((skill_dir / "SKILL.md").exists())

    def test_preserve_book_end_to_end_with_runner(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            book_dir = self._make_raw_book(root)
            runner_cmd = self._make_runner(root)

            result = preserve_book(book_dir, title="Raw Book", book_id="raw-book", runner_cmd=runner_cmd)

            self.assertEqual(result, 0)
            note_path = book_dir / "notes" / "chapter-01-alpha.jsonl"
            rows = [json.loads(line) for line in note_path.read_text(encoding="utf-8").splitlines() if line.strip()]
            self.assertTrue(rows)
            self.assertEqual(rows[0]["summary"], "Filled summary for chapter-01-alpha-chunk-001.")
            summary_text = (book_dir / "summaries" / "chapter-01-alpha.md").read_text(encoding="utf-8")
            self.assertIn("Summary for chapter-01-alpha.", summary_text)
            audit = audit_book(book_dir)
            self.assertTrue(audit["validate_ok"])
            self.assertGreater(audit["filled_note_count"], 0)

    def test_extract_notes_rejects_wrong_chunk_id(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            book_dir = self._make_raw_book(root)
            preserve_book(book_dir, title="Raw Book", book_id="raw-book", skip_validate=True)

            with self.assertRaisesRegex(ValueError, "wrong chunk_id"):
                extract_notes(book_dir, runner_cmd=self._make_runner(root, wrong_chunk=True), force=True)

    def test_generate_summaries_requires_filled_notes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            book_dir = self._make_raw_book(root)
            preserve_book(book_dir, title="Raw Book", book_id="raw-book", skip_validate=True)

            with self.assertRaisesRegex(RuntimeError, "untouched notes remain"):
                generate_summaries(book_dir, runner_cmd=self._make_runner(root), force=True)

    def test_full_workflow_generates_skill_with_runner(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            book_dir = self._make_raw_book(root)
            runner_cmd = self._make_runner(root)

            target_book_dir, skill_dir = full_workflow(
                book_dir,
                book_dir=book_dir,
                title="Raw Book",
                book_id="raw-book",
                runner_cmd=runner_cmd,
                generate_skill=True,
                force_skill=True,
                skill_root=root / "skills",
            )

            self.assertEqual(target_book_dir, book_dir.resolve())
            self.assertIsNotNone(skill_dir)
            self.assertTrue((skill_dir / "references" / "local-book-map.md").exists())
            self.assertTrue((book_dir / "summaries" / "chapter-01-alpha.md").exists())

    def test_default_generated_skill_name_starts_with_book(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            book_dir = self._make_book(root)

            skill_dir = generate_book_skill(book_dir, skill_root=root / "skills", force=True)

            self.assertEqual(skill_dir.name, "book-synthetic-book-coach")
            openai_yaml = (skill_dir / "agents" / "openai.yaml").read_text(encoding="utf-8")
            self.assertIn('display_name: "Book Synthetic Book Coach"', openai_yaml)


if __name__ == "__main__":
    unittest.main()
