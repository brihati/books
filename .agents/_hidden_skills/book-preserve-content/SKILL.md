---
name: book-preserve-content
description: Use when preserving book or chapter content in high detail without loading the full text into context; covers semantic chunking, structured chunk-note extraction, examples, quotes, definitions, facts, and source-linked preservation artifacts.
---

# Book Preserve Content

Use this skill when the goal is durable reuse of book content, not a one-shot summary.

## Principle

Do not make the chapter summary the source of truth. Preserve source-linked chunk notes first, then generate summaries, study notes, coaching material, or Q&A answers from those notes and retrieved chunks.

## Local Tooling

Use `/Users/sachin/books/tools/book_pipeline.py`.

Core commands:

```bash
python3 tools/book_pipeline.py chunk "files/Book Name" --target-chars 7000 --overlap-chars 700
python3 tools/book_pipeline.py prepare-notes "files/Book Name" --force
python3 tools/book_pipeline.py build-index "files/Book Name"
python3 tools/book_pipeline.py validate "files/Book Name" --max-chars 9000
```

## Chunk Note Schema

Each chunk note must preserve:

- `summary`
- `key_points`
- `arguments`
- `examples`
- `stories`
- `definitions`
- `names`
- `dates`
- `numbers`
- `places`
- `terms`
- `quotes`
- `actionable_lessons`
- `open_questions`

Keep source metadata intact:

- `book_id`
- `chapter_id`
- `chunk_id`
- `source.chapter_title`
- `source.source_path`
- `source.source_pages`
- `source.char_start`
- `source.char_end`
- `source.checksum`

## Extraction Rules

- Work chunk by chunk.
- Preserve concrete claims, examples, stories, definitions, names, dates, numbers, places, terminology, and short useful quotes.
- Keep examples attached to the idea they support.
- Preserve argumentative or chronological sequence when it matters.
- Use empty fields rather than inventing details.
- Quotes must be short and present in the source chunk.
- If an extraction is uncertain, put the uncertainty in `open_questions`.

## Process

1. Confirm the book has `chunks/*.jsonl`.
2. Run `prepare-notes` to generate JSONL skeletons and prompt packets.
3. Fill each note object from its matching prompt packet or source chunk.
4. Rebuild `indexes/search.sqlite`.
5. Validate with `book_pipeline.py validate`.

The filled `notes/*.jsonl` files become the durable knowledge layer.
