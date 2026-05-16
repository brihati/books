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
  "chunk_id": "chapter-16-interviews-case-studies-with-top-pricing-leaders-chunk-004",
  "source": {
    "chapter_title": "Interviews & Case Studies With Top Pricing Leaders",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/16 - Interviews Case Studies With Top Pricing Leaders.txt",
    "source_pages": "185-308",
    "char_start": 9049,
    "char_end": 16359,
    "checksum": "cb54f62461e931ef"
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
modules that we would have struggled to sell before. So, we’ve allowed AJIT GHUMAN 188 our average deal size value to increase considerably, and created the possibility for the Customer Success team to upsell more proactively - throughout the lifetime of the customer. Finally, we’ve added a services revenue stream that didn’t exist earlier, based on this pricing change.

PRICE TO SCALE 189 Revamping Packaging & Pricing at Gainsight, with Johnny Cheng My interview with Johnny Cheng on his time at Gainsight was one of the most instructive in terms of the challenges that occur with pricing when a company is in its high growth stage. As the then Director of Product Marketing at Gainsight, Johnny commandeered Pricing Strategy, CPQ (Quote-to-Cash), Go-to-Market Pricing and Packaging, Analytics and Reporting, as well as Deal Strategy and Support. He elaborates in his own words. How Gainsight Pioneered the Customer Success Movement Gainsight is the leader in Customer Success (CS) software. We are to CS platforms what Salesforce is for Customer Relationship Management (CRM), or what Workday is for Human Resources (HR). The CS movement happened five or six years ago. If you look at CS roles back then, they didn’t really exist in an organization. You would have a support person and an account manager — and that was basically it. Gainsight pioneered the whole CS movement and actually built a community of CS professionals — almost a set of buyers. As a consequence of the community, we started seeing elevated roles like Chief Customer Officer (CCO). Interestingly, a lot of our early adopters and champions are CCOs at a bunch of companies now. In terms of our target buyer, it is obviously CS professionals, like the CCO and VP, who we sell to. For more traditional companies, we try to sell to IT or the Head of Support. This is especially true for companies going through a digital transformation, moving from a perpetual license to a subscription model. Earlier, when they deployed hardware, they would just charge for support and move on. Now, as they’re moving to a subscription AJIT GHUMAN 190 model, they see a bunch of different customer touchpoints. And so, they need software that can basically handle that. That’s kind of our sweet spot, in terms of who we sell to. We definitely have a lot of big names that really believe in this whole transfor- mation, which takes them from what they always did, to ongoing CS. Gainsight’s Pricing Problems One of the reasons Gainsight brought me on-board was to fix the number one thing that was broken there – pricing. In particular, the most broken segment was mid-market. Ironically, mid-market was actually their product-market fit sweet spot. Smaller customers couldn’t afford them altogether and larger companies could probably build something similar themselves. But to have pricing be broken in your target segment is bad. In the mid-market space, at the time, Gainsight used a feature-based pricing model where it was just a good-better-best offering — that’s it. For a set price of say $1,000-$2,000-$3,000, you just get a good- better-best package. I’ll go into why that was broken. They also had an Enterprise model, where it was just completely discrete pricing. Sales would basically make up a price. The top of the Enterprise deals worked fine with that approach because they were value selling, and they didn’t need much guidance. But Gainsight was stuck in the mid-market segment, where they didn’t have the luxury of doing a return on investment (ROI) analysis of a five-year launch and building a discrete pricing model; all while wanting to sell on value and not leave money on the table. The good-better-best model wasn’t even working, because they were always selling the middle tier package each time. Even when they sold the larger tier, it was at the same Average Selling Price (ASP) as the middle tier. Not only that, but the packages created a lot of shelfware, and there were constant downsells. PRICE TO SCALE 191 Gaisught’s software was extremely custom. Every company does CS differently and every client needs their platform to be something different. It’s not cookie-cutter or like Marketing Automation, with very defined for-use cases. Everyone knew how to do that. With CS, no one knew how to do it! Everyone had their own view, their own brain. The good-better-best approach didn’t really work. For larger Enterprise companies — the top ones — if you did an analysis based on their price points, it was all over the place. They were selling stuff for like $5 a user or then $1,000 a user. It was just like the Wild West, whatever money they could get, they just went for it! Johnny’s Approach To Packaging & Pricing Creating a Modular Packaging Solution Looking at my past experience, one thing that worked really well was solution-based selling. We created modular solutions — think of them as Lego pieces. We could tell a salesperson, “Here are your Lego sets, you can put them together however you want.” But, there was a price tied to each module. It was almost like a packaged-plus-à la carte hybrid model. In order to develop these Lego pieces, I did this packaging exercise (which I do at all of my companies) in the following steps: 1. List out: We broke down every single feature and just listed them all out. These usually end up in the hundreds. 2. Group up: Once we had these, we looked through different lenses for how to bucket these capabilities into what I call modules - capabilities that are natural to group together, like things a set of users would commonly use. 3. Test: When these bucketed modules were created, we started going through iterations to test them against customer segments, to see whether they fit that segment’s usage. 4. Rearrange: We also checked to confirm if the features that formed the modules were mutually exclusive and completely AJIT GHUMAN 192 exhaustive (MECE), or not. Based on the testing, we broke up or combined these modules further. 5. Categorize: Finally, we categorized the modules we arrived at - based on their sophistication, price point, value, and a bunch of historical analyses about how they typically performed, adoption, and more. Going through these categorizations, we started noticing patterns that helped decide packaging: • What if these products are of very high value, they’re table stakes, and used by everybody? These went into a base package. • What module does only the most sophisticated customer see, is of very high value, and increases adoption? This could be its own standalone add-on module. The caveat with this approach is that it requires a fine balance, and not listing out a hundred things. What you do want is to group the modules to a point where the salespeople can understand it. Then, they can sell the value of each individual one, and it can carry a discrete price. Setting The Value Metric The main benefit of a solution selling model is that you can have zero to two value metrics per module, if you really wanted to go with that level of granularity. Our primary value metric at Gainsight was users; our secondary was number of customers. If you think of the individual modules, they were either based on: a) Users, or b) Customers, or c) Users and customers, or d) None (which is a flat fee). PRICE TO SCALE 193
>>>
