Extract preservation notes for this book chunk.

Rules:
- Preserve concrete content: claims, examples, stories, names, dates, numbers, definitions, terms, and useful quotes.
- Keep wording faithful to the source; do not add outside facts.
- Quotes must be short and must appear in the chunk.
- If a field has nothing meaningful, leave it as an empty list or empty string.
- Return only valid JSON matching the schema.

Schema:
{
  "book_id": "price-to-scale",
  "chapter_id": "chapter-05-step-2",
  "chunk_id": "chapter-05-step-2-chunk-004",
  "source": {
    "chapter_title": "Step 2",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/05 - Step 2.txt",
    "source_pages": "23-46",
    "char_start": 17210,
    "char_end": 22690,
    "checksum": "9d977c8b7ee93fcd"
  },
  "summary": "",
  "key_points": [],
  "arguments": [],
  "examples": [],
  "stories": [],
  "definitions": [],
  "names": [],
  "dates": [],
  "numbers": [],
  "places": [],
  "terms": [],
  "quotes": [],
  "actionable_lessons": [],
  "open_questions": []
}

Chunk text:
<<<
5 https://amplitude.com/pricing
AJIT GHUMAN
32

Fig. 8: Amplitude Pricing Plans
It’s interesting to note that they do not expose the pricing for the
‘Growth’ and ‘Enterprise’ plans. This indicates that they are going
after a broad market across verticals where comparably sized clients
might have differing price elasticity. Not publishing a price allows
them to capture greater value from clients that are able to pay more.
In the subsequent chapter, we will see how this is accomplished by
creative discounting buffers and approval rules for your sales team.
The ‘Free’ tier offered by Amplitude is another indicator that they
intend to reach a wide market, the reason being that ‘free’ plans have
a poor conversion rate in general to paid plans and the offer would
only make sense if a) They were going after a large TAM and/or b)
They want to undercut a competitor.
Now, this is not how the pricing page always looked for this company.
I always find it interesting to do some research using the Wayback
Machine and seeing how a company’s positioning and pricing have
evolved. Here are two historical snapshots of their pricing in 2016
(Figure 9).
PRICE TO SCALE
33
April 2016-

Sept 2016-

Fig. 9: Amplitude Pricing Plan Evolution
Can we infer anything from the evolution of their pricing page?
I would suggest that what likely happened is as the company found
new customers, they realized many of them could pay much more
than the company initially charged. Now, this is all well and good,
since the company in 2016 probably was a new entrant to the market
with fewer feature differentiators and less of a brand cache. In 2020,
AJIT GHUMAN
34
as they innovated with their product and became a more trusted
brand, they probably charged more and hence removed the specific
pricing from their product page as they didn’t want to peg their
prices low.
OK, so now that we understand how this type of packaging looks like
in real life, how do we create this for our own product?
Well for one we know the output of our effort needs to fall into
roughly three (or four) packages or tiers. The goal is to bucket
features together such that there is:
1. Gradation: There is a gradual upward gradation of capability.
2. Package <> Segment Fit: Each package’s capabilities map to
a significant representative market segment that is likely to
auto-select a specific package for its needs (i.e. a certain
segment always chooses the middle tier, another segment
always chooses the bottom-most tier).
3. No Shelf-ware: If at the end we find that a certain package is
rarely picked by its intended target segment, then that
package needs to be removed. Similarly, if we find a package
is often selected but a key underlying feature is unused, then
that feature shouldn’t be part of the package. (Read the
Gainsight example in the case study section of the book to see
how poorly fit packages impact a company’s sales motion)
Start by thinking of broad segments of your customers based on your
sales motion. One way to do this is by company size and simply use
a standard grouping like SMB, Mid-Market, Enterprise. Now create a
set of feature groupings such that there is a 1-1 mapping between
the feature groupings and the prior defined customer segments.
Here is a fictional example of this exercise for a marketing
automation product (Figure 10). We have grouped features to map to
our assumed needs for each market segment. The groupings are
graded and more complex at the top end.
PRICE TO SCALE
35

Fig. 10: Packaging our Automation Product
At this point, we have our initial hypothesis of packaging, but this
needs to be tested against our selected customer segments to see
whether there truly is package <> segment fit. In the next chapter, we
will cover research methods to answer this very question.
But before that let’s now take a look at modular packaging.
This discussion brings up an important point on pricing
transparency. According to a recent report by Chartmogul6
roughly 75% of SaaS companies publish pricing on their websites
and 25% do not. In my opinion, this is interesting data but by no
means a reason to follow the herd per se.
I’d like to propose a simple 2x2 matrix (Figure 11) to decide when
it would make sense to publish the prices along with the packages
on your website.

6 https://blog.chartmogul.com/saas-pricing-report/#pricingMatters
AJIT GHUMAN
36

Fig. 11: Deciding on Price Transparency
When you have a large market with a high degree of homogeneity,
then it is feasible to emulate other SaaS companies and publish
the complete pricing structure online (replete with packages and
prices) as it can help you scale your sales engine and maximum
value from the market. On the other hand, if your market size is
limited (say Fortune 100 Retailers), or heterogeneous (say, across
Retail, Pharma, Airlines, etc.) then the call is more subjective. I’ve
worked in enterprise SaaS companies that have opted to not
publish any pricing publicly so as to give their Sales teams more
ability to sell a targeted offer to their prospects. In those cases, the
packages were defined internally but there was lower price
transparency which dissuaded package comparisons and enabled
them to extract requisite value from prospects that had varying
amounts of willingness to pay or price elasticity. In this specific
context, sales reps appreciated their ability to offer their prospects
the right package without necessarily getting into the ‘shop-a-
package’ discussion.
>>>
