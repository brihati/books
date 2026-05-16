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
  "chunk_id": "chapter-16-interviews-case-studies-with-top-pricing-leaders-chunk-037",
  "source": {
    "chapter_title": "Interviews & Case Studies With Top Pricing Leaders",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/16 - Interviews Case Studies With Top Pricing Leaders.txt",
    "source_pages": "185-308",
    "char_start": 188242,
    "char_end": 195190,
    "checksum": "f23c4fc4d16ef1a6"
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
to build an economically
differentiated product at Coralogix.
Understanding the Market Dynamic
"Data is growing exponentially. It's simple: data grows faster than
revenue. Doesn't matter how much your company will grow; data will
outpace that," says Ariel Assaraf, CEO of Coralogix, highlighting a
critical issue in the observability sector. Traditional pricing models
in this space have struggled because these models create a sort of
fake NRR, as spend increases alongside the ballooning of data.
Ariel explains the paradox many companies face: "For observability
and security, the more data you have, the less you know. The more
you pay, the more inferior your performance gets." This challenge is

53 https://www.youtube.com/watch?v=S-Z_sqzg0-0
AJIT GHUMAN
298
compounded by the expensive and often sluggish processes of stor-
ing and indexing vast amounts of data.
Diving deeper into the issue, Ariel states, "In an environment dominated
by traditional storage and indexing methods, businesses find
themselves trapped in a cycle of escalating costs without corresponding
gains in insights or operational efficiencies. As data volumes grow,
systems become increasingly sluggish, turning what should be a
competitive advantage—data—into a cumbersome liability."
To combat these inefficiencies, Ariel shares Coralogix's innovative
approach: "We had to rethink our strategy from the ground up.
Instead of sticking to conventional data management practices, we
prioritized innovative solutions emphasizing data analysis over data
storage. This shift cuts down our storage costs and boosts our ability
to derive meaningful insights quickly and efficiently."
Coralogix’s Initial Market Realization
Initially, Coralogix attempted to create intelligence on top of existing
products. However, Ariel and his team quickly realized that
integrating into existing systems and adding value in a cost-effective
way for customers presented considerable challenges.
Recognizing these obstacles, Coralogix significantly pivoted at the
end of 2017. Ariel describes this period as a fresh start: "We had to
essentially restart the company from scratch, beginning of 2018 with
a small team and a clear focus." This new direction wasn't just about
survival but about rethinking how to deliver value in the observability
space—a sector dominated by established players and complex data
challenges.
"We restarted our journey in early 2018 with five people, no customers,
and no revenue," Ariel recounts. This moment was critical—it marked a
pivot that would redefine the company's trajectory.
PRICE TO SCALE
299
Pioneering a Pricing Revolution
"One of the key learnings from our initial years was the power of the
pricing page on your website. It's one of the most powerful messaging
pages," Ariel explains. In the highly competitive observability market,
where differentiation is challenging due to technical parity among
competitors, Coralogix opted to innovate through its pricing strategy.
When Coralogix first launched, the initial pricing strategy was a one-
size-fits-all model. Ariel and his team realized that traditional pricing
models did not cater effectively to the varying needs of their customers,
nor did they reflect the actual value delivered."In a landscape where
traditional storage and indexing methods dominate, businesses find
themselves trapped in a cycle of escalating costs without proportional
gains in insights or operational efficiencies. As data volumes grow, the
systems become increasingly sluggish, transforming what should be a
competitive advantage—data—into a cumbersome liability.
To address this, Coralogix introduced a flexible pricing model
aligned more closely with customer usage and the value they derived
from the service. "We moved away from a one-size-fits-all approach,
recognizing that each customer's needs are unique. By aligning our
pricing with the specific value customers gain from our platform, we
enhanced customer satisfaction and positioned ourselves distinc-
tively against our competitors."
"This flexibility became a game-changer in our growth trajectory,
significantly boosting our customer acquisition and retention rates,"
Ariel reflects on the impact of their innovative pricing.
The company’s current pricing model reflects the company's contin-
uous evolution and commitment to meeting customer needs through
flexible, transparent pricing. The model features a unit-based pricing
structure, where customers pay per gigabyte (GB) of data ingested,
with costs varying based on the type of data and its use case:
• Frequent Search: $1.15 per GB
• Monitoring: $0.50 per GB
• Compliance: $0.17 per GB
AJIT GHUMAN
300

Fig.1 : Coralogix’s Current Pricing as of 2024
This approach allows customers to choose any combination of these
categories, ensuring they only pay for the data they use, tailored to
their specific requirements. This pricing model maximizes data ROI
by acting as flexible currency, eliminating the need to commit to a
fixed amount of any data type, thereby ensuring cost control by
preventing overages or underutilization.
Ariel explains, "Our goal with the current pricing model is to provide
maximum flexibility and value to our customers. By allowing them to
mix and match logs, metrics, and traces across our data pipelines,
PRICE TO SCALE
301
we ensure consistent pricing regardless of how their needs shift."
This model supports a broad spectrum of customer needs, from
startups with minimal data requirements to large enterprises with
extensive data needs.
Innovative Approach: Analyze Before Indexing and
Aligning Technology with Pricing
Coralogix's strategy revolved around "analyze before index," a
methodology allowing significant cost reductions and efficiency
improvements. "We used to rely on the index for storage, but today,
we analyze about 70% of the data that goes through Coralogix without
storing it anywhere," Ariel notes. By analyzing data before storing it,
Coralogix significantly reduced storage costs while enhancing data
processing speed and relevance.
Ariel explains, "We realized that traditional data storage methods
were unsustainable. We needed to handle massive loads of data
without incurring prohibitive costs." The traditional approach of
indexing all incoming data increased storage expenses and slowed
down data retrieval and processing times, impacting overall system
performance.
"We had to rethink our strategy from the ground up. Instead of
sticking to conventional data management practices, we prioritized
innovative solutions emphasizing data analysis over data storage,"
Ariel explains.
To implement this, Coralogix implemented a multi-faceted product
strategy:54
1. Embedding Databases in Streams: By embedding a database
into each stream, Coralogix could process data in real-time,
only storing what was necessary. This approach ensured that
data was analyzed and actionable insights were generated
before any storage decisions were made.
>>>
