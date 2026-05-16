from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.book_pipeline import _write_json, _write_jsonl, cmd_build_index
from tools.cognee_bookwiki import (
    ingest_books,
    lint_wiki,
    promote_query_page,
    query_books,
)


class CogneeBookWikiTests(unittest.TestCase):
    def _make_book(self, root: Path) -> Path:
        book_dir = root / "files" / "Synthetic Pricing"
        for rel in ["chapters", "chunks", "notes", "summaries", "indexes", "manifests"]:
            (book_dir / rel).mkdir(parents=True, exist_ok=True)

        chapter_id = "chapter-01-pricing-metric"
        chapter_path = book_dir / "chapters" / "01 - Pricing Metric.txt"
        chapter_path.write_text(
            "A pricing metric determines how a SaaS company captures value from customers.\n",
            encoding="utf-8",
        )
        _write_json(
            book_dir / "manifests" / "book.json",
            {
                "book_id": "synthetic-pricing",
                "title": "Synthetic Pricing",
                "book_dir": str(book_dir),
                "chapter_count": 1,
                "chapters": [
                    {
                        "chapter_id": chapter_id,
                        "index": 1,
                        "title": "Pricing Metric",
                        "path": str(chapter_path),
                        "start_page": 1,
                        "end_page": 2,
                        "char_count": len(chapter_path.read_text(encoding="utf-8")),
                    }
                ],
            },
        )
        chunk = {
            "book_id": "synthetic-pricing",
            "chapter_id": chapter_id,
            "chunk_id": f"{chapter_id}-chunk-001",
            "chunk_index": 1,
            "chapter_title": "Pricing Metric",
            "source_path": str(chapter_path),
            "source_pages": "1-2",
            "char_start": 0,
            "char_end": 77,
            "text": "A pricing metric determines how a SaaS company captures value from customers.\n",
            "checksum": "deadbeefdeadbeef",
        }
        _write_jsonl(book_dir / "chunks" / f"{chapter_id}.jsonl", [chunk])
        note = {
            "book_id": "synthetic-pricing",
            "chapter_id": chapter_id,
            "chunk_id": f"{chapter_id}-chunk-001",
            "source": {
                "chapter_title": "Pricing Metric",
                "source_path": str(chapter_path),
                "source_pages": "1-2",
                "char_start": 0,
                "char_end": 77,
                "checksum": "deadbeefdeadbeef",
            },
            "summary": "Pricing metric selection controls how value is captured.",
            "key_points": ["A pricing metric should align with customer value."],
            "arguments": [],
            "examples": ["Per-seat pricing and usage-based pricing capture value differently."],
            "stories": [],
            "definitions": ["Pricing metric: the unit used to capture value from customers"],
            "names": [],
            "dates": [],
            "numbers": [],
            "places": [],
            "terms": ["Pricing metric", "Usage-based pricing", "Customer value"],
            "quotes": [],
            "actionable_lessons": ["Choose a metric that scales with delivered value."],
            "open_questions": [],
        }
        _write_jsonl(book_dir / "notes" / f"{chapter_id}.jsonl", [note])
        (book_dir / "summaries" / f"{chapter_id}.md").write_text(
            "# Pricing Metric\n\nPricing metrics connect packaging, value capture, and customer behavior.\n",
            encoding="utf-8",
        )
        cmd_build_index(type("Args", (), {"book_dir": book_dir})())
        return book_dir

    def test_ingest_writes_wiki_and_session_memory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_book(root)
            result = ingest_books(
                books_root=root / "files",
                requested_books=["Synthetic Pricing"],
                wiki_dir=root / "wiki",
                memory_dir=root / "memory",
                session_id="test-session",
                redis_url=None,
                use_redis=False,
                use_cognee=False,
                dataset="test",
                include_notes=True,
                max_chapters=None,
                max_note_packets=10,
                max_concepts=20,
            )

            self.assertEqual(result["book_count"], 1)
            self.assertGreater(result["packet_count"], 0)
            self.assertTrue((root / "wiki" / "index.md").exists())
            self.assertTrue((root / "wiki" / "books" / "synthetic-pricing.md").exists())
            self.assertTrue((root / "wiki" / "concepts" / "pricing-metric.md").exists())
            rows = [
                json.loads(line)
                for line in (root / "memory" / "bookwiki_session.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertEqual(rows[-1]["type"], "ingest")

    def test_query_promote_and_lint(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_book(root)
            ingest_books(
                books_root=root / "files",
                requested_books=None,
                wiki_dir=root / "wiki",
                memory_dir=root / "memory",
                session_id="test-session",
                redis_url=None,
                use_redis=False,
                use_cognee=False,
                dataset="test",
                include_notes=True,
                max_chapters=None,
                max_note_packets=10,
                max_concepts=20,
            )

            result = query_books(
                books_root=root / "files",
                requested_books=None,
                wiki_dir=root / "wiki",
                memory_dir=root / "memory",
                query="pricing metric customer value",
                session_id="test-session",
                redis_url=None,
                use_redis=False,
                use_cognee=False,
                dataset="test",
                limit=5,
                save_playbook=False,
            )
            self.assertGreater(result["hit_count"], 0)
            query_page = Path(result["query_page"])
            self.assertTrue(query_page.exists())
            self.assertIn("Source Hits", query_page.read_text(encoding="utf-8"))

            playbook = promote_query_page(
                query_page=query_page,
                wiki_dir=root / "wiki",
                memory_dir=root / "memory",
                session_id="test-session",
                redis_url=None,
                use_redis=False,
                use_cognee=False,
                dataset="test",
                feedback="Useful enough to persist.",
            )
            self.assertTrue(playbook.exists())
            self.assertIn("Useful enough", playbook.read_text(encoding="utf-8"))

            lint = lint_wiki(
                wiki_dir=root / "wiki",
                memory_dir=root / "memory",
                session_id="test-session",
                redis_url=None,
                use_redis=False,
            )
            self.assertGreaterEqual(lint["page_count"], 1)
            self.assertTrue((root / "wiki" / "lint.md").exists())


if __name__ == "__main__":
    unittest.main()
