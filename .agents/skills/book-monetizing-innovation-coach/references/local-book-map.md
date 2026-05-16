# Local Book Map

Use this file to ground the generated skill in the user's local preserved book artifacts.

## Root Paths

- Book root: `/Users/sachin/books/files/Monetizing Innovation/`
- Book manifest: `/Users/sachin/books/files/Monetizing Innovation/manifests/book.json`
- Chunk manifest: `/Users/sachin/books/files/Monetizing Innovation/manifests/chunks.json`
- Source chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/`
- Chunk-note skeletons or filled notes: `/Users/sachin/books/files/Monetizing Innovation/notes/`
- Chunk extraction prompts: `/Users/sachin/books/files/Monetizing Innovation/prompts/`
- Chapter summary prompts: `/Users/sachin/books/files/Monetizing Innovation/prompts/summaries/`
- Search index: `/Users/sachin/books/files/Monetizing Innovation/indexes/search.sqlite`
- Full chapter text fallback: `/Users/sachin/books/files/Monetizing Innovation/chapters/`
- Legacy summaries fallback: `/Users/sachin/books/files/Monetizing Innovation/summary/`
- Canonical summaries: `/Users/sachin/books/files/Monetizing Innovation/summaries/`

## Retrieval Rule

Search the preservation index first:

```bash
python3 tools/book_pipeline.py search "/Users/sachin/books/files/Monetizing Innovation" "query terms" --limit 8
```

Use retrieved chunks and filled notes as primary grounding. Use summaries as a fallback for higher-level synthesis.

## Preservation Status

- Current chapter count: 14
- Current chunk count: 67
- Notes may be skeletons unless explicitly filled after chunk extraction.
- Search indexes raw chunks and any non-empty filled notes.

## Chapter Map

1. `CHAPTER 1: How Innovators Leave Billions on the Table`
   - Chapter ID: `chapter-01-how-innovators-leave-billions-on-the-table`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-01-how-innovators-leave-billions-on-the-table.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-01-how-innovators-leave-billions-on-the-table.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-01-how-innovators-leave-billions-on-the-table.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/01 - CHAPTER 1 How Innovators Leave Billions on the Table.txt`
2. `CHAPTER 2: Feature Shocks, Minivations, Hidden Gems, and Undeads`
   - Chapter ID: `chapter-02-feature-shocks-minivations-hidden-gems-and-undea`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-02-feature-shocks-minivations-hidden-gems-and-undea.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-02-feature-shocks-minivations-hidden-gems-and-undea.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-02-feature-shocks-minivations-hidden-gems-and-undea.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/02 - CHAPTER 2 Feature Shocks Minivations Hidden Gems and Undeads.txt`
3. `CHAPTER 3: Why Good People Get It Wrong`
   - Chapter ID: `chapter-03-why-good-people-get-it-wrong`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-03-why-good-people-get-it-wrong.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-03-why-good-people-get-it-wrong.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-03-why-good-people-get-it-wrong.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/03 - CHAPTER 3 Why Good People Get It Wrong.txt`
4. `CHAPTER 4: Have the “Willingness-to-Pay” Talk Early`
   - Chapter ID: `chapter-04-have-the-willingness-to-pay-talk-early`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-04-have-the-willingness-to-pay-talk-early.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-04-have-the-willingness-to-pay-talk-early.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-04-have-the-willingness-to-pay-talk-early.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/04 - CHAPTER 4 Have the Willingness-to-Pay Talk Early.txt`
5. `CHAPTER 5: Don’t Default to a One-Size-Fits-All Solution`
   - Chapter ID: `chapter-05-don-t-default-to-a-one-size-fits-all-solution`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-05-don-t-default-to-a-one-size-fits-all-solution.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-05-don-t-default-to-a-one-size-fits-all-solution.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-05-don-t-default-to-a-one-size-fits-all-solution.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/05 - CHAPTER 5 Dont Default to a One-Size-Fits-All Solution.txt`
