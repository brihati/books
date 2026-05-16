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
  "chunk_id": "chapter-05-step-2-chunk-003",
  "source": {
    "chapter_title": "Step 2",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/05 - Step 2.txt",
    "source_pages": "23-46",
    "char_start": 11319,
    "char_end": 17256,
    "checksum": "dd54b4bcebda9b70"
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
Fig. 5: Popcorn - Packaging
AJIT GHUMAN
28
Let us look at another example (Figure 6), that of the Ford Mustang.

Fig. 6: Model Comparison - Ford Mustangs
A customer may be looking to buy a Ford Mustang. All Mustangs are
built on a common base but each model is priced based on the
variations in features offered - horsepower, engine specs, shell,
interiors, etc.
The sports car aficionado, who is heuristically inclined to associate
a Mustang as a status symbol, will be willing to spend more and opt
for the Mustang Shelby GT500. The base model of the Mustang
EcoBoost Fastback would not have the level of specs that the GT500
would offer. There would also be discerning customers who want
more features than the base model offers, but aren't willing to
splurge on the most high-end model. The manufacturer assesses this
segment as well and offers the Mustang BULLITT for them - priced
between the base and high-end models. This is a good example of
how the manufacturer is looking to maximize the area beneath the
curve by offering multiple features of a relatively horizontal product
through packaging variations.
This logic applies similarly to software packaging.
So how do you create packages for software?
PRICE TO SCALE
29
In my experience there are roughly two ways to go about this exercise:
1. Good-Better-Best: It is becoming common in SaaS to create 2-
3 step graded packages, nicknamed good-better-best
packaging, for different customer segments and to map these
packages to different price points that those segments will be
able to bear. Different sets of features are grouped into a
package and targeted at different market segments so as to
provide a set of capabilities that do the best job of solving the
segment’s main use cases. This approach works well in
capturing revenue from a market that has a large set of
prospects with less variance in their willingness to pay or avg
deal size, often these are SMB and Mid-Market segments. Here
deal velocity takes precedence over finely tuned price points.
2. Modular: This approach involves attributing value to distinct
groupings of features that unlock specific use cases for your
prospects. The modularity enables your packaging to vary
considerably between any two given customers. This works
better in a market where there is a high variance in
willingness to pay (WTP) and the average sale price (ASP) and
a smaller universe of prospects. In these situations, a high
revenue capture rate is more important than velocity. For
such cases, flexibility is usually king, and a well designed,
bespoke-fit type of package can help maximize revenue
capture in this segment.
The following figure illustrates roughly how I visualize the decision
of selecting a specific approach. A Good-Better-Best model is better
suited for when there is a large ‘n’, i.e. number of customers/
accounts available in the market to be sold that are somewhat
homogenous in their needs. For example, direct to consumer, digital-
first companies in the ecommerce vertical. On the other hand the
modular approach would be better if the market was more
heterogeneous. For example when the same product is sold to
insurance, telco, retail and/or hospitality where all these industries
have varying needs. The total market ‘n’ is small and the market is
also  heterogeneous, in that case depending on the circumstance one
AJIT GHUMAN
30
can make an argument of doing away with packaging as such. For
example, a selection of 20 top financial issuers with varying use cases
for a data science platform. At the end of the day there are no rules
to this, but hopefully this helps make your decision process clearer.
Once you understand these techniques, you can always mix and
match them for best effect.

Good-Better-Best Packaging
In order to understand good-better-best packaging let’s start with the
example of Salesforce’s Service Cloud pricing4 (Figure 7):

Fig. 7: Salesforce Service Cloud Packages

4 https://www.salesforce.com/products/service-cloud/pricing/
PRICE TO SCALE
31
Looking at Salesforce’s Service Cloud packages, you can see that each
package variant provides a range of sub-features that are common
and the higher priced packages offer more features. In ‘Essentials’
they are only going to offer case management, in ‘Professional’ they
will further offer CRM and case management. CRM is where you can
store all your account information and with just the ‘Essentials’
package, you may not be able to.
In the ‘Unlimited’ edition, they offer 24x7 customer support and may
offer AI features or some more enterprise features and charge you
higher for those impressive or lucrative features that are on offer.
This is rudimentary software packaging and pricing.
The packages are graded based on features that map to companies
of different sizes and needs (segments). One point of Salesforce’s
packaging grid is telling. They’ve clearly outlined on their website
what the prices for the different packages are. We can infer from this
that Salesforce is trying to achieve a high degree of price
standardization and transparency, which tends to be useful when an
organization has a large sales engine and a target market that it
seeks to attract.
The drawback of such an approach is that prospects can easily
comparison-shop to choose the right capability no-matter which
industry vertical they are in, making the sales more transactional
and missing out on pricing elasticity variances between industries
that generally tend to be able to pay more, e.g. Finance vs industries
that tend to be very price conscious, say, Retail.
Another example is that of a company called Amplitude, which offers
product analytics software. Here we can see that Amplitude has three
plans5, one of which is a completely free plan and the other two seem
to be catered to mid-sized growing companies and larger established
enterprises respectively (Figure 8).

5 https://amplitude.com/pricing
AJIT GHUMAN
32
>>>
