# Local Book Map

Use this file to ground the generated skill in the user's local preserved book artifacts.

## Root Paths

- Book root: `/Users/sachin/books/files/Price to Scale/`
- Book manifest: `/Users/sachin/books/files/Price to Scale/manifests/book.json`
- Chunk manifest: `/Users/sachin/books/files/Price to Scale/manifests/chunks.json`
- Source chunks: `/Users/sachin/books/files/Price to Scale/chunks/`
- Chunk-note skeletons or filled notes: `/Users/sachin/books/files/Price to Scale/notes/`
- Chunk extraction prompts: `/Users/sachin/books/files/Price to Scale/prompts/`
- Chapter summary prompts: `/Users/sachin/books/files/Price to Scale/prompts/summaries/`
- Search index: `/Users/sachin/books/files/Price to Scale/indexes/search.sqlite`
- Full chapter text fallback: `/Users/sachin/books/files/Price to Scale/chapters/`
- Legacy summaries fallback: `/Users/sachin/books/files/Price to Scale/summary/`
- Canonical summaries: `/Users/sachin/books/files/Price to Scale/summaries/`

## Retrieval Rule

Search the preservation index first:

```bash
python3 tools/book_pipeline.py search "/Users/sachin/books/files/Price to Scale" "query terms" --limit 8
```

Use retrieved chunks and filled notes as primary grounding. Use summaries as a fallback for higher-level synthesis.

## Preservation Status

- Current chapter count: 16
- Current chunk count: 87
- Notes may be skeletons unless explicitly filled after chunk extraction.
- Search indexes raw chunks and any non-empty filled notes.

## Chapter Map

1. `contents`
   - Chapter ID: `chapter-01-contents`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-01-contents.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-01-contents.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-01-contents.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/01 - contents.txt`
2. `Preface`
   - Chapter ID: `chapter-02-preface`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-02-preface.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-02-preface.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-02-preface.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/02 - Preface.txt`
3. `The 5-Step Pricing Transformation Framework`
   - Chapter ID: `chapter-03-the-5-step-pricing-transformation-framework`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-03-the-5-step-pricing-transformation-framework.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-03-the-5-step-pricing-transformation-framework.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-03-the-5-step-pricing-transformation-framework.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/03 - The 5-Step Pricing Transformation Framework.txt`
4. `Step 1`
   - Chapter ID: `chapter-04-step-1`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-04-step-1.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-04-step-1.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-04-step-1.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/04 - Step 1.txt`
5. `Step 2`
   - Chapter ID: `chapter-05-step-2`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-05-step-2.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-05-step-2.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-05-step-2.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/05 - Step 2.txt`
6. `Step 3`
   - Chapter ID: `chapter-06-step-3`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-06-step-3.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-06-step-3.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-06-step-3.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/06 - Step 3.txt`
7. `Step 4`
   - Chapter ID: `chapter-07-step-4`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-07-step-4.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-07-step-4.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-07-step-4.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/07 - Step 4.txt`
8. `Step 5a`
   - Chapter ID: `chapter-08-step-5a`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-08-step-5a.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-08-step-5a.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-08-step-5a.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/08 - Step 5a.txt`
9. `Step 5b`
   - Chapter ID: `chapter-09-step-5b`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-09-step-5b.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-09-step-5b.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-09-step-5b.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/09 - Step 5b.txt`
10. `Step 5c`
   - Chapter ID: `chapter-10-step-5c`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-10-step-5c.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-10-step-5c.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-10-step-5c.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/10 - Step 5c.txt`
11. `Pricing Example`
   - Chapter ID: `chapter-11-pricing-example`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-11-pricing-example.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-11-pricing-example.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-11-pricing-example.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/11 - Pricing Example.txt`
12. `Usage Based Pricing`
   - Chapter ID: `chapter-12-usage-based-pricing`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-12-usage-based-pricing.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-12-usage-based-pricing.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-12-usage-based-pricing.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/12 - Usage Based Pricing.txt`
13. `How To Optimize Your Pricing in the Face of Churn & Inflation in SaaS`
   - Chapter ID: `chapter-13-how-to-optimize-your-pricing-in-the-face-of-chur`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-13-how-to-optimize-your-pricing-in-the-face-of-chur.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-13-how-to-optimize-your-pricing-in-the-face-of-chur.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-13-how-to-optimize-your-pricing-in-the-face-of-chur.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/13 - How To Optimize Your Pricing in the Face of Churn Inflation in SaaS.txt`
14. `Economics & Pricing of GenAI Development`
   - Chapter ID: `chapter-14-economics-pricing-of-genai-development`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-14-economics-pricing-of-genai-development.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-14-economics-pricing-of-genai-development.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-14-economics-pricing-of-genai-development.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/14 - Economics Pricing of GenAI Development.txt`
15. `Don’t Miss This`
   - Chapter ID: `chapter-15-don-t-miss-this`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-15-don-t-miss-this.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-15-don-t-miss-this.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-15-don-t-miss-this.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/15 - Dont Miss This.txt`
16. `Interviews & Case Studies With Top Pricing Leaders`
   - Chapter ID: `chapter-16-interviews-case-studies-with-top-pricing-leaders`
   - Chunks: `/Users/sachin/books/files/Price to Scale/chunks/chapter-16-interviews-case-studies-with-top-pricing-leaders.jsonl`
   - Notes: `/Users/sachin/books/files/Price to Scale/notes/chapter-16-interviews-case-studies-with-top-pricing-leaders.jsonl`
   - Summary: `/Users/sachin/books/files/Price to Scale/summaries/chapter-16-interviews-case-studies-with-top-pricing-leaders.md`
   - Full: `/Users/sachin/books/files/Price to Scale/chapters/16 - Interviews Case Studies With Top Pricing Leaders.txt`
