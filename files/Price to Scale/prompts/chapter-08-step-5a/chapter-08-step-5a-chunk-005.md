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
  "chapter_id": "chapter-08-step-5a",
  "chunk_id": "chapter-08-step-5a-chunk-005",
  "source": {
    "chapter_title": "Step 5a",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/08 - Step 5a.txt",
    "source_pages": "99-124",
    "char_start": 19775,
    "char_end": 27411,
    "checksum": "c52cf74184e4c073"
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
me couch the word ‘simple’. It is only simple in relation to a CPQ build out but can be significantly involved. When I revamped the calculator based on new packaging and pricing at Narvar, it took me well over 2 weeks to make sure it covered all our pricing scenarios and was setup in a user friendly way, where sales reps could easily duplicate the main tab of the calculator and get cracking at pricing. Often you will need to build out both CPQ and a Pricing Calculator, with the former being more of a gold standard quoting system, and the latter being an agile sales and product tool. Figure 30 illustrates a (fairly) simplified representation of a google- doc based calculator. AJIT GHUMAN 110

Fig. 30: A Simple Pricing Calculator The simple calculator depiction shows that in order to price out a certain package, a sales rep needs only to take three simple steps to get to the price. Check off the packages and add-ons in question, enter the estimated quantity of the main pricing variable and then note down the itemized price for their selection. In most cases this can be really useful to provide a price range to prospects in the initial stages of a deal, followed later by using CPQ to formalize the process. In reality, the calculator won’t be so simple. You will likely have many more SKUs, add-ons and special conditions to abide by. Even so, I hope this provides a general idea of what the inputs and outputs should look like. PRICE TO SCALE 111 The internet will probably give you dozens of such examples, but what you should note are the following tips: 1. Make the calculator super simple to use: I’d be thousands of dollars richer if I had a buck for every time a sales rep wanted me to price out their deal for a specific situation. This is after I tried my best to simplify it as much as possible. Spend as much time cleaning up the UI of the calculator as you spend on the formulae and reference tables themselves. 2. Realize that it's a piece of software: As soon as you release a version of the calculator, you will start to get a lot of usage and your pricing or packaging may have small changes or errors caught as things proceed. You’ll need to set it up such that all your reps can always access the latest version of this software. Do not open up a single tab for everyone to use, do not commit to fixing every rep’s version either. The best process is to keep either a protected google sheet or a tab that cannot be modified by the reps, but can be routinely copied for pricing work. Then when you release an update, you will have to combine that with communication asking the reps to make new copies. 3. Don’t create long chain formulas: This is still related to #2, but important enough that I’m calling it out separately. Excel will let you create really intricate formulae, with arcane functions - don’t do it. Create simple formulae that refer to calculations from intermediate tables and sheets. Organize everything in a modular fashion because inevitably you will change the pricing or someone else will try to modify the calculator, and if it is too complex, it will introduce unnecessary headaches. Worse still, if an executive tries to understand it and can’t, they won’t trust the output -- believe me this happens far too often. Keep things modular and transparent. AJIT GHUMAN 112 CPQ Configure-Price-Quote (CPQ) refers to a system that allows a sales rep to configure a package, generate a pricing quote (including internal approvals on discounts, etc.) as well as the contractual paperwork for their deal in a seamless automated process, enabling fast deal closure with transparency, as well as keeping a record in the CRM of what exactly was sold and for how much. Another larger benefit is that it enables complete adherence to the pricing model. Because a software quoting implementation imposes guardrails on use cases and limitations to manually closed deals, it forces sales reps to strictly adhere to the pricing model deployed. Quoting Johnny Cheng: “My fundamental belief is that in order to do value selling, you need a lot of flexibility, a ton of flexibility. What ends up happen- ing in a model where if you introduce a lot of flexibility, is it comes with complexity. But complexity is a deal killer, it slows down deals, complexity makes it so that the reps can't defend the deal, they can't defend the price points, they can't understand why it's at this price point. And so in order to solve for that complexity and keep the flexibility, you have to introduce tools such as CPQ“. In practice however it is hard to implement well, and is something nearly every pricing leader I interviewed considers a headache or a challenge. In order to implement a CPQ solution, as the pricing leader, you will need to interface with your Sales Ops, Finance and Sales teams. In most cases such an implementation should be owned by the Ops team with heavy input from you on the pricing structure. Be warned however that your job here starts to mimic that of a software product manager and that requirements will have to be defined fairly granularly. You will need to produce documents that cover all of the following: PRICE TO SCALE 113 • How new deals will be priced • How upsells will be priced • Packages with add-ons and dependencies defined • What the discounting structure is • Whether older pricing books should be carried over • Policy regarding grandfathering older customers • Policy regarding overages in usage • The product data required for product usage monitoring • A process of introducing new products • Test cases to ensure correct outputs • Any inputs/edits on generating Order Forms or Statements of Work • Defined approval chains for non-standard deals • And more. Suffice to say this work somehow always tends to take 2-3x more time than you will estimate initially whether or not you have a consultant or an internal team building this out for you. This is so mostly because the scenarios that have to be built into this piece of software go beyond the pricing structure; they have to do with the day-to-day process (sometimes informal) of deal closure and in many cases highlights undefined policies for certain internal business processes. Keep this timeline in mind before committing a rollout timeframe to your leadership team. Beyond the pricing and process definition it is critical to involve some key friendly sales reps in the build phase. These reps can test to make sure the software is simple enough to use without unnec- essary complexity, confusion or friction. Many implementation teams scramble to get an implementation finished without sales in- volvement and call it a day with a basic sales training. Inevitably this will lead to some unexpected usability or use case issues cropping up that may limit sales adoption of the product. The worst thing after months of implementation would be for your sales team to rebel, AJIT GHUMAN 114 eschew the process and revert back to a totally manual way of selling — if this happens you will be left cleaning the mess on the other hand. There are a ton of resources online that offer best practices on CPQ implementation. One that I liked is a book on the topic, CPQ Implementation Guide by Marcin Krzych26. As a final note of personal opinion, fast growing companies where pricing structure may undergo evolution every other quarter, may not want to overinvest in this CPQ capability. Primarily because CPQ implementations take a long time, and by the time you have put something into product use, new requirements come up - sinking a lot of time and resources in this never ending process. At some point
>>>