6. `CHAPTER 6: When Designing Products, Configuration and Bundling is More Science Than Art`
   - Chapter ID: `chapter-06-when-designing-products-configuration-and-bundli`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-06-when-designing-products-configuration-and-bundli.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-06-when-designing-products-configuration-and-bundli.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-06-when-designing-products-configuration-and-bundli.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/06 - CHAPTER 6 When Designing Products Configuration and Bundling is More Science Than Art.txt`
7. `CHAPTER 7: Go beyond the Price Point`
   - Chapter ID: `chapter-07-go-beyond-the-price-point`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-07-go-beyond-the-price-point.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-07-go-beyond-the-price-point.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-07-go-beyond-the-price-point.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/07 - CHAPTER 7 Go beyond the Price Point.txt`
8. `CHAPTER 8: Price Low for Market Share or High for Premium Branding?`
   - Chapter ID: `chapter-08-price-low-for-market-share-or-high-for-premium-b`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-08-price-low-for-market-share-or-high-for-premium-b.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-08-price-low-for-market-share-or-high-for-premium-b.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-08-price-low-for-market-share-or-high-for-premium-b.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/08 - CHAPTER 8 Price Low for Market Share or High for Premium Branding.txt`
9. `CHAPTER 9: From Hoping to Knowing`
   - Chapter ID: `chapter-09-from-hoping-to-knowing`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-09-from-hoping-to-knowing.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-09-from-hoping-to-knowing.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-09-from-hoping-to-knowing.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/09 - CHAPTER 9 From Hoping to Knowing.txt`
10. `CHAPTER 10: The Innovation Won’t Speak for Itself`
   - Chapter ID: `chapter-10-the-innovation-won-t-speak-for-itself`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-10-the-innovation-won-t-speak-for-itself.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-10-the-innovation-won-t-speak-for-itself.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-10-the-innovation-won-t-speak-for-itself.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/10 - CHAPTER 10 The Innovation Wont Speak for Itself.txt`
11. `CHAPTER 11: Use Behavioral Pricing Tactics to Persuadeand Sell`
   - Chapter ID: `chapter-11-use-behavioral-pricing-tactics-to-persuadeand-se`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-11-use-behavioral-pricing-tactics-to-persuadeand-se.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-11-use-behavioral-pricing-tactics-to-persuadeand-se.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-11-use-behavioral-pricing-tactics-to-persuadeand-se.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/11 - CHAPTER 11 Use Behavioral Pricing Tactics to Persuadeand Sell.txt`
12. `CHAPTER 12 Maintain Your PriceIntegrity`
   - Chapter ID: `chapter-12-maintain-your-priceintegrity`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-12-maintain-your-priceintegrity.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-12-maintain-your-priceintegrity.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-12-maintain-your-priceintegrity.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/12 - CHAPTER 12 Maintain Your PriceIntegrity.txt`
13. `CHAPTER 13: Learning from the Best`
   - Chapter ID: `chapter-13-learning-from-the-best`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-13-learning-from-the-best.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-13-learning-from-the-best.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-13-learning-from-the-best.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/13 - CHAPTER 13 Learning from the Best.txt`
14. `CHAPTER 14: Implementing the “Designing the Productaround the Price ”Innovation Process`
   - Chapter ID: `chapter-14-implementing-the-designing-the-productaround-the`
   - Chunks: `/Users/sachin/books/files/Monetizing Innovation/chunks/chapter-14-implementing-the-designing-the-productaround-the.jsonl`
   - Notes: `/Users/sachin/books/files/Monetizing Innovation/notes/chapter-14-implementing-the-designing-the-productaround-the.jsonl`
   - Summary: `/Users/sachin/books/files/Monetizing Innovation/summaries/chapter-14-implementing-the-designing-the-productaround-the.md`
   - Full: `/Users/sachin/books/files/Monetizing Innovation/chapters/14 - CHAPTER 14 Implementing the Designing the Productaround the Price Innovation Process.txt`
