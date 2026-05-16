# Local Book Map

Use this file to ground the generated skill in the user's local preserved book artifacts.

## Root Paths

- Book root: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/`
- Book manifest: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/manifests/book.json`
- Chunk manifest: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/manifests/chunks.json`
- Source chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/`
- Chunk-note skeletons or filled notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/`
- Chunk extraction prompts: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/prompts/`
- Chapter summary prompts: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/prompts/summaries/`
- Search index: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/indexes/search.sqlite`
- Full chapter text fallback: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/`
- Legacy summaries fallback: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summary/`
- Canonical summaries: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/`

## Retrieval Rule

Search the preservation index first:

```bash
python3 tools/book_pipeline.py search "/Users/sachin/books/files/The Strategy and Tactics of Pricing" "query terms" --limit 8
```

Use retrieved chunks and filled notes as primary grounding. Use summaries as a fallback for higher-level synthesis.

## Preservation Status

- Current chapter count: 22
- Current chunk count: 164
- Notes may be skeletons unless explicitly filled after chunk extraction.
- Search indexes raw chunks and any non-empty filled notes.

## Chapter Map

1. `Cover`
   - Chapter ID: `chapter-01-cover`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-01-cover.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-01-cover.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-01-cover.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/01 - Cover.txt`
2. `Title`
   - Chapter ID: `chapter-02-title`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-02-title.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-02-title.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-02-title.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/02 - Title.txt`
3. `Copyright`
   - Chapter ID: `chapter-03-copyright`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-03-copyright.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-03-copyright.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-03-copyright.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/03 - Copyright.txt`
4. `Contents`
   - Chapter ID: `chapter-04-contents`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-04-contents.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-04-contents.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-04-contents.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/04 - Contents.txt`
5. `Detailed Table of Contents`
   - Chapter ID: `chapter-05-detailed-table-of-contents`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-05-detailed-table-of-contents.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-05-detailed-table-of-contents.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-05-detailed-table-of-contents.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/05 - Detailed Table of Contents.txt`
6. `Preface`
   - Chapter ID: `chapter-06-preface`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-06-preface.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-06-preface.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-06-preface.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/06 - Preface.txt`
7. `Acknowledgments`
   - Chapter ID: `chapter-07-acknowledgments`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-07-acknowledgments.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-07-acknowledgments.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-07-acknowledgments.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/07 - Acknowledgments.txt`
8. `List of In-Line Boxes`
   - Chapter ID: `chapter-08-list-of-in-line-boxes`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-08-list-of-in-line-boxes.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-08-list-of-in-line-boxes.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-08-list-of-in-line-boxes.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/08 - List of In-Line Boxes.txt`
9. `List of Exhibits`
   - Chapter ID: `chapter-09-list-of-exhibits`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-09-list-of-exhibits.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-09-list-of-exhibits.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-09-list-of-exhibits.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/09 - List of Exhibits.txt`
10. `Chapter 1 Strategic Pricing Coordinating the Drivers of Profitability`
   - Chapter ID: `chapter-10-strategic-pricing-coordinating-the-drivers-of-pr`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-10-strategic-pricing-coordinating-the-drivers-of-pr.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-10-strategic-pricing-coordinating-the-drivers-of-pr.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-10-strategic-pricing-coordinating-the-drivers-of-pr.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/10 - Chapter 1 Strategic Pricing Coordinating the Drivers of Profitability.txt`
11. `Chapter 2 Economic Value The Guiding Force of Pricing Strategy`
   - Chapter ID: `chapter-11-economic-value-the-guiding-force-of-pricing-stra`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-11-economic-value-the-guiding-force-of-pricing-stra.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-11-economic-value-the-guiding-force-of-pricing-stra.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-11-economic-value-the-guiding-force-of-pricing-stra.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/11 - Chapter 2 Economic Value The Guiding Force of Pricing Strategy.txt`
12. `Chapter 3 Price and Value Communication Strategies to Influence Willingness-to-Pay`
   - Chapter ID: `chapter-12-price-and-value-communication-strategies-to-infl`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-12-price-and-value-communication-strategies-to-infl.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-12-price-and-value-communication-strategies-to-infl.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-12-price-and-value-communication-strategies-to-infl.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/12 - Chapter 3 Price and Value Communication Strategies to Influence Willingness-to-Pay.txt`
13. `Chapter 4 Price Structure Tactics for Pricing Differently Across Customer Segment`
   - Chapter ID: `chapter-13-price-structure-tactics-for-pricing-differently`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-13-price-structure-tactics-for-pricing-differently.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-13-price-structure-tactics-for-pricing-differently.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-13-price-structure-tactics-for-pricing-differently.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/13 - Chapter 4 Price Structure Tactics for Pricing Differently Across Customer Segment.txt`
