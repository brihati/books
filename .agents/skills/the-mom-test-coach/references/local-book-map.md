# Local Book Map

Use this file to ground the generated skill in the user's local preserved book artifacts.

## Root Paths

- Book root: `/Users/sachin/books/files/The Mom Test/`
- Book manifest: `/Users/sachin/books/files/The Mom Test/manifests/book.json`
- Chunk manifest: `/Users/sachin/books/files/The Mom Test/manifests/chunks.json`
- Source chunks: `/Users/sachin/books/files/The Mom Test/chunks/`
- Chunk-note skeletons or filled notes: `/Users/sachin/books/files/The Mom Test/notes/`
- Chunk extraction prompts: `/Users/sachin/books/files/The Mom Test/prompts/`
- Chapter summary prompts: `/Users/sachin/books/files/The Mom Test/prompts/summaries/`
- Search index: `/Users/sachin/books/files/The Mom Test/indexes/search.sqlite`
- Full chapter text fallback: `/Users/sachin/books/files/The Mom Test/chapters/`
- Legacy summaries fallback: `/Users/sachin/books/files/The Mom Test/summary/`
- Canonical summaries: `/Users/sachin/books/files/The Mom Test/summaries/`

## Retrieval Rule

Search the preservation index first:

```bash
python3 tools/book_pipeline.py search "/Users/sachin/books/files/The Mom Test" "query terms" --limit 8
```

Use retrieved chunks and filled notes as primary grounding. Use summaries as a fallback for higher-level synthesis.

## Preservation Status

- Current chapter count: 11
- Current chunk count: 33
- Notes may be skeletons unless explicitly filled after chunk extraction.
- Search indexes raw chunks and any non-empty filled notes.

## Chapter Map

1. `Contents`
   - Chapter ID: `chapter-01-contents`
   - Chunks: `/Users/sachin/books/files/The Mom Test/chunks/chapter-01-contents.jsonl`
   - Notes: `/Users/sachin/books/files/The Mom Test/notes/chapter-01-contents.jsonl`
   - Summary: `/Users/sachin/books/files/The Mom Test/summaries/chapter-01-contents.md`
   - Full: `/Users/sachin/books/files/The Mom Test/chapters/01 - Contents.txt`
2. `Introduction`
   - Chapter ID: `chapter-02-introduction`
   - Chunks: `/Users/sachin/books/files/The Mom Test/chunks/chapter-02-introduction.jsonl`
   - Notes: `/Users/sachin/books/files/The Mom Test/notes/chapter-02-introduction.jsonl`
   - Summary: `/Users/sachin/books/files/The Mom Test/summaries/chapter-02-introduction.md`
   - Full: `/Users/sachin/books/files/The Mom Test/chapters/02 - Introduction.txt`
3. `The Mom Test`
   - Chapter ID: `chapter-03-the-mom-test`
   - Chunks: `/Users/sachin/books/files/The Mom Test/chunks/chapter-03-the-mom-test.jsonl`
   - Notes: `/Users/sachin/books/files/The Mom Test/notes/chapter-03-the-mom-test.jsonl`
   - Summary: `/Users/sachin/books/files/The Mom Test/summaries/chapter-03-the-mom-test.md`
   - Full: `/Users/sachin/books/files/The Mom Test/chapters/03 - The Mom Test.txt`
4. `Avoiding bad data`
   - Chapter ID: `chapter-04-avoiding-bad-data`
   - Chunks: `/Users/sachin/books/files/The Mom Test/chunks/chapter-04-avoiding-bad-data.jsonl`
   - Notes: `/Users/sachin/books/files/The Mom Test/notes/chapter-04-avoiding-bad-data.jsonl`
   - Summary: `/Users/sachin/books/files/The Mom Test/summaries/chapter-04-avoiding-bad-data.md`
   - Full: `/Users/sachin/books/files/The Mom Test/chapters/04 - Avoiding bad data.txt`
