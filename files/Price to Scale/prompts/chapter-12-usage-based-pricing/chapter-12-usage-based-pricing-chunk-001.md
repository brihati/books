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
  "chapter_id": "chapter-12-usage-based-pricing",
  "chunk_id": "chapter-12-usage-based-pricing-chunk-001",
  "source": {
    "chapter_title": "Usage Based Pricing",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/12 - Usage Based Pricing.txt",
    "source_pages": "159-164",
    "char_start": 0,
    "char_end": 6257,
    "checksum": "3cb0a0d9805b7b3e"
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
155

USAGE BASED PRICING
Not A Panacea

The experience of launching Usage Based Pricing (UBP) at a former
employer and well-known software company has formed the basis of
a lot of learnings explained in this chapter. UBP today gets a lot of
positive/panacea-type coverage from pricing practitioners, leaders
and VCs. However, in my opinion UBP can “feel/sound” very good. It
markets very well. But the under-the-hood math, implementation
and rationale require a level of nuance that is not obvious in how
great this sounds at first blush.
I have had to fight to roll back executives' grandiose pitches, which
would have led to half the revenue loss of my former product line if
implemented as originally envisioned. It was always funny to me that
some specific executives at this company thought this "pain" was
worth the "gain" of moving to UBP.
I am not saying that UBP would not be a great fit for certain
companies and types of products, it probably will and has been, as
evidenced by NRR rates of companies like Snowflake ~130%. In
Janelle Teng’s, Next Big Teng Substack,32 she cites research by
Goldman Sachs indicating that companies with consumption models
increased net new revenue faster than subscription peers.

32 https://nextbigteng.substack.com/p/consumption-vs-subscription-models-
downturns
AJIT GHUMAN
156
Learning 1: Your market must be a fit
to UBP
Usage based pricing, or “paying only for what you use,” is a very
compelling pitch when it comes to pricing. It certainly stands to de-
risk the customers’ buyer purchase. It also helps to position your
product/company as a modern mover/shaker in the eyes of VCs and
Industry Analysts. After all, companies like Snowflake and Amazon
do very well with it.
But even if it made all the sense in the world on the surface, that has
nothing to do with the market and industry you serve. Read the
example about Kustomer’s CEO earlier in the book about being
unable to innovate with their pricing strategy because the customers
who purchased Customer Service software were only used to paying
$ per agent.
Now, this may change in the near future with AI disrupting existing
market categories, when exactly this happens and to what extent isn’t
clear. SaaS as an industry always operates ahead of the innovation
curve, it also means that if your customers are in “traditional”
industries/segments, then they are just not going to “get it.” Similarly,
if you sell a Salesforce app, you are naturally going to be compared
to the base $ per user pricing that Salesforce offers.
I have seen executives make big bold claims of a change in their
pricing metric to pacify Industry Analysts, where they haven’t truly
had enough conversations with a representative sample of their
customers. Don’t be this executive.
PRICE TO SCALE
157
Learning 2: The taxi vs car dynamic –
apply UBP only to the right product
type
Many people buy equipment in their homes as a capability that they
need to have, even if they don’t use it every day. An example of this
is a car purchase. It is indispensable for most people and yet many
only drive their cars once a week. If the car company moved to usage-
based pricing, would it still work for the car company? It would just
not fit the type of product being bought. Similarly, many software
products are bought as capabilities that are needed. But not a lot of
people are actively logging into the product and using it every day. In
fact these could be very sticky products and be perceived as
indispensable by customers and yet with very low usage. What would
be the point of moving the pricing model of such a product to UBP?
In fact, what is likely to happen is a sharp downfall in revenue
because the product was hardly being used in the first place.
I have personally been in the situation where a competitor moved
their pricing to UBP creating FUD in the minds of our executives but
upon speaking with customers and analyzing their usage patterns it
was clear this was a capability purchase for them. The FUD did its job
and made our company chase the bright shiny object of UBP when it
wouldn’t be a fit for them specifically.
However, if you are building a new AI-based product like an image
or text generation product, and specially if it is closer to a founda-
tional service offering that will underpin different application-layer
products, then it is less likely to be considered a capability and more
a consumption oriented service where UBP will fit.
AJIT GHUMAN
158
Learning 3: UBP reduces revenue and
valuation predictability
UBP is sometimes confused with customers “only paying what they
will use”. This is not true and in fact can set up a company for drastic
revenue variability. Do you see the problem in this statement? Usage-
based pricing means paying based on a specific pricing metric that
is related or specific to the use of the product. It does not
automatically imply a PG&E-esque payment for usage. Many times it
can mean buying a set quantity of a product’s consumption, think
data plans with Verizon or AT&T. This is covered in the tariff
structure options (linear vs 2-part vs 3-part) earlier in the book. This
provides for revenue predictability.
However, there definitely is inherent revenue unpredictability in UBP
as compared to traditional user-based models. In Janelle Teng’s, Next
Big Teng Substack33, in a May 2023 post she highlights this issue,
“Last week, cloud data infrastructure company Snowflake reported
its FY24 Q1 earnings. While the company posted solid headline and
bottom-line numbers that beat consensus expectations, it lowered
FY24 revenue growth outlook for a second time within the last 2
quarters, causing the stock to tumble ~13% after hours (chart above).
Snowflake pointed to degrading consumption patterns and a lack of
predictability of when headwinds might subside as key reasons for
the revision”.
Additionally, what other thing does this variability imply? That the
fundamental valuation model of subscription-based software will not
directly apply to usage-based companies. The same valuation multi-
ple cannot now be applied if the revenue is variable/unpredictable.
I further recommend reading Dave Kellog’s blog post34, “The Mental
Mapping from Annual to Monthly and Usage-Based SaaS Metrics” to
>>>
