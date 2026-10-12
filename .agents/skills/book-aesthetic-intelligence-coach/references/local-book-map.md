# Local Book Map

Use this file to ground the generated skill in the user's local preserved book artifacts.

## Root Paths

- Book root: `/Users/sachin/books/files/Aesthetic Intelligence/`
- Book manifest: `/Users/sachin/books/files/Aesthetic Intelligence/manifests/book.json`
- Chunk manifest: `/Users/sachin/books/files/Aesthetic Intelligence/manifests/chunks.json`
- Source chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/`
- Chunk-note skeletons or filled notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/`
- Chunk extraction prompts: `/Users/sachin/books/files/Aesthetic Intelligence/prompts/`
- Chapter summary prompts: `/Users/sachin/books/files/Aesthetic Intelligence/prompts/summaries/`
- Search index: `/Users/sachin/books/files/Aesthetic Intelligence/indexes/search.sqlite`
- Full chapter text fallback: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/`
- Legacy summaries fallback: `/Users/sachin/books/files/Aesthetic Intelligence/summary/`
- Canonical summaries: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/`

## Retrieval Rule

Search the preservation index first:

```bash
python3 tools/book_pipeline.py search "/Users/sachin/books/files/Aesthetic Intelligence" "query terms" --limit 8
```

Use retrieved chunks and filled notes as primary grounding. Use summaries as a fallback for higher-level synthesis.

## Preservation Status

- Current chapter count: 15
- Current chunk count: 73
- Filled note count: 73
- Untouched note count: 0
- Canonical summary count: 15
- Search indexes raw chunks, filled notes, and available summaries.

## Outline Note

The PDF outline exposes the teaching chapters at two levels. This preserved workspace keeps the top-level outline so the introduction, conclusion, notes, index, and other back matter remain accessible. The main teaching material is grouped as:

- `chapter-06-part-i-mastering-the-other-ai`: Part I, including book chapters 1-4.
- `chapter-07-part-ii-boost-your-aq`: Part II, including book chapters 5-8.
- `chapter-08-part-iii-the-aesthetic-future`: Part III, including book chapter 9.

## Chapter Map

1. `Cover`
   - Chapter ID: `chapter-01-cover`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-01-cover.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-01-cover.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-01-cover.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/01 - Cover.txt`
2. `Title Page`
   - Chapter ID: `chapter-02-title-page`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-02-title-page.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-02-title-page.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-02-title-page.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/02 - Title Page.txt`
3. `Dedication`
   - Chapter ID: `chapter-03-dedication`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-03-dedication.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-03-dedication.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-03-dedication.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/03 - Dedication.txt`
4. `Contents`
   - Chapter ID: `chapter-04-contents`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-04-contents.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-04-contents.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-04-contents.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/04 - Contents.txt`
5. `Introduction: Aesthetics Matter`
   - Chapter ID: `chapter-05-introduction-aesthetics-matter`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-05-introduction-aesthetics-matter.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-05-introduction-aesthetics-matter.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-05-introduction-aesthetics-matter.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/05 - Introduction Aesthetics Matter.txt`
6. `Part I: Mastering the Other AI`
   - Chapter ID: `chapter-06-part-i-mastering-the-other-ai`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-06-part-i-mastering-the-other-ai.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-06-part-i-mastering-the-other-ai.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-06-part-i-mastering-the-other-ai.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/06 - Part I Mastering the Other AI.txt`
7. `Part II: Boost Your AQ`
   - Chapter ID: `chapter-07-part-ii-boost-your-aq`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-07-part-ii-boost-your-aq.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-07-part-ii-boost-your-aq.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-07-part-ii-boost-your-aq.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/07 - Part II Boost Your AQ.txt`
8. `Part III: The Aesthetic Future`
   - Chapter ID: `chapter-08-part-iii-the-aesthetic-future`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-08-part-iii-the-aesthetic-future.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-08-part-iii-the-aesthetic-future.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-08-part-iii-the-aesthetic-future.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/08 - Part III The Aesthetic Future.txt`
9. `Conclusion`
   - Chapter ID: `chapter-09-conclusion`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-09-conclusion.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-09-conclusion.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-09-conclusion.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/09 - Conclusion.txt`
10. `Acknowledgments`
   - Chapter ID: `chapter-10-acknowledgments`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-10-acknowledgments.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-10-acknowledgments.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-10-acknowledgments.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/10 - Acknowledgments.txt`
11. `Notes`
   - Chapter ID: `chapter-11-notes`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-11-notes.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-11-notes.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-11-notes.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/11 - Notes.txt`
12. `Index`
   - Chapter ID: `chapter-12-index`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-12-index.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-12-index.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-12-index.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/12 - Index.txt`
13. `About the Author`
   - Chapter ID: `chapter-13-about-the-author`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-13-about-the-author.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-13-about-the-author.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-13-about-the-author.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/13 - About the Author.txt`
14. `Copyright`
   - Chapter ID: `chapter-14-copyright`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-14-copyright.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-14-copyright.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-14-copyright.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/14 - Copyright.txt`
15. `About the Publisher`
   - Chapter ID: `chapter-15-about-the-publisher`
   - Chunks: `/Users/sachin/books/files/Aesthetic Intelligence/chunks/chapter-15-about-the-publisher.jsonl`
   - Notes: `/Users/sachin/books/files/Aesthetic Intelligence/notes/chapter-15-about-the-publisher.jsonl`
   - Summary: `/Users/sachin/books/files/Aesthetic Intelligence/summaries/chapter-15-about-the-publisher.md`
   - Full: `/Users/sachin/books/files/Aesthetic Intelligence/chapters/15 - About the Publisher.txt`
