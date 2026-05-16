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

Chapter ID: chapter-12-usage-based-pricing

Chunk notes:
```json
[
  {
    "chunk_id": "chapter-12-usage-based-pricing-chunk-001",
    "source": {
      "chapter_title": "Usage Based Pricing",
      "char_end": 6257,
      "char_start": 0,
      "checksum": "3cb0a0d9805b7b3e",
      "source_pages": "159-164",
      "source_path": "/Users/sachin/books/files/Price to Scale/chapters/12 - Usage Based Pricing.txt"
    },
    "summary": "Usage Based Pricing (UBP) is often marketed as a panacea but requires careful consideration of market fit, product type, and revenue predictability. The author discusses three key learnings: market suitability, product type alignment, and the inherent revenue unpredictability UBP introduces compared to traditional subscription models.",
    "key_points": [
      "UBP sounds compelling but requires nuance in implementation that isn't obvious initially",
      "UBP is not appropriate for all companies and products despite positive industry coverage",
      "Market and customer expectations matter more than surface-level appeal of UBP",
      "Capability purchases with low usage are not suitable for UBP models",
      "UBP reduces revenue and valuation predictability compared to subscription models",
      "Tariff structures (linear, 2-part, 3-part) can provide revenue predictability within UBP"
    ],
    "arguments": [
      "UBP marketing sounds good but the underlying math and implementation are more complex than they appear",
      "Customer market expectations and industry norms constrain the viability of UBP adoption",
      "Products purchased as capabilities rather than consumption services are poor fits for UBP",
      "Revenue variability in UBP models means traditional SaaS valuation multiples cannot be directly applied",
      "Competitors adopting UBP can create FUD that leads companies to chase unsuitable pricing models"
    ],
    "examples": [
      "Snowflake achieves NRR rates of approximately 130% with UBP",
      "Kustomer's CEO was unable to innovate with pricing strategy because customer service software buyers expected $ per agent pricing",
      "Car purchases are capability-based despite infrequent usage; shifting to usage-based pricing would not work",
      "Salesforce app sellers are naturally compared to Salesforce's $ per user pricing model",
      "Data plans from Verizon and AT&T are usage-based pricing with set quantity purchases",
      "Snowflake reported degrading consumption patterns and lowered FY24 revenue growth outlook, causing 13% stock drop after hours"
    ],
    "stories": [
      "Author had to fight to roll back executives' grandiose UBP pitches that would have caused 50% revenue loss for their former product line",
      "Author personally experienced a competitor moving to UBP creating FUD in their company's executives, but customer analysis showed it was a capability purchase"
    ],
    "definitions": [
      "Usage-based pricing: paying based on a specific pricing metric that is related or specific to the use of the product",
      "Capability purchase: products bought as capabilities that are needed but not used frequently"
    ],
    "names": [
      "Janelle Teng",
      "Ajit Ghuman",
      "Dave Kellog",
      "Goldman Sachs"
    ],
    "dates": [
      "May 2023",
      "FY24 Q1"
    ],
    "numbers": [
      "130%",
      "13%",
      "50%"
    ],
    "places": [],
    "terms": [
      "Usage Based Pricing (UBP)",
      "Net Revenue Retention (NRR)",
      "Pricing metric",
      "Tariff structure",
      "Linear pricing",
      "2-part pricing",
      "3-part pricing",
      "Consumption model",
      "Subscription model",
      "Capability purchase",
      "Revenue predictability",
      "FUD (Fear, Uncertainty, Doubt)"
    ],
    "quotes": [
      "UBP can \"feel/sound\" very good. It markets very well.",
      "\"paying only for what you use,\" is a very compelling pitch when it comes to pricing",
      "companies with consumption models increased net new revenue faster than subscription peers",
      "Don't be this executive.",
      "\"Last week, cloud data infrastructure company Snowflake reported its FY24 Q1 earnings. While the company posted solid headline and bottom-line numbers that beat consensus expectations, it lowered FY24 revenue growth outlook for a second time within the last 2 quarters, causing the stock to tumble ~13% after hours\"",
      "\"Snowflake pointed to degrading consumption patterns and a lack of predictability of when headwinds might subside as key reasons for the revision\""
    ],
    "actionable_lessons": [
      "Have representative sample conversations with customers before making bold claims about pricing metric changes",
      "Analyze customer usage patterns before adopting UBP to ensure product type fits",
      "Do not adopt UBP simply because competitors do or to satisfy Industry Analysts",
      "Evaluate whether your product is a capability purchase or a consumption-based service before implementing UBP",
      "Understand that UBP introduces revenue variability that requires different valuation models than traditional SaaS"
    ],
    "open_questions": [
      "When exactly will AI disruption change traditional market categories' pricing expectations?",
      "To what extent will AI disrupt existing market categories and their pricing norms?",
      "What valuation models should be applied to usage-based companies if traditional SaaS multiples don't apply?"
    ]
  },
  {
    "chunk_id": "chapter-12-usage-based-pricing-chunk-002",
    "source": {
      "chapter_title": "Usage Based Pricing",
      "char_end": 9735,
      "char_start": 5557,
      "checksum": "2a0990ffd3eef852",
      "source_pages": "159-164",
      "source_path": "/Users/sachin/books/files/Price to Scale/chapters/12 - Usage Based Pricing.txt"
    },
    "summary": "Exploration of key learnings in usage-based pricing implementation, including valuation challenges, operational complexity, and sales compensation restructuring required for successful UBP adoption.",
    "key_points": [
      "Valuation multiples from subscription-based software cannot be directly applied to usage-based companies due to revenue variability and unpredictability",
      "Traditional SaaS metrics like ARR and MRR may not fit well with usage-based pricing models",
      "Operational implementation of UBP requires metering, CRM/CPQ/ERP/Billing system integration, and is significantly more complex in larger established organizations",
      "Sales compensation structures must be rethought for UBP with commission models based on account growth",
      "Sales forecasting becomes critical and difficult under UBP due to revenue unpredictability"
    ],
    "arguments": [
      "Variable revenue streams from UBP cannot support traditional subscription-based valuation models",
      "Operational complexity of UBP implementation is often underestimated by pricing consultants, VCs, and industry analysts",
      "Sales teams will not adopt UBP without clarity on compensation structure and payment timing"
    ],
    "examples": [
      "Snowflake lowered FY24 revenue growth outlook for a second time within 2 quarters, causing stock to tumble ~13% after hours, citing degrading consumption patterns and unpredictable headwinds"
    ],
    "stories": [
      "Author's experience launching UBP where enterprise sellers refused to surface UBP to buyers until sales compensation questions were clarified"
    ],
    "definitions": [
      "Trailing spend: a metric suggested for usage-based pricing models as alternative to traditional ARR and MRR"
    ],
    "names": [
      "Dave Kellogg",
      "Ajit Ghuman",
      "Snowflake",
      "Monetizely"
    ],
    "dates": [
      "2023-24",
      "2022"
    ],
    "numbers": [
      "13%",
      "4 months to 2 years",
      "2 quarters"
    ],
    "places": [],
    "terms": [
      "Usage-based pricing (UBP)",
      "ARR (Annual Recurring Revenue)",
      "MRR (Monthly Recurring Revenue)",
      "NRR (Net Revenue Retention)",
      "CAC (Customer Acquisition Cost)",
      "Valuation multiple",
      "Metering",
      "CPQ (Configure Price Quote)",
      "CRM (Customer Relationship Management)",
      "ERP (Enterprise Resource Planning)",
      "Feature flag",
      "PLG (Product-Led Growth)",
      "Consumption patterns"
    ],
    "quotes": [
      "degrading consumption patterns and a lack of predictability of when headwinds might subside",
      "the fundamental valuation model of subscription-based software will not directly apply to usage-based companies",
      "I really cannot overstate how complex this can get and the most ideal pricing strategy certainly is not the best for an organization"
    ],
    "actionable_lessons": [
      "When implementing UBP, ensure pricing metrics are metered across all customers with data flowing to CRM, CPQ, ERP and Billing systems",
      "Rethink sales compensation structures to include commission based on account growth when initial sale price is minimal under UBP",
      "Build sales forecasting models to support usage-based pricing motion",
      "Address sales compensation questions upfront before asking sellers to surface UBP to buyers",
      "Consider operational readiness and technology stack capabilities before committing to UBP as primary pricing strategy"
    ],
    "open_questions": [
      "How should companies adapt traditional SaaS metrics for usage-based pricing models?",
      "What valuation framework is most appropriate for usage-based software companies?",
      "How can organizations reduce the 4 months to 2 years implementation timeline for operational plumbing of UBP?"
    ]
  }
]
```
