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
  "chunk_id": "chapter-12-usage-based-pricing-chunk-002",
  "source": {
    "chapter_title": "Usage Based Pricing",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/12 - Usage Based Pricing.txt",
    "source_pages": "159-164",
    "char_start": 5557,
    "char_end": 9735,
    "checksum": "2a0990ffd3eef852"
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
ions, it lowered
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

33 https://nextbigteng.substack.com/p/consumption-vs-subscription-models-
downturns
34 https://kellblog.com/2022/10/13/mapping-from-annual-to-monthly-and-usage-
based-saas-metrics/
PRICE TO SCALE
159
understand the implications of this model on financial metric
reporting. The blog explains the complexities of shifting from annual
to monthly and usage-based SaaS metrics, stressing that traditional
metrics like ARR and MRR may not fit well with usage-based pricing
models. It suggests that focusing on trailing spend and rethinking
metrics like NRR and CAC is crucial for better alignment. The author
urges companies to understand what "recurring" revenue means in
these contexts and adapt their metrics accordingly.
Learning 4: Operational plumbing for
UBP can be a critical hurdle
Even if UBP makes all the sense for a given organization, and there
is all around alignment in this being the main approach to pricing
there is still a challenge in implementing it. This challenge tends to
be harder to overcome in larger established orgs compared to
smaller orgs given legacy tech/sales processes.
For UBP to work, the pricing metric in question must be metered in
the product across all customers. This data must be sent to the CRM,
CPQ, ERP and Billing system so that accurate invoices are generated
for customers. Additionally, sellers must be able to sell with “esti-
mated spend” rather than fixed spend with traditional subscription
sales. The technology implementation around this is non trivial and
must be project managed with diligence.
At this moment there are a ton of vendors adjusting their technology
stacks to solve this problem from metering companies, feature flag
implementation companies, CPQ and Billing vendors. At Monetizely,
we ourselves built a CPQ from 2023-24 and exited the market because
of how slow moving, fractured and similar the vendors were to each
other. Each individual technology listed here can take anywhere from
4 months to 2 years to implement.
I really cannot overstate how complex this can get and the most ideal
pricing strategy certainly is not the best for an organization. Top tier
pricing consultants do not have experience in operations and do not
AJIT GHUMAN
160
get it. VCs do not get it. Industry Analysts do not get it. (The only note
I will add is that online sales or PLG orgs or smaller startups are less
likely to have the same challenge because the pricing could be simpler
and since it is core to product delivery, you’d like to have your
engineering build the stack right upfront.)
Learning 5: Sales compensation and
forecasting should not be ignored
Assuming there is a direct sales element to your software sale, in
order to implement UBP you must rethink your sales compensation
structure. If due to UBP the initial sale price is minimal, then the
sellers will want some sort of commission based on the growth of the
account, it is something you will not be able to avoid. Sales
forecasting becomes important for the same reason that valuation
estimation becomes tricky, and a reasonable model will need to be
built for the sales motion to support usage based pricing.
In my own experience launching UBP, my enterprise sellers straight
up told me that there was no chance that they would even surface up
UBP to their buyers until key questions of sales compensation were
clarified. When a seller gets paid, how much upfront, and how much
later on, matters in this structure and will be scrutinized by the reps.
>>>
