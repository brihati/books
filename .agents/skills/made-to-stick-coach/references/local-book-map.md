# Local Book Map

Use this file to ground the generated skill in the user's local preserved book artifacts.

## Root Paths

- Book root: `/Users/sachin/books/files/Made to Stick/`
- Book manifest: `/Users/sachin/books/files/Made to Stick/manifests/book.json`
- Chunk manifest: `/Users/sachin/books/files/Made to Stick/manifests/chunks.json`
- Source chunks: `/Users/sachin/books/files/Made to Stick/chunks/`
- Chunk-note skeletons or filled notes: `/Users/sachin/books/files/Made to Stick/notes/`
- Chunk extraction prompts: `/Users/sachin/books/files/Made to Stick/prompts/`
- Chapter summary prompts: `/Users/sachin/books/files/Made to Stick/prompts/summaries/`
- Search index: `/Users/sachin/books/files/Made to Stick/indexes/search.sqlite`
- Full chapter text fallback: `/Users/sachin/books/files/Made to Stick/chapters/`
- Legacy summaries fallback: `/Users/sachin/books/files/Made to Stick/summary/`
- Canonical summaries: `/Users/sachin/books/files/Made to Stick/summaries/`

## Retrieval Rule

Search the preservation index first:

```bash
python3 tools/book_pipeline.py search "/Users/sachin/books/files/Made to Stick" "query terms" --limit 8
```

Use retrieved chunks and filled notes as primary grounding. Use summaries as a fallback for higher-level synthesis.

## Preservation Status

- Current chapter count: 4
- Current chunk count: 85
- Notes may be skeletons unless explicitly filled after chunk extraction.
- Search indexes raw chunks and any non-empty filled notes.

## Chapter Map

1. `CHAPTER 1`
   - Chapter ID: `chapter-01-chapter`
   - Chunks: `/Users/sachin/books/files/Made to Stick/chunks/chapter-01-chapter.jsonl`
   - Notes: `/Users/sachin/books/files/Made to Stick/notes/chapter-01-chapter.jsonl`
   - Summary: `/Users/sachin/books/files/Made to Stick/summaries/chapter-01-chapter.md`
   - Full: `/Users/sachin/books/files/Made to Stick/chapters/01 - CHAPTER 1.txt`
2. `CHAPTER 4`
   - Chapter ID: `chapter-02-chapter`
   - Chunks: `/Users/sachin/books/files/Made to Stick/chunks/chapter-02-chapter.jsonl`
   - Notes: `/Users/sachin/books/files/Made to Stick/notes/chapter-02-chapter.jsonl`
   - Summary: `/Users/sachin/books/files/Made to Stick/summaries/chapter-02-chapter.md`
   - Full: `/Users/sachin/books/files/Made to Stick/chapters/02 - CHAPTER 4.txt`
3. `CHAPTER 3`
   - Chapter ID: `chapter-03-chapter`
   - Chunks: `/Users/sachin/books/files/Made to Stick/chunks/chapter-03-chapter.jsonl`
   - Notes: `/Users/sachin/books/files/Made to Stick/notes/chapter-03-chapter.jsonl`
   - Summary: `/Users/sachin/books/files/Made to Stick/summaries/chapter-03-chapter.md`
   - Full: `/Users/sachin/books/files/Made to Stick/chapters/03 - CHAPTER 3.txt`
4. `CHAPTER 4`
   - Chapter ID: `chapter-04-chapter`
   - Chunks: `/Users/sachin/books/files/Made to Stick/chunks/chapter-04-chapter.jsonl`
   - Notes: `/Users/sachin/books/files/Made to Stick/notes/chapter-04-chapter.jsonl`
   - Summary: `/Users/sachin/books/files/Made to Stick/summaries/chapter-04-chapter.md`
   - Full: `/Users/sachin/books/files/Made to Stick/chapters/04 - CHAPTER 4.txt`
