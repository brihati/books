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
  "chapter_id": "chapter-11-pricing-example",
  "chunk_id": "chapter-11-pricing-example-chunk-003",
  "source": {
    "chapter_title": "Pricing Example",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/11 - Pricing Example.txt",
    "source_pages": "143-158",
    "char_start": 6347,
    "char_end": 14002,
    "checksum": "96afd6f6f2fa16f0"
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
th much greater efficiency and at high volume What are the primary expected benefits of the product? ● Reduction in customer support costs (human) - expecting to see a 30 to 40% reduction in agents required as compared to live chat ● Higher consumer NPS/satisfaction ● Faster issue resolution times PRICE TO SCALE 143 What buyer personas are involved in the buying cycle? ● Expect to sell to Head of Customer Support ● Get introduction via Heads of Digital, and/or Marketing Who are our main competitors? ● Zendesk ● Salesforce Service Cloud ● Both offer more robust customer service offerings, out of which the chatbot is one part of the solution What is our differentiation relative to competition?

● Much better use of AI, leading much higher automation rates ● Competition’s technology takes much longer to implement, our product is self-service and can literally be built and deployed in a few days Where are we weaker relative to competition? ● The agent-side of our product is bare bones and doesn’t match what companies like Zendesk and Salesforce have to offer for large agent teams Why would companies select us? ● They have a high volume of customer service requests, with relatively small teams burdened with this volume and difficulty scaling up agent counts very high ● Less complicated issues, but high volume of customer issues ● Industries that would be a fit: ○ Gaming ○ Digital Media ○ High Growth Tech Companies What were the main reasons clients in the beta program were interested? ● Fast client business growth rates and high opinion of ACME Inc’s current product offerings. ● Avoid extensive external RFPs Furthermore, our AE interviewed revealed that she thinks this product could increase win-rates of ACME’s main product line and that this product could be ‘thrown in’ to sweeten the deal. (note that this input contradicts the VP of Product Management’s intention of making this into a successful product line, so while we may not ‘throw in’ the product, it could definitely be a promising upsell for certain types of clients) AJIT GHUMAN 144 We now have enough information to come up with our hypothesis on positioning, packaging and pricing. Positioning Given the info provided, we can write a summary positioning statement: ACME Inc’s Chatbot product is a purpose built solution to automate the resolution of high volume customer service issues for high growth technology enabled companies, unlike (SFDC/Zendesk) ACME’s proprietary AI technology is able to fully automate 50-60% customer service issues and go live within days. Packaging Since the product is still in its nascent stage, we don’t have to fret too much about packaging except for making sure we take into account differing price elasticity for ACME’s existing mid- market segment and a potential new enterprise new prospect customer segment. The packaging differentiation could simply be offering differing service levels and an option to build custom integrations which enterprise customers often need. Given this, we will create two different plans targeting mid- market and enterprise respectively, with the former being more of a self-service deployment model and the latter being a custom implementation with additional professional services support. Pro Elite The Pro package is made for clients that handle a lesser case volume per day. Some of the features included in the Pro package are: ● Base chat widget ● Canned service bots ● CRM integration ● Tech support ● Training videos Companies with higher case volumes would see more benefits by using the Elite package. It is designed to be more customizable with a greater degree of support. Some of the features included in the Elite package are: ● Special AI models ● Custom service bots ● 24x7 support ● Dedicated CSM ● BI analytics PRICE TO SCALE 145 Pricing Here is where we must make a more critical decision. We could either price as the industry does, i.e. on a per agent basis (capability model) or we could price based on the number of issues processed/automated (usage model). Given that the best potential fit of our product will be companies with smaller agent teams AND high customer support volume, pricing on usage would both be better tied to value and offer better revenue upside (since the alternative per agent price could limit revenue potential). In the usage based model we have a few options: ● Price per automated (partially or fully) support case ● Price per bot interaction ● Price per any initiated chat/chatbot interaction ● Price per bot step invoked How do we decide which metric to opt for? (read Mixpanel’s pricing metric case study to further dive deep into tradeoffs involved) The metric must be a) simple to understand b) easy to track c) tied to value d) and be predictable. While the price per automated support cases might be the most directly related to the value we offer, it can be unpredictable with some companies being better at being able to build automations than others (read a related case study on Nosto later in the book about this). Price per bot interaction suffers from the same problem. Pricing per bot step invoked is additionally too complex for easy understanding. We hone in our hypothesis of the main pricing metric to be around any initiated chat or chatbot interaction. This extracts value based on usage of the product, but keeps the revenue predictable as the client will still be on the hook for actually implementing the chatbots. The challenge is then to convince buyers in the sales cycle that the technology indeed performs as stated. We are being completely cognizant that this pricing is different from the industry’s established pricing model, but what enables a different metric is that the product is sufficiently differentiated. AJIT GHUMAN 146 Hypothesis Testing Now that we have an informed hypothesis, how do we conduct a market test? The process we follow here is roughly: 1. Identify a representative market sample 2. Select the right interview/analysis technique 3. Synthesize our learnings In order to select a representative sample we will look for high- growth technology enabled companies within the company’s cus- tomer base (this will serve as a mid-market proxy) and then get feedback from larger ‘enterprise’ firms from the broader market. The amount of companies we can test with depends on what methods we use, who we have access to as well as our own resource constraints. Given the newness of this product, it would be hard to get enough input on pricing from just surveys (which work well for more well established product categories). I would expect that primary research would reveal a lot more information, and we can club that with a basic pricing range survey. Since ACME’s customer base is around 100 companies, with about 40 companies fitting the high-growth tech criteria set earlier, we should be able to get enough of a sample set from ~10 live conver- sations and 15-20 survey responses. In the broader market we are not so constrained, so we will attempt to survey a few hundred enterprise companies (this will generally give us a 10-15% response rate) and live conversations again with ~10 companies. For primary research we will use the template described in the earlier chapter. Specifically our live deck will have the following sections: • Intro to the technology/product PRICE TO SCALE 147 • Force rank pain points (relating to handling customer support issues) • Demo • Unprompted feedback • Force rank benefits • Open-ended feedback on pricing metric • Low price (poor quality) and High price (too expensive) bounds To test a specific price point we would need to translate our metric to
>>>
