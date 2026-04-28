---
name: book-hierarchical-summary
description: Use when generating section, chapter, or book-level summaries from preserved chunk notes; covers hierarchical summarization, detail retention, deduplication, and summaries that remain traceable to chunk IDs.
---

# Book Hierarchical Summary

Use this skill after chunk notes exist. The summary should be generated from preserved notes and retrieved chunks, not by loading a full chapter at once.

## Hierarchy

Use this order:

```text
chunk notes -> section summaries -> chapter summary -> book summary
```

If a chapter is small enough to fit in context, still prefer chunk notes when they exist because they preserve source IDs and reduce detail loss.

## Merge Rules

- Preserve original sequence unless the user asks for a thematic summary.
- Deduplicate repeated points.
- Keep examples, stories, and case studies attached to the idea they support.
- Keep names, dates, numbers, definitions, and terms when they matter.
- Do not add claims that are not present in the notes or retrieved chunks.
- Mark ambiguity rather than smoothing it over.
- Cite or mention relevant `chapter_id` / `chunk_id` when the output will be used for later retrieval.

## Default Chapter Output

For each chapter, produce:

1. Chapter title
2. Detailed but compressed summary
3. Key points
4. Important examples or stories
5. Definitions and terms
6. Names, dates, numbers, and places
7. Short relevant quotes or standout statements
8. Actionable lessons
9. Source chunk IDs

## Practical Flow

1. Read the relevant `notes/<chapter-id>.jsonl`.
2. If notes are empty or incomplete, retrieve source chunks with:

```bash
python3 tools/book_pipeline.py search "files/Book Name" "topic or phrase" --limit 8
```

3. Summarize by chunk group first when the chapter has many chunks.
4. Merge group summaries into the chapter summary.
5. Rebuild or update `summaries/<chapter-id>.md`.

To generate merge prompts from existing chunk notes:

```bash
python3 tools/book_pipeline.py prepare-summaries "files/Book Name"
```
