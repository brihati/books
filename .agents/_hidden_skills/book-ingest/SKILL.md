---
name: book-ingest
description: Use when adding a new book, PDF, manuscript, or chapter set to the local book preservation workspace; covers PDF chapter splitting, book manifests, directory setup, and source-preserving ingestion before summarization or retrieval.
---

# Book Ingest

Use this skill before preservation, summarization, or Q&A when a book has not yet been normalized into the local workspace.

## Local Tooling

Primary scripts live in `/Users/sachin/books/tools/`:

- `pdf_split_chapters.py`: split a PDF into per-chapter `.txt` files using a PDF outline/ToC or regex fallback.
- `book_pipeline.py`: create book manifests, chunks, note skeletons, prompts, indexes, and validation checks.

## Workflow

1. Identify the source.

- PDF source: use `tools/pdf_split_chapters.py` first.
- Existing chapter `.txt` files: skip PDF splitting and initialize the book directly.
- Keep source files intact. Generated artifacts should live under the book directory.

2. Split PDFs into chapter text.

Use the PDF ToC when available:

```bash
python3 tools/pdf_split_chapters.py "files/Book Name/book.pdf" --list --level 1
python3 tools/pdf_split_chapters.py "files/Book Name/book.pdf" --level 1 --include-title-regex '(?i)^\s*chapter\s+[0-9]+'
```

Use `--fallback-regex` only when the PDF has no useful outline.

3. Initialize the book manifest.

```bash
python3 tools/book_pipeline.py init-book "files/Book Name" --title "Book Name" --book-id book-name
```

4. Chunk the chapters.

```bash
python3 tools/book_pipeline.py chunk "files/Book Name" --target-chars 7000 --overlap-chars 700
```

5. Prepare extraction artifacts.

```bash
python3 tools/book_pipeline.py prepare-notes "files/Book Name" --force
python3 tools/book_pipeline.py build-index "files/Book Name"
python3 tools/book_pipeline.py validate "files/Book Name" --max-chars 9000
```

## Output Contract

The ingestion pass should produce:

- `manifests/book.json`
- `manifests/chunks.json`
- `chunks/*.jsonl`
- `notes/*.jsonl`
- `prompts/<chapter-id>/<chunk-id>.md`
- `indexes/search.sqlite`

The original PDF and chapter text files remain the source of truth.
