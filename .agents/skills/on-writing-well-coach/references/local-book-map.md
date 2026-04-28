# Local Book Map

Use this file to ground the generated skill in the user's local preserved book artifacts.

## Root Paths

- Book root: `/Users/sachin/books/files/On Writing Well/`
- Book manifest: `/Users/sachin/books/files/On Writing Well/manifests/book.json`
- Chunk manifest: `/Users/sachin/books/files/On Writing Well/manifests/chunks.json`
- Source chunks: `/Users/sachin/books/files/On Writing Well/chunks/`
- Chunk-note skeletons or filled notes: `/Users/sachin/books/files/On Writing Well/notes/`
- Chunk extraction prompts: `/Users/sachin/books/files/On Writing Well/prompts/`
- Chapter summary prompts: `/Users/sachin/books/files/On Writing Well/prompts/summaries/`
- Search index: `/Users/sachin/books/files/On Writing Well/indexes/search.sqlite`
- Full chapter text fallback: `/Users/sachin/books/files/On Writing Well/chapters/`
- Legacy summaries fallback: `/Users/sachin/books/files/On Writing Well/summary/`
- Canonical summaries: `/Users/sachin/books/files/On Writing Well/summaries/`

## Retrieval Rule

Search the preservation index first:

```bash
python3 tools/book_pipeline.py search "/Users/sachin/books/files/On Writing Well" "query terms" --limit 8
```

Use retrieved chunks and filled notes as primary grounding. Use summaries as a fallback for higher-level synthesis.

## Preservation Status

- Current chapter count: 10
- Current chunk count: 87
- Notes may be skeletons unless explicitly filled after chunk extraction.
- Search indexes raw chunks and any non-empty filled notes.

## Chapter Map

1. `Cover`
   - Chapter ID: `chapter-01-cover`
   - Chunks: `/Users/sachin/books/files/On Writing Well/chunks/chapter-01-cover.jsonl`
   - Notes: `/Users/sachin/books/files/On Writing Well/notes/chapter-01-cover.jsonl`
   - Summary: `/Users/sachin/books/files/On Writing Well/summaries/chapter-01-cover.md`
   - Full: `/Users/sachin/books/files/On Writing Well/chapters/01 - Cover.txt`
2. `Copyright page`
   - Chapter ID: `chapter-02-copyright-page`
   - Chunks: `/Users/sachin/books/files/On Writing Well/chunks/chapter-02-copyright-page.jsonl`
   - Notes: `/Users/sachin/books/files/On Writing Well/notes/chapter-02-copyright-page.jsonl`
   - Summary: `/Users/sachin/books/files/On Writing Well/summaries/chapter-02-copyright-page.md`
   - Full: `/Users/sachin/books/files/On Writing Well/chapters/02 - Copyright page.txt`
3. `Contents`
   - Chapter ID: `chapter-03-contents`
   - Chunks: `/Users/sachin/books/files/On Writing Well/chunks/chapter-03-contents.jsonl`
   - Notes: `/Users/sachin/books/files/On Writing Well/notes/chapter-03-contents.jsonl`
   - Summary: `/Users/sachin/books/files/On Writing Well/summaries/chapter-03-contents.md`
   - Full: `/Users/sachin/books/files/On Writing Well/chapters/03 - Contents.txt`
4. `Introduction`
   - Chapter ID: `chapter-04-introduction`
   - Chunks: `/Users/sachin/books/files/On Writing Well/chunks/chapter-04-introduction.jsonl`
   - Notes: `/Users/sachin/books/files/On Writing Well/notes/chapter-04-introduction.jsonl`
   - Summary: `/Users/sachin/books/files/On Writing Well/summaries/chapter-04-introduction.md`
   - Full: `/Users/sachin/books/files/On Writing Well/chapters/04 - Introduction.txt`
5. `Part I – Principles`
   - Chapter ID: `chapter-05-part-i-principles`
   - Chunks: `/Users/sachin/books/files/On Writing Well/chunks/chapter-05-part-i-principles.jsonl`
   - Notes: `/Users/sachin/books/files/On Writing Well/notes/chapter-05-part-i-principles.jsonl`
   - Summary: `/Users/sachin/books/files/On Writing Well/summaries/chapter-05-part-i-principles.md`
   - Full: `/Users/sachin/books/files/On Writing Well/chapters/05 - Part I Principles.txt`
6. `Part II – Methods`
   - Chapter ID: `chapter-06-part-ii-methods`
   - Chunks: `/Users/sachin/books/files/On Writing Well/chunks/chapter-06-part-ii-methods.jsonl`
   - Notes: `/Users/sachin/books/files/On Writing Well/notes/chapter-06-part-ii-methods.jsonl`
   - Summary: `/Users/sachin/books/files/On Writing Well/summaries/chapter-06-part-ii-methods.md`
   - Full: `/Users/sachin/books/files/On Writing Well/chapters/06 - Part II Methods.txt`
7. `Part III – Forms`
   - Chapter ID: `chapter-07-part-iii-forms`
   - Chunks: `/Users/sachin/books/files/On Writing Well/chunks/chapter-07-part-iii-forms.jsonl`
   - Notes: `/Users/sachin/books/files/On Writing Well/notes/chapter-07-part-iii-forms.jsonl`
   - Summary: `/Users/sachin/books/files/On Writing Well/summaries/chapter-07-part-iii-forms.md`
   - Full: `/Users/sachin/books/files/On Writing Well/chapters/07 - Part III Forms.txt`
8. `Part IV – Attitudes`
   - Chapter ID: `chapter-08-part-iv-attitudes`
   - Chunks: `/Users/sachin/books/files/On Writing Well/chunks/chapter-08-part-iv-attitudes.jsonl`
   - Notes: `/Users/sachin/books/files/On Writing Well/notes/chapter-08-part-iv-attitudes.jsonl`
   - Summary: `/Users/sachin/books/files/On Writing Well/summaries/chapter-08-part-iv-attitudes.md`
   - Full: `/Users/sachin/books/files/On Writing Well/chapters/08 - Part IV Attitudes.txt`
9. `Sources`
   - Chapter ID: `chapter-09-sources`
   - Chunks: `/Users/sachin/books/files/On Writing Well/chunks/chapter-09-sources.jsonl`
   - Notes: `/Users/sachin/books/files/On Writing Well/notes/chapter-09-sources.jsonl`
   - Summary: `/Users/sachin/books/files/On Writing Well/summaries/chapter-09-sources.md`
   - Full: `/Users/sachin/books/files/On Writing Well/chapters/09 - Sources.txt`
10. `Index`
   - Chapter ID: `chapter-10-index`
   - Chunks: `/Users/sachin/books/files/On Writing Well/chunks/chapter-10-index.jsonl`
   - Notes: `/Users/sachin/books/files/On Writing Well/notes/chapter-10-index.jsonl`
   - Summary: `/Users/sachin/books/files/On Writing Well/summaries/chapter-10-index.md`
   - Full: `/Users/sachin/books/files/On Writing Well/chapters/10 - Index.txt`
