# Local Book Map

Use this file to ground the generated skill in the user's local preserved book artifacts.

## Root Paths

- Book root: `/Users/sachin/books/files/Building a StoryBrand 2.0/`
- Book manifest: `/Users/sachin/books/files/Building a StoryBrand 2.0/manifests/book.json`
- Chunk manifest: `/Users/sachin/books/files/Building a StoryBrand 2.0/manifests/chunks.json`
- Source chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/`
- Chunk-note skeletons or filled notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/`
- Chunk extraction prompts: `/Users/sachin/books/files/Building a StoryBrand 2.0/prompts/`
- Chapter summary prompts: `/Users/sachin/books/files/Building a StoryBrand 2.0/prompts/summaries/`
- Search index: `/Users/sachin/books/files/Building a StoryBrand 2.0/indexes/search.sqlite`
- Full chapter text fallback: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/`
- Legacy summaries fallback: `/Users/sachin/books/files/Building a StoryBrand 2.0/summary/`
- Canonical summaries: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/`

## Retrieval Rule

Search the preservation index first:

```bash
python3 tools/book_pipeline.py search "/Users/sachin/books/files/Building a StoryBrand 2.0" "query terms" --limit 8
```

Use retrieved chunks and filled notes as primary grounding. Use summaries as a fallback for higher-level synthesis.

## Preservation Status

- Current chapter count: 15
- Current chunk count: 66
- Notes may be skeletons unless explicitly filled after chunk extraction.
- Search indexes raw chunks and any non-empty filled notes.

## Chapter Map

1. `Title Page`
   - Chapter ID: `chapter-01-title-page`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-01-title-page.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-01-title-page.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-01-title-page.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/01 - Title Page.txt`
2. `Copyright`
   - Chapter ID: `chapter-02-copyright`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-02-copyright.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-02-copyright.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-02-copyright.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/02 - Copyright.txt`
3. `Contents`
   - Chapter ID: `chapter-03-contents`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-03-contents.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-03-contents.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-03-contents.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/03 - Contents.txt`
4. `Want Your Entire Team to Understand the StoryBrand Framework?`
   - Chapter ID: `chapter-04-want-your-entire-team-to-understand-the-storybra`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-04-want-your-entire-team-to-understand-the-storybra.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-04-want-your-entire-team-to-understand-the-storybra.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-04-want-your-entire-team-to-understand-the-storybra.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/04 - Want Your Entire Team to Understand the StoryBrand Framework.txt`
5. `Note from the Author on This Updated Edition`
   - Chapter ID: `chapter-05-note-from-the-author-on-this-updated-edition`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-05-note-from-the-author-on-this-updated-edition.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-05-note-from-the-author-on-this-updated-edition.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-05-note-from-the-author-on-this-updated-edition.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/05 - Note from the Author on This Updated Edition.txt`
6. `Introduction`
   - Chapter ID: `chapter-06-introduction`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-06-introduction.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-06-introduction.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-06-introduction.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/06 - Introduction.txt`
7. `Section 1: Why Most Marketing Is A Money Pit`
   - Chapter ID: `chapter-07-section-1-why-most-marketing-is-a-money-pit`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-07-section-1-why-most-marketing-is-a-money-pit.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-07-section-1-why-most-marketing-is-a-money-pit.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-07-section-1-why-most-marketing-is-a-money-pit.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/07 - Section 1 Why Most Marketing Is A Money Pit.txt`
8. `Section 2: Building Your StoryBrand`
   - Chapter ID: `chapter-08-section-2-building-your-storybrand`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-08-section-2-building-your-storybrand.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-08-section-2-building-your-storybrand.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-08-section-2-building-your-storybrand.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/08 - Section 2 Building Your StoryBrand.txt`
9. `Section 3: Executing Your StoryBrand Messaging and Marketing Campaign`
   - Chapter ID: `chapter-09-section-3-executing-your-storybrand-messaging-an`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-09-section-3-executing-your-storybrand-messaging-an.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-09-section-3-executing-your-storybrand-messaging-an.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-09-section-3-executing-your-storybrand-messaging-an.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/09 - Section 3 Executing Your StoryBrand Messaging and Marketing Campaign.txt`
10. `Afterword`
   - Chapter ID: `chapter-10-afterword`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-10-afterword.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-10-afterword.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-10-afterword.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/10 - Afterword.txt`
11. `Acknowledgments`
   - Chapter ID: `chapter-11-acknowledgments`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-11-acknowledgments.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-11-acknowledgments.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-11-acknowledgments.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/11 - Acknowledgments.txt`
12. `About the Author`
   - Chapter ID: `chapter-12-about-the-author`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-12-about-the-author.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-12-about-the-author.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-12-about-the-author.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/12 - About the Author.txt`
13. `Praise for the StoryBrand Framework`
   - Chapter ID: `chapter-13-praise-for-the-storybrand-framework`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-13-praise-for-the-storybrand-framework.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-13-praise-for-the-storybrand-framework.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-13-praise-for-the-storybrand-framework.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/13 - Praise for the StoryBrand Framework.txt`
14. `StoryBrand Resources`
   - Chapter ID: `chapter-14-storybrand-resources`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-14-storybrand-resources.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-14-storybrand-resources.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-14-storybrand-resources.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/14 - StoryBrand Resources.txt`
15. `Notes`
   - Chapter ID: `chapter-15-notes`
   - Chunks: `/Users/sachin/books/files/Building a StoryBrand 2.0/chunks/chapter-15-notes.jsonl`
   - Notes: `/Users/sachin/books/files/Building a StoryBrand 2.0/notes/chapter-15-notes.jsonl`
   - Summary: `/Users/sachin/books/files/Building a StoryBrand 2.0/summaries/chapter-15-notes.md`
   - Full: `/Users/sachin/books/files/Building a StoryBrand 2.0/chapters/15 - Notes.txt`
