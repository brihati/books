---
name: book-query
description: Use when answering questions from preserved local book content; covers retrieval from chunk text, structured notes, examples, quotes, definitions, and source-linked answers without relying on memory.
---

# Book Query

Use this skill when the user asks a question about a preserved local book, chapter, concept, quote, example, or tactic.

## Retrieval First

Search the local index before answering:

```bash
python3 tools/book_pipeline.py search "files/Book Name" "query terms" --limit 8
```

Use the retrieved chunks and notes as the answer basis. Do not rely on memory when the local book exists.

## Answer Rules

- Answer only from retrieved source chunks, filled notes, or existing summaries.
- Prefer specific chapter/chunk references over vague book-level claims.
- If retrieved evidence is weak, say what was found and what remains uncertain.
- For quotes, use only short excerpts that appear in the retrieved source.
- For coaching or application, separate book-grounded material from your own applied advice.

## Search Tactics

Use multiple searches for broad concepts:

```bash
python3 tools/book_pipeline.py search "files/Book Name" "tactical empathy" --limit 8
python3 tools/book_pipeline.py search "files/Book Name" "labeling emotions" --limit 8
python3 tools/book_pipeline.py search "files/Book Name" "that's right" --limit 8
```

Search across:

- concept names
- alternate phrases
- examples or story names
- chapter titles
- quoted phrases

## Output Shape

Default to:

- direct answer
- supporting points
- source references by `chapter_id` / `chunk_id`
- relevant short quotes only when useful
- limitations if the index or notes are incomplete