14. `Chapter 5 Pricing Policy Influencing Customer Expectations and Purchase Behaviors`
   - Chapter ID: `chapter-14-pricing-policy-influencing-customer-expectations`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-14-pricing-policy-influencing-customer-expectations.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-14-pricing-policy-influencing-customer-expectations.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-14-pricing-policy-influencing-customer-expectations.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/14 - Chapter 5 Pricing Policy Influencing Customer Expectations and Purchase Behaviors.txt`
15. `Chapter 6 Price Level Setting Prices that Capture a Share of the Value Created`
   - Chapter ID: `chapter-15-price-level-setting-prices-that-capture-a-share`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-15-price-level-setting-prices-that-capture-a-share.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-15-price-level-setting-prices-that-capture-a-share.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-15-price-level-setting-prices-that-capture-a-share.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/15 - Chapter 6 Price Level Setting Prices that Capture a Share of the Value Created.txt`
16. `Chapter 7 Price Competition Managing Conflict Thoughtfully`
   - Chapter ID: `chapter-16-price-competition-managing-conflict-thoughtfully`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-16-price-competition-managing-conflict-thoughtfully.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-16-price-competition-managing-conflict-thoughtfully.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-16-price-competition-managing-conflict-thoughtfully.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/16 - Chapter 7 Price Competition Managing Conflict Thoughtfully.txt`
17. `Chapter 8 Measurement of Price Sensitivity Research Techniques to Supplement Judgment`
   - Chapter ID: `chapter-17-measurement-of-price-sensitivity-research-techni`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-17-measurement-of-price-sensitivity-research-techni.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-17-measurement-of-price-sensitivity-research-techni.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-17-measurement-of-price-sensitivity-research-techni.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/17 - Chapter 8 Measurement of Price Sensitivity Research Techniques to Supplement Judgment.txt`
18. `Chapter 9 Financial Analysis Analyzing Costs and Profits for Pricing`
   - Chapter ID: `chapter-18-financial-analysis-analyzing-costs-and-profits-f`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-18-financial-analysis-analyzing-costs-and-profits-f.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-18-financial-analysis-analyzing-costs-and-profits-f.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-18-financial-analysis-analyzing-costs-and-profits-f.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/18 - Chapter 9 Financial Analysis Analyzing Costs and Profits for Pricing.txt`
19. `Chapter 10 Specialized Strategies Adapting Pricing to Accommodate Common Challenges`
   - Chapter ID: `chapter-19-specialized-strategies-adapting-pricing-to-accom`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-19-specialized-strategies-adapting-pricing-to-accom.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-19-specialized-strategies-adapting-pricing-to-accom.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-19-specialized-strategies-adapting-pricing-to-accom.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/19 - Chapter 10 Specialized Strategies Adapting Pricing to Accommodate Common Challenges.txt`
20. `Chapter 11 Creating Strategic Pricing Capability Assembling Talent, Processes, and Data to Build Competitive Advantage`
   - Chapter ID: `chapter-20-creating-strategic-pricing-capability-assembling`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-20-creating-strategic-pricing-capability-assembling.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-20-creating-strategic-pricing-capability-assembling.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-20-creating-strategic-pricing-capability-assembling.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/20 - Chapter 11 Creating Strategic Pricing Capability Assembling Talent Processes and Data to Build Competitive Advantage.txt`
21. `Chapter 12 Ethics and the Law Understanding the Constraints on Pricing`
   - Chapter ID: `chapter-21-ethics-and-the-law-understanding-the-constraints`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-21-ethics-and-the-law-understanding-the-constraints.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-21-ethics-and-the-law-understanding-the-constraints.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-21-ethics-and-the-law-understanding-the-constraints.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/21 - Chapter 12 Ethics and the Law Understanding the Constraints on Pricing.txt`
22. `Index`
   - Chapter ID: `chapter-22-index`
   - Chunks: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chunks/chapter-22-index.jsonl`
   - Notes: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/notes/chapter-22-index.jsonl`
   - Summary: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/summaries/chapter-22-index.md`
   - Full: `/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/22 - Index.txt`
