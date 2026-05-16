Create a source-linked hierarchical chapter summary from these chunk notes.

Rules:
- Use only the notes below.
- Preserve the original sequence by chunk_id unless a thematic grouping is clearly better.
- Deduplicate repeated points.
- Keep concrete examples, stories, definitions, names, dates, numbers, places, terms, and short quotes.
- Keep examples attached to the idea they support.
- Do not invent missing details.
- If notes are incomplete, say which chunk_ids need extraction before a complete summary can be trusted.

Output:
1. Chapter title
2. Detailed chapter summary
3. Key points
4. Important examples and stories
5. Definitions and terms
6. Names, dates, numbers, and places
7. Short relevant quotes or standout statements
8. Actionable lessons
9. Source chunk IDs used

Chapter ID: chapter-06-step-3

Chunk notes:
```json
[
  {
    "chunk_id": "chapter-06-step-3-chunk-001",
    "source": {
      "chapter_title": "Step 3",
      "char_end": 6928,
      "char_start": 0,
      "checksum": "d79c8a3c8b3788a6",
      "source_pages": "43-47",
      "source_path": "/Users/sachin/books/files/Price to Scale/chapters/06 - Step 3.txt"
    },
    "summary": "Step 3 focuses on selecting a pricing metric as the most consequential decision in pricing strategy. It introduces two main approaches: Consumption-based pricing (per-seat and usage-based models) and Capability-based pricing (lump-sum offerings). A detailed checklist and real-life examples (Helpshift and Kustomer) illustrate how this decision impacts revenue capture and business growth.",
    "key_points": [
      "Selecting the pricing metric is the most consequential decision in the entire pricing exercise",
      "Getting the pricing metric right allows fine-tuning of other pricing model components; getting it wrong can slow sales velocity",
      "The goal is to charge customers proportionally to both company size and perceived value derived",
      "Two main pricing approaches exist at the highest level: Capability-based and Consumption-based pricing",
      "Consumption pricing includes per-seat and usage-based models",
      "Capability pricing is a lump-sum approach that doesn't allow for usage growth over time",
      "A structured checklist helps evaluate and rank candidate pricing metrics"
    ],
    "arguments": [
      "Seat-based pricing works well for foundational 'system of record' products like CRMs, HR, or Customer Support systems that are routinely used across departments",
      "Usage-based pricing can be more directly tied to the value a prospect receives and lead to easier client adoption",
      "Usage-based pricing is useful when there are hard costs that scale with usage (e.g., S3 storage, compute power)",
      "Capability pricing works well as add-on modules on top of a base platform utilizing consumption-based pricing"
    ],
    "examples": [
      "Amplitude charges per analytics event processed",
      "Google Drive charges on storage consumed",
      "Twilio charges per SMS sent",
      "Fraud detection companies charge based on the number of transactions processed",
      "Helpshift priced based on MAU (monthly active users) resulting in $240,000 annual ASP vs. $24,000 with seat-based pricing",
      "Kustomer retained seat-based pricing model like Zendesk incumbents"
    ],
    "stories": [
      "Helpshift case study: Company chose MAU-based pricing instead of per-seat pricing. A customer with 20 support agents at $100/month would be $24,000/year with seat pricing, but the same customer with 20 Million MAU paying $100 per 100,000 MAU resulted in $20,000/month or $240,000 annual ASP - a 10x revenue increase"
    ],
    "definitions": [
      "Consumption Pricing: Pricing that scales with actual units of usage or per-seat allocations",
      "Capability Pricing: Pricing a product as a lump-sum amount for the capability offered, which may be fixed or scale based on customer size",
      "Seat-based model: A way to size the client account by charging per user, allowing the brand to charge more from larger clients",
      "Usage-based model: Scales with the actual units of usage of a product"
    ],
    "names": [
      "Tien Tzuo",
      "Zuora CEO",
      "Brad Birnbaum",
      "Kustomer CEO"
    ],
    "dates": [],
    "numbers": [
      "20 agents",
      "$100 per month",
      "$24,000 annual deal price",
      "20 Million MAU",
      "$100 per 100,000 MAU",
      "$20,000 monthly price",
      "$240,000 annual ASP",
      "10x increase in revenue capture"
    ],
    "places": [],
    "terms": [
      "Pricing Metric",
      "Heuristic",
      "Consumption Pricing",
      "Capability Pricing",
      "Per Seat Pricing",
      "Usage-based Pricing",
      "MAU (Monthly Active Users)",
      "System of Record",
      "ASP (Annual Subscription Price)",
      "Hard Costs",
      "SaaS"
    ],
    "quotes": [
      "If you get it right, almost every other piece of your pricing model and operations can be fine tuned. If you get it wrong, you may not only waste the time taken in conducting this project but can significantly slow down sales velocity",
      "Subscribed"
    ],
    "actionable_lessons": [
      "Use the proposed checklist with six criteria to evaluate and rank candidate pricing metrics: tie to client value, fit for clients, measurability, predictability, diminishing or scaled costs, and deal economics",
      "For Capability pricing, the unit of pricing is per product or module; move to selecting the right price point",
      "For Consumption pricing, decide between traditional per-seat model or usage-based, then evaluate candidates against the checklist",
      "Consider whether your product's costs scale with usage (e.g., infrastructure vs. application layer) when selecting metrics",
      "Choose metrics that maximize revenue capture while meeting all other evaluation criteria"
    ],
    "open_questions": [
      "How should you decide between Consumption and Capability pricing for your specific product?",
      "What is the most appropriate usage metric for your product offering?",
      "Can your product be instrumented to easily measure a specific metric?"
    ]
  },
  {
    "chunk_id": "chapter-06-step-3-chunk-002",
    "source": {
      "chapter_title": "Step 3",
      "char_end": 12883,
      "char_start": 6460,
      "checksum": "b020c2189d4ea5e8",
      "source_pages": "47-64",
      "source_path": "/Users/sachin/books/files/Price to Scale/chapters/06 - Step 3.txt"
    },
    "summary": "Analysis of pricing metric changes at three established SaaS companies (Kustomer, Mixpanel, HubSpot) during their growth stages, showing how they adapted pricing models to better align with customer value perception and simplify sales processes.",
    "key_points": [
      "Second pricing metric achieved 10x increase in revenue capture",
      "Customers prefer repeatable, consistent pricing that maps to existing budgets over innovative but unfamiliar models",
      "Changing pricing metrics can reduce customer churn when bills no longer feel disproportionate to value",
      "Pricing metric changes enable faster sales cycles by reducing need for translation work",
      "Multi-product companies face friction when single metrics don't align across all products",
      "New pricing metrics must be tied to value, measurable, and predictable"
    ],
    "arguments": [
      "Customers in mid-market prefer familiar pricing models mapped to existing budgets rather than innovative consumption models",
      "Events-based pricing created misalignment between usage bills and perceived value as companies expanded use cases",
      "Contact-based pricing for Marketing Hub created friction when sales activity increased contacts unrelated to marketing value",
      "A customer's measure of success should be quality of leads (marketing-qualified contacts) rather than total database size"
    ],
    "examples": [
      "Helpshift achieved 10x revenue increase with second pricing metric",
      "Kustomer retained seat-based pricing model despite direct competition with Zendesk",
      "Mixpanel changed from Events to Monthly Tracked Users (MTUs) pricing",
      "HubSpot changed from Contacts to Marketing Contacts pricing metric",
      "HubSpot's CRM was free while Sales Hub was per-seat, creating inconsistent pricing philosophy"
    ],
    "stories": [
      "Kustomer wanted innovative consumption-based pricing but discovered customers wanted familiar, repeatable models mapping to existing budgets",
      "Mixpanel found Events metric became misaligned with customer value perception as company grew across use cases and industries",
      "HubSpot discovered sales activity in Sales Hub generated additional contacts that increased Marketing Hub subscription price without proportional marketing value"
    ],
    "definitions": [
      "Monthly Tracked Users (MTUs): Similar to MAUs, used by Mixpanel as pricing metric tied to value, measurable, and predictable",
      "Marketing Contacts: HubSpot's metric counting only contacts customers needed to interact with via email or ads, replacing total Contacts metric"
    ],
    "names": [
      "Brad Birnbaum",
      "Dharmesh Shah",
      "Kate Bueker",
      "Ajit Ghuman"
    ],
    "dates": [
      "2006",
      "2019",
      "2020",
      "Q3 and Q4"
    ],
    "numbers": [
      "10x",
      "$1 Billion",
      "1 Billion"
    ],
    "places": [
      "web-based support space",
      "mid-market"
    ],
    "terms": [
      "seat-based pricing",
      "consumption model",
      "pricing metric",
      "usage-based bills",
      "customer churn",
      "sales motion",
      "multi-product platform",
      "Events",
      "database size",
      "per-seat basis",
      "inbound marketing",
      "marketing automation"
    ],
    "quotes": [
      "10x increase in revenue capture with the second pricing metric",
      "they didn't want innovative pricing. They wanted repeatable, consistent pricing that mapped to the budget they already had in place",
      "they already had a budget in place, so they just said, 'Hey, we have X amount allocated for a solution'",
      "our customers didn't want a consumption model",
      "Reduced customer churn: As now customers wouldn't be saddled with paying disproportionately more compared to value derived",
      "Faster sales motion: Deals close faster as Sales don't have to play the role of translator",
      "A customer's measure of success isn't just how much they can grow their database, but how many leads in that database are worthy of nurturing",
      "Our marketing contacts pricing model allows customers to only pay for the contacts they want to market to via email or ads"
    ],
    "actionable_lessons": [
      "Test whether innovative pricing models align with customer budget constraints and familiarity before implementation",
      "Ensure pricing metrics remain aligned with customer value perception as company expands across use cases",
      "When expanding to multi-product offerings, reconsider whether single pricing metrics work consistently across all products",
      "Use pricing metrics that are tied to customer success and value outcomes rather than raw usage metrics",
      "Marketing Contacts model shows benefit of charging only for contacts customers actually intend to market to"
    ],
    "open_questions": [
      "What specific impact did Kustomer's pricing model have after Facebook's $1 billion acquisition in 2020?",
      "What were the exact metrics showing reduced churn and faster sales at Mixpanel after switching to MTU pricing?",
      "How did HubSpot's customer mix change quantitatively following the Marketing Contacts pricing transition?"
    ]
  },
  {
    "chunk_id": "chapter-06-step-3-chunk-003",
    "source": {
      "chapter_title": "Step 3",
      "char_end": 19312,
      "char_start": 12370,
      "checksum": "0db47bfb2cfd4859",
      "source_pages": "47-64",
      "source_path": "/Users/sachin/books/files/Price to Scale/chapters/06 - Step 3.txt"
    },
    "summary": "Explains three pricing structure models for consumption-based pricing: Linear Model, 2-Part Tariff, and 3-Part Tariff. Compares their pros and cons, discusses a hypothetical Pro Plan example, analyzes revenue implications, and introduces block pricing to provide volume discounts.",
    "key_points": [
      "Customer success measured by leads worthy of nurturing, not just database size",
      "Marketing contacts pricing model allows customers to pay only for contacts they market to",
      "Three main pricing structure options exist for consumption-based models",
      "Linear model simplifies but creates revenue unpredictability",
      "2-Part tariff is increasingly common and customers are accustomed to it",
      "3-Part tariff maximizes revenue capture if implemented by dominant market player",
      "Block pricing needed to provide volume discounts across all models",
      "Revenue charts show different predictability outcomes for each model"
    ],
    "arguments": [
      "Linear model reduces risk for clients by charging only for usage, increasing market penetration",
      "Linear model requires accurate instrumentation, increasing overhead costs",
      "2-Part tariff improves revenue predictability while enabling upside of greater usage",
      "2-Part tariff can lead to sawtooth edges creating pricing inconsistency",
      "3-Part tariff maximizes revenue capture according to academic research",
      "3-Part tariff incentivizes increased product usage",
      "3-Part tariff may cause buyer's remorse if customer needs change",
      "Block pricing needed to provide volume discounts within all models"
    ],
    "examples": [
      "Marketing automation product pricing with split between marketing and non-marketing contacts",
      "Nosto's pricing evolved from purely usage-based to include capability and platform pricing",
      "Oracle solved pricing for marketing automation when SMS sending created significant hard costs",
      "2-Part Tariff example: $10,000 + $0.40 per unit",
      "3-Part Tariff example: 5GB of data for $40/month, $0.10 for every MB afterward",
      "3-Part Tariff example: 100 seats for $10,000 per month and $150 per seat for additional seats",
      "Pro Plan Linear Model: $0.40 per unit",
      "Pro Plan 2-Part Tariff: $20,000 platform fee + $0.30 per unit",
      "Pro Plan 3-Part Tariff: $30,000 platform fee with 110,000 units included + $0.30 per additional unit",
      "Block pricing example with tiered rates: $0.40 per unit (0-100,000), $0.35 per unit (100,001-250,000), $0.30 per unit (250,001-500,000)"
    ],
    "stories": [
      "Team went back to drawing board on contact pricing after discovering customer success wasn't just about database growth"
    ],
    "definitions": [
      "Linear Model: charge a set unit price based on main pricing variable, per seat, per event",
      "2-Part Tariff: charge a base platform fee as setup price and add unit price",
      "3-Part Tariff: offer set number of units for base fee and overage fee on top; also known as cell phone plan model",
      "Block pricing: sub-levels within pricing models that provide volume discounts"
    ],
    "names": [
      "Nosto",
      "Oracle",
      "Ajit Ghuman"
    ],
    "dates": [],
    "numbers": [
      "5GB",
      "100 seats",
      "$10,000",
      "$150",
      "$0.40",
      "100,000",
      "$20,000",
      "$0.30",
      "110,000",
      "200,000",
      "$150,000",
      "$0.35",
      "250,000",
      "500,000",
      "100,001",
      "250,001"
    ],
    "places": [],
    "terms": [
      "consumption-based pricing",
      "marketing contacts pricing",
      "platform fee",
      "unit price",
      "overage fee",
      "sawtooth edges",
      "pricing inconsistency",
      "market penetration",
      "revenue predictability",
      "buyer's remorse",
      "churn",
      "volume discounts",
      "block pricing",
      "usage-based"
    ],
    "quotes": [
      "A customer's measure of success isn't just how much they can grow their database, but how many leads in that database are worthy of nurturing.",
      "Our marketing contacts pricing model allows customers to only pay for the contacts they want to market to via email or ads.",
      "bigger companies will want more predictable revenue",
      "it works only for a sub-set of customers with lower unit volume"
    ],
    "actionable_lessons": [
      "Segment pricing by whether leads are marketing-ready to charge customers appropriately",
      "Study Nosto and Oracle case studies to understand real pricing tradeoffs",
      "Use 2-Part tariff if seeking balance between revenue predictability and growth",
      "Use 3-Part tariff only if company is dominant or differentiated in market",
      "Implement block pricing to provide volume discounts within any pricing model",
      "Test pricing models against revenue charts to visualize impact at different usage levels",
      "Monitor where pricing models anchor larger customers negatively"
    ],
    "open_questions": [
      "How should block pricing be structured to work across wide swath of unit volume consumption?",
      "What is optimal number and structure of pricing tiers within block pricing?"
    ]
  },
  {
    "chunk_id": "chapter-06-step-3-chunk-004",
    "source": {
      "chapter_title": "Step 3",
      "char_end": 25212,
      "char_start": 19251,
      "checksum": "df42e1b1a7e2f918",
      "source_pages": "47-64",
      "source_path": "/Users/sachin/books/files/Price to Scale/chapters/06 - Step 3.txt"
    },
    "summary": "The chunk explains three pricing models with volume tiers (linear, 2-part, and 3-part), then introduces capability pricing for add-ons. It discusses trade-offs between revenue predictability and client adoption, and provides three methods for pricing add-on features.",
    "key_points": [
      "Linear model offers volume-based discounts with no platform fee",
      "2-Part model combines lower per-unit fees with graded platform fees for revenue predictability",
      "3-Part model includes larger unit bundles with overage fees to incentivize tier upgrades",
      "3-Part model eliminates sawtooth pricing edges and provides higher predictability and revenue",
      "Newer products face adoption challenges with 2-part and 3-part models",
      "Capability pricing is most suitable for add-ons rather than base software pricing",
      "Add-on pricing can be fixed, percentage-based, or percentage-based with min/max bounds"
    ],
    "arguments": [
      "2-Part model can be optimized to mirror Linear model while retaining guaranteed revenue from platform fees",
      "3-Part model provides the lowest possible price curve while incentivizing upgrades through overage pricing",
      "Capability pricing for base software leaves money on the table and dissuades enterprise adoption",
      "Percentage-of-base-fee add-on pricing may still be too cheap for small customers or too expensive for large ones",
      "Min/max bounded percentage pricing balances the benefits of proportional sizing without extreme price points"
    ],
    "examples": [
      "Basecamp pricing at flat $99/month independent of usage",
      "Linear model pricing: $0.40/unit (0-100,000 units), $0.35/unit (100,001-250,000), $0.30/unit (250,001-500,000)",
      "2-Part model with platform fee: $0.30/unit + $20,000 fee (0-100,000 units), $0.25/unit + $30,000 fee (100,001-250,000), $0.20/unit + $40,000 fee (250,001-500,000)",
      "3-Part model: 100,000 units with $35,000 tier fee and $0.45 overage rate (inferred $0.35/unit)",
      "Add-on pricing example: $5,000 fixed price, or 10% of $40,000 base ACV = $4,000"
    ],
    "stories": [],
    "definitions": [
      "Consumption based pricing model: predominant approach for base pricing in SaaS",
      "Capability pricing: charging a set amount for a piece of software capability",
      "Overage fee: charge per unit beyond included units in a tier, typically higher than inferred per-unit cost",
      "Platform fee: fixed recurring fee component in 2-part and 3-part models",
      "Add-on pricing: pricing for additional higher-end capabilities added to existing packages"
    ],
    "names": [
      "Basecamp",
      "Tom Tonguz"
    ],
    "dates": [],
    "numbers": [
      "100,000",
      "250,000",
      "500,000",
      "$0.40",
      "$0.35",
      "$0.30",
      "$0.25",
      "$0.20",
      "$20,000",
      "$30,000",
      "$40,000",
      "$35,000",
      "$75,000",
      "$125,000",
      "$0.45",
      "$99",
      "$5000",
      "$4000",
      "10%"
    ],
    "places": [],
    "terms": [
      "Linear model",
      "2-Part model",
      "3-Part model",
      "sawtooth edges",
      "unit range breakpoints",
      "platform fee",
      "consumption fees",
      "inferred $/unit fee",
      "overage fee",
      "tier fee",
      "included units",
      "capability pricing",
      "add-on pricing",
      "pay as you go",
      "ACV",
      "price-volume curves"
    ],
    "quotes": [
      "charging a set amount for a piece of software capability",
      "you are more likely not only to leave money on the table but actively dissuade enterprise adoption",
      "it would make your sales and sales operations teams go crazy with the complexity",
      "This is what we want. It gives us even higher predictability and more revenue"
    ],
    "actionable_lessons": [
      "For newer products, prefer linear pricing models for better client adoption",
      "For established products seeking revenue predictability, consider 2-part or 3-part models",
      "Use capability pricing primarily for add-ons rather than base pricing",
      "For add-ons, use percentage-of-base-fee pricing with min/max bounds to balance small and large customer pricing",
      "Price add-ons consistently to avoid complexity in sales operations",
      "Set overage prices higher than the inferred per-unit price to incentivize tier upgrades"
    ],
    "open_questions": [
      "How should you balance between revenue predictability and client adoption for your specific product maturity level?",
      "Which pricing model structure best fits your product's unique characteristics and market position?"
    ]
  }
]
```
