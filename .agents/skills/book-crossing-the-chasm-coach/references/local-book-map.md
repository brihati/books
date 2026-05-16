# Local Book Map

Use this file to ground the generated skill in the user's local preserved book artifacts.

## Root Paths

- Book root: `/Users/sachin/books/files/Crossing the Chasm/`
- Book manifest: `/Users/sachin/books/files/Crossing the Chasm/manifests/book.json`
- Chunk manifest: `/Users/sachin/books/files/Crossing the Chasm/manifests/chunks.json`
- Source chunks: `/Users/sachin/books/files/Crossing the Chasm/chunks/`
- Chunk-note skeletons or filled notes: `/Users/sachin/books/files/Crossing the Chasm/notes/`
- Chunk extraction prompts: `/Users/sachin/books/files/Crossing the Chasm/prompts/`
- Chapter summary prompts: `/Users/sachin/books/files/Crossing the Chasm/prompts/summaries/`
- Search index: `/Users/sachin/books/files/Crossing the Chasm/indexes/search.sqlite`
- Full chapter text fallback: `/Users/sachin/books/files/Crossing the Chasm/chapters/`
- Legacy summaries fallback: `/Users/sachin/books/files/Crossing the Chasm/summary/`
- Canonical summaries: `/Users/sachin/books/files/Crossing the Chasm/summaries/`

## Retrieval Rule

Search the preservation index first:

```bash
python3 tools/book_pipeline.py search "/Users/sachin/books/files/Crossing the Chasm" "query terms" --limit 8
```

Use retrieved chunks and filled notes as primary grounding. Use summaries as a fallback for higher-level synthesis.

## Preservation Status

- Current chapter count: 9
- Current chunk count: 64
- Notes may be skeletons unless explicitly filled after chunk extraction.
- Search indexes raw chunks and any non-empty filled notes.

## Chapter Map

1. `Introduction`
   - Chapter ID: `chapter-01-introduction`
   - Chunks: `/Users/sachin/books/files/Crossing the Chasm/chunks/chapter-01-introduction.jsonl`
   - Notes: `/Users/sachin/books/files/Crossing the Chasm/notes/chapter-01-introduction.jsonl`
   - Summary: `/Users/sachin/books/files/Crossing the Chasm/summaries/chapter-01-introduction.md`
   - Full: `/Users/sachin/books/files/Crossing the Chasm/chapters/01 - Introduction.txt`
2. `High-Tech Marketing Illusion`
   - Chapter ID: `chapter-02-high-tech-marketing-illusion`
   - Chunks: `/Users/sachin/books/files/Crossing the Chasm/chunks/chapter-02-high-tech-marketing-illusion.jsonl`
   - Notes: `/Users/sachin/books/files/Crossing the Chasm/notes/chapter-02-high-tech-marketing-illusion.jsonl`
   - Summary: `/Users/sachin/books/files/Crossing the Chasm/summaries/chapter-02-high-tech-marketing-illusion.md`
   - Full: `/Users/sachin/books/files/Crossing the Chasm/chapters/02 - High-Tech Marketing Illusion.txt`
3. `The D-Day Analogy`
   - Chapter ID: `chapter-03-the-d-day-analogy`
   - Chunks: `/Users/sachin/books/files/Crossing the Chasm/chunks/chapter-03-the-d-day-analogy.jsonl`
   - Notes: `/Users/sachin/books/files/Crossing the Chasm/notes/chapter-03-the-d-day-analogy.jsonl`
   - Summary: `/Users/sachin/books/files/Crossing the Chasm/summaries/chapter-03-the-d-day-analogy.md`
   - Full: `/Users/sachin/books/files/Crossing the Chasm/chapters/03 - The D-Day Analogy.txt`
4. `Target the Point of Attack`
   - Chapter ID: `chapter-04-target-the-point-of-attack`
   - Chunks: `/Users/sachin/books/files/Crossing the Chasm/chunks/chapter-04-target-the-point-of-attack.jsonl`
   - Notes: `/Users/sachin/books/files/Crossing the Chasm/notes/chapter-04-target-the-point-of-attack.jsonl`
   - Summary: `/Users/sachin/books/files/Crossing the Chasm/summaries/chapter-04-target-the-point-of-attack.md`
   - Full: `/Users/sachin/books/files/Crossing the Chasm/chapters/04 - Target the Point of Attack.txt`
5. `Assemble the Invasion Force`
   - Chapter ID: `chapter-05-assemble-the-invasion-force`
   - Chunks: `/Users/sachin/books/files/Crossing the Chasm/chunks/chapter-05-assemble-the-invasion-force.jsonl`
   - Notes: `/Users/sachin/books/files/Crossing the Chasm/notes/chapter-05-assemble-the-invasion-force.jsonl`
   - Summary: `/Users/sachin/books/files/Crossing the Chasm/summaries/chapter-05-assemble-the-invasion-force.md`
   - Full: `/Users/sachin/books/files/Crossing the Chasm/chapters/05 - Assemble the Invasion Force.txt`
6. `Define the Battle`
   - Chapter ID: `chapter-06-define-the-battle`
   - Chunks: `/Users/sachin/books/files/Crossing the Chasm/chunks/chapter-06-define-the-battle.jsonl`
   - Notes: `/Users/sachin/books/files/Crossing the Chasm/notes/chapter-06-define-the-battle.jsonl`
   - Summary: `/Users/sachin/books/files/Crossing the Chasm/summaries/chapter-06-define-the-battle.md`
   - Full: `/Users/sachin/books/files/Crossing the Chasm/chapters/06 - Define the Battle.txt`
7. `Launch the Invasion`
   - Chapter ID: `chapter-07-launch-the-invasion`
   - Chunks: `/Users/sachin/books/files/Crossing the Chasm/chunks/chapter-07-launch-the-invasion.jsonl`
   - Notes: `/Users/sachin/books/files/Crossing the Chasm/notes/chapter-07-launch-the-invasion.jsonl`
   - Summary: `/Users/sachin/books/files/Crossing the Chasm/summaries/chapter-07-launch-the-invasion.md`
   - Full: `/Users/sachin/books/files/Crossing the Chasm/chapters/07 - Launch the Invasion.txt`
8. `Leaving the Chasm Behind`
   - Chapter ID: `chapter-08-leaving-the-chasm-behind`
   - Chunks: `/Users/sachin/books/files/Crossing the Chasm/chunks/chapter-08-leaving-the-chasm-behind.jsonl`
   - Notes: `/Users/sachin/books/files/Crossing the Chasm/notes/chapter-08-leaving-the-chasm-behind.jsonl`
   - Summary: `/Users/sachin/books/files/Crossing the Chasm/summaries/chapter-08-leaving-the-chasm-behind.md`
   - Full: `/Users/sachin/books/files/Crossing the Chasm/chapters/08 - Leaving the Chasm Behind.txt`
9. `Appendix 1`
   - Chapter ID: `chapter-09-appendix-1`
   - Chunks: `/Users/sachin/books/files/Crossing the Chasm/chunks/chapter-09-appendix-1.jsonl`
   - Notes: `/Users/sachin/books/files/Crossing the Chasm/notes/chapter-09-appendix-1.jsonl`
   - Summary: `/Users/sachin/books/files/Crossing the Chasm/summaries/chapter-09-appendix-1.md`
   - Full: `/Users/sachin/books/files/Crossing the Chasm/chapters/09 - Appendix 1.txt`
