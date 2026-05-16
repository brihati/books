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
  "chapter_id": "chapter-07-step-4",
  "chunk_id": "chapter-07-step-4-chunk-007",
  "source": {
    "chapter_title": "Step 4",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/07 - Step 4.txt",
    "source_pages": "65-98",
    "char_start": 30275,
    "char_end": 37926,
    "checksum": "bb16f99125471507"
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
late purely the impact of the
software in question and on the other hand, organizations cherry
pick their best customers to be used in these case studies.
This sentiment is echoed by Tomas Tunguz in his own blog, The
Siren Song of ROI Based Pricing25
“If we reflect on the most successful software companies, the very
largest, very few sell based on ROI. What is the return on investment
of a Salesforce or a Workday deployment? How do you calculate it?
How does an AE defend it?
Many times these ROI calculations assert unquestionable numbers.
But most buyers approach these kinds of arguments with skepticism
and even cynicism. Sometimes, they have been burned in the past
making kind of arguments.

25 https://tomtunguz.com/the-siren-song-of-roi-based-sales/ PRICE TO SCALE 87 Other times, buyers recognize that it is almost impossible to measure true return on investment. Switching costs are rarely accounted for in his calculations. Measuring increasing productivity is very difficult. Soft costs “challenge the math.” The point being that a well paid consultant can come up with an amazing ROI number and when your customer does this analysis at the end of the year, the numbers they see will not be this rosy. So if you base your pricing to be a percent of ROI, you and your organization will then bear the onus of justifying it at year end. This is why, while all companies talk about ROI, nearly none use it for pricing. Don’t get me wrong, ROI is a great tool, but for price justification, just not for pricing. Competitive & Category Price Points So far in the book we’ve covered some critical elements towards set- ting the price of our product(s) and we’ve mostly looked at our value delivered to customers. Our analysis wouldn’t be complete if we don’t look at competition and the larger product segment/ category we operate under. In order to understand this, it's helpful to think about the nature of certain markets. We can broadly segment markets into the following subtypes: 1. Blue ocean: In this type of market, your product is replacing a different way of doing things and faces lesser head to head competition. Usually this market has seen action before but now could be mistaken for a boring place to be. In this type of market, you have many more degrees of freedom on how to price and how much to price. A high price elasticity cus- tomer such as a national bank might end up paying 5-10x AJIT GHUMAN 88 more than a national retailer. However, the issue in this mar- ket is more category and solution evangelization and dispro- portionate effort needs to be made to ‘get things going’ in the market, until then every sales is on its merits. Thankfully you avoid the problem of commoditization and a pressure to keep prices low. 2. Monopolistic: I like to call this market similar to a vacuum cleaner where one big company sucks up most of the market and sets the benchmark for product functionality and price. The customer service landscape is one such with Zendesk taking the lion’s share of market spend and attention. The CRM market is another, where Salesforce sets the agenda. Smaller players exist but only at the margins or as add-ons on top of the core functionality these players bring to the table. Head on competitors tend to fail, unless they bring a truly 10x ad- vantage over the incumbent. Pricing in this market is in reference to the big player. If Salesforce charges $150 a seat, then your pricing is evaluated in context of it - i.e. it becomes an anchor in the mind of prospects and customers. And if a company pays $150/seat for its CRM, then a limited capability that adds on the CRM would automatically have to be a reason- able percentage of this price. This eventually can end up in a race to the bottom price struggle if the incumbent fails to innovate, as new players crop up and in some cases copy ex- isting capabilities and offer it for cheaper. 3. Renaissance: I didn’t have the right technical term for this market, but I call this the Renaissance market where a bunch of small players are vying for dominance but there hasn’t been a clear leader that exists. The difference between this market and the Blue Ocean market is that here key pricing variables are converging, i.e. most players will now start charging per seat or per usage. Value propositions are simi- lar but capabilities have significant room for differentiation. There isn’t much to anchor outside of the customer segment, and all focus needs to be in correctly serving your ICP. In a PRICE TO SCALE 89 sense pricing agility within the right pricing structure be- comes more important than having the exact right price point. Once you understand the type of market you are in, then you should have an intuitive grasp of how much you should account for compet- itive price points and pre-set anchors in the minds of customers. Let’s now look at a few other variables before we actually come down to our decision of setting the price point. Your Cost of Delivery Many pricing experts and articles give some real estate to ‘cost-plus pricing’. This approach essentially adds a margin amount to the cost of production of a given product. This may make sense in commod- itized markets for products which have hard costs of production, but for products like software (at least in the application layer) it makes very little sense to do cost-plus pricing since there are mostly hard setup costs but very little production costs, or cost to serve every additional customer after that. This is also why software is generally a high margin business. (Some amount of cost-plus pricing may still be relevant in SaaS, and that happens the closer the software is to the infrastructure layer and tied to hard costs such as compute power, storage, etc.) On the whole, I am still surprised when time after time, seasoned executives push back on pricing by saying “we need to charge more for this because it’s costly to deliver”, or, “this x feature is really simple so why are we charging so much for it?” For the most part in software sales, pricing for software is based on perceived value to the customer and not the cost of production. Albeit there is always an implementation price charged in addition to account for the delivery of the product to the customer, but even that cannot seem unreasonable 10-15% of software ACV is standard in the industry today. AJIT GHUMAN 90 All that being said, costs still need to be looked at, because they can a) act to sanity check your go to market strategy and b) to ensure you actually get the build once distribute-many economic cost advantage Average Cost vs. Marginal Cost in Providing SaaS Services In SaaS companies, a commonly used financial metric for deter- mining price points and assessing profitability is the Cost of Goods Sold (COGS) per seat This metric is typically calculated by dividing the total cost of providing the software across the entire customer base by the number of users or seats. While this approach is useful for assessing overall profitability, it can be misleading when it comes to making pricing-related decisions. The key issue lies in the difference between average cost and marginal cost. The average cost reflects the total expenditure spread across all users, giving a broad view of the cost structure. However, the marginal cost: the cost of providing the service to an additional user or seat, is usually significantly lower than the average COGS. This discrepancy occurs because many of the costs associated with SaaS products, such as development, infrastructure, and customer support, are largely fixed or do not scale directly with the number of users.
>>>