5. `Asking important questions`
   - Chapter ID: `chapter-05-asking-important-questions`
   - Chunks: `/Users/sachin/books/files/The Mom Test/chunks/chapter-05-asking-important-questions.jsonl`
   - Notes: `/Users/sachin/books/files/The Mom Test/notes/chapter-05-asking-important-questions.jsonl`
   - Summary: `/Users/sachin/books/files/The Mom Test/summaries/chapter-05-asking-important-questions.md`
   - Full: `/Users/sachin/books/files/The Mom Test/chapters/05 - Asking important questions.txt`
6. `Keeping it casual`
   - Chapter ID: `chapter-06-keeping-it-casual`
   - Chunks: `/Users/sachin/books/files/The Mom Test/chunks/chapter-06-keeping-it-casual.jsonl`
   - Notes: `/Users/sachin/books/files/The Mom Test/notes/chapter-06-keeping-it-casual.jsonl`
   - Summary: `/Users/sachin/books/files/The Mom Test/summaries/chapter-06-keeping-it-casual.md`
   - Full: `/Users/sachin/books/files/The Mom Test/chapters/06 - Keeping it casual.txt`
7. `Commitment and advancement`
   - Chapter ID: `chapter-07-commitment-and-advancement`
   - Chunks: `/Users/sachin/books/files/The Mom Test/chunks/chapter-07-commitment-and-advancement.jsonl`
   - Notes: `/Users/sachin/books/files/The Mom Test/notes/chapter-07-commitment-and-advancement.jsonl`
   - Summary: `/Users/sachin/books/files/The Mom Test/summaries/chapter-07-commitment-and-advancement.md`
   - Full: `/Users/sachin/books/files/The Mom Test/chapters/07 - Commitment and advancement.txt`
8. `Finding conversations`
   - Chapter ID: `chapter-08-finding-conversations`
   - Chunks: `/Users/sachin/books/files/The Mom Test/chunks/chapter-08-finding-conversations.jsonl`
   - Notes: `/Users/sachin/books/files/The Mom Test/notes/chapter-08-finding-conversations.jsonl`
   - Summary: `/Users/sachin/books/files/The Mom Test/summaries/chapter-08-finding-conversations.md`
   - Full: `/Users/sachin/books/files/The Mom Test/chapters/08 - Finding conversations.txt`
9. `Choosing your customers`
   - Chapter ID: `chapter-09-choosing-your-customers`
   - Chunks: `/Users/sachin/books/files/The Mom Test/chunks/chapter-09-choosing-your-customers.jsonl`
   - Notes: `/Users/sachin/books/files/The Mom Test/notes/chapter-09-choosing-your-customers.jsonl`
   - Summary: `/Users/sachin/books/files/The Mom Test/summaries/chapter-09-choosing-your-customers.md`
   - Full: `/Users/sachin/books/files/The Mom Test/chapters/09 - Choosing your customers.txt`
10. `Running the process`
   - Chapter ID: `chapter-10-running-the-process`
   - Chunks: `/Users/sachin/books/files/The Mom Test/chunks/chapter-10-running-the-process.jsonl`
   - Notes: `/Users/sachin/books/files/The Mom Test/notes/chapter-10-running-the-process.jsonl`
   - Summary: `/Users/sachin/books/files/The Mom Test/summaries/chapter-10-running-the-process.md`
   - Full: `/Users/sachin/books/files/The Mom Test/chapters/10 - Running the process.txt`
11. `Conclusion and cheatsheet`
   - Chapter ID: `chapter-11-conclusion-and-cheatsheet`
   - Chunks: `/Users/sachin/books/files/The Mom Test/chunks/chapter-11-conclusion-and-cheatsheet.jsonl`
   - Notes: `/Users/sachin/books/files/The Mom Test/notes/chapter-11-conclusion-and-cheatsheet.jsonl`
   - Summary: `/Users/sachin/books/files/The Mom Test/summaries/chapter-11-conclusion-and-cheatsheet.md`
   - Full: `/Users/sachin/books/files/The Mom Test/chapters/11 - Conclusion and cheatsheet.txt`
