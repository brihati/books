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
  "chapter_id": "chapter-16-interviews-case-studies-with-top-pricing-leaders",
  "chunk_id": "chapter-16-interviews-case-studies-with-top-pricing-leaders-chunk-017",
  "source": {
    "chapter_title": "Interviews & Case Studies With Top Pricing Leaders",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/16 - Interviews Case Studies With Top Pricing Leaders.txt",
    "source_pages": "185-308",
    "char_start": 82229,
    "char_end": 89901,
    "checksum": "b19ad19a1c0f719b"
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
chase.
In April 2019, we came out with a subscription pricing model. At this
point, we had been selling our product for two-three years and had
over a thousand customers completely on the CapEx model. We
aimed to get new customers to start purchasing subscriptions. Once
we penetrated this base, we would start thinking about how to get the
existing installed base to switch over.
PRICE TO SCALE
231
In making this change, we wanted to make pricing comparable,
with a slight premium. So, if you were buying our subscription
offering Rubrik Go for a minimum three-year subscription, we
wanted to ensure this is comparable to that of a customer buying
CapEx (Perpetual License) with three-year support.

There was a need for a slight premium here. Think about it — if you were to buy an iPhone outright, it would be cheaper than if you did a three-year lease, as there’s a little premium for that cash flow. We knew we could demand a little premium going into an annual payment model. But, for the most part, we didn’t want the price to be significantly higher to incentivize customers to go into subscription. The more we thought about it, it was less about the price for us, and more about making a holistic program with additional benefits included in the CapEx license, to move customers to the subscription model. If pricing is equal or close, and customers see all these other benefits and  features in the subscription model, they naturally choose to go that way. Coming up with the Subscription Model While overall reception was good, a key critical decision Rubrik made was to not focus only on new customers, but also remember the existing ones that got us till here. The subscription model was always incremental to CapEx one, which wasn’t taken away to avoid alienating customers. Without naming anyone, the industry has seen certain decisions that alienated the existing installed base; it leads to backlash and ultimately reintroduction of the old model. To walk through the process that we took to get to our subscription model - we started with a six-month-long study to really understand AJIT GHUMAN 232 the pain points for our customers in the backup and recovery space. This included interviews, surveys and even a conjoint study where customers put together their own pricing and packaging solutions. We provided a series of products, and had customers pick the top three they would want to see bundled together. This in-depth customer study allowed us to realize the pain points: 1. High upfront costs with CapEx. 2. Backup and recovery — Chief Information Officers (CIOs) mandating teams to migrate X percent to the cloud within three to five years. So, they want to make sure the license model they’re purchasing will future-proof them for the cloud. 3. Unpredictability around costs, specifically related to hardware refreshes. Once we found these pain points, we needed to create a subscription program to tackle them, but keep pricing relatively in the same range as the CapEx model. If we resolved the issues, we thought hopefully everyone will start choosing this option naturally over the CapEx model. We didn’t want to do away with the CapEx model in order to not alienate anyone, but wanted to incentivize customers to the subscription model by offering more benefits. The solutions: 1. Prepay upfront: Our subscription gave the option of prepaying all upfront, or an annual payment option which was slightly higher. 2. Future-proof: We also included license transferability between the hardware appliance and the cloud for the period of the term, to eliminate worries of future-proofing, eliminating double charges for using our software to deploy to the cloud. 3. Free refreshes: Lastly, for complicated refreshes or unpredictable costs, we decided on an evergreen hardware refresh program — as long as you continued to renew every three years, you’d be eligible for a free hardware refresh. PRICE TO SCALE 233 Essentially, if you bought Rubrik today on subscription, you would not have to worry about paying for hardware again. All these benefits were discovered through the customer research phase, where we also asked about willingness to pay, how much they would be willing to pay more than the annual payment model, etc. The holistic program is that you want to make sure to solve the customer’s needs, especially as it’s related to your core platform. Enabling Sales to Succeed Sales enablement and Total Cost of Ownership (TCO) building is a very critical piece to pricing and packaging. The way I see it as a product manager, is that my product is my license. I research my license and then make a roadmap for the first one. If there’s going to be a second product, I work on the upgrade license. I have to take this roadmap to the market and ensure that everybody understands how to sell it, understands the value of it — both customers and the field. Then, I also have to follow all the success metrics and tracking. One thing we learned quickly (as soon as we launched), is that the field was starting to do a TCO against itself, positioning the CapEx model and Go model to the customer at the same time. This ends up confusing customers and slowing down the deal. If you show both models, the customer is bound to ask for a TCO for both. This ends up with a company doing a TCO against itself rather than the competitor. We nipped this in the bud. If it is a pure evergreen customer, they’re used to subscription. If they’re buying this, or worried about refreshes and going to the cloud, they have the Operating Expense (OpEx) budget. If they’re a Federal or State, Local and Education (SLED) customer, they have to buy CapEx. They’re not interested in SaaS, nor do they have plans on moving to the cloud. If they’re an existing customer, go, CapEx, for example. AJIT GHUMAN 234 In this way, we make a Go/No-Go table. We position one model at a time, do one TCO at a time. The majority of the time, Rubrik Go would satisfy it, but in some edge cases, it doesn’t. Some at Rubrik who have earlier sold SaaS and subscription at peers like Snowflake or ServiceNow, got this point easily; but others who had to switch over, came from box- pusher type selling — at places like Dell, EMC and more. Getting these lifers in the backup and recovery market to buy into the vision and positioning of Rubrik Go as the main option, took some time. We learned from this and made it part of our pricing and packaging enablement, and go-to market for all other offerings thereafter. It can get confusing when you start having a portfolio of products. This task falls on Pricing and Packaging (P&P) at Rubrik; at other places, it may fall on sales enablement. But I believe only a P&P strategy team can do enablement best, because there’s a lot of detail that goes into it. Selecting Pricing Value Metrics Since we were still selling appliances we didn’t really need to mess with the metric for the hardware much and it remained tied to raw backend terabytes. Selecting the value metric actually comes more in play with our SaaS products. That has no hardware involved. For instance, we have Office 365, other workloads, security or compliance products that we may be pricing as not included in our base product. In those scenarios, it’s more strategic to get the metric right. People think pricing and packaging is easy. One can figure out the price and willingness to pay, but what metric you price on, how you package it and what’s included — that requires more strategic rationale. We first set the baseline and figured out the most comparable market in the industry, how they price, and what is the overall market consensus feedback on that.
>>>
