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
  "chapter_id": "chapter-06-step-3",
  "chunk_id": "chapter-06-step-3-chunk-003",
  "source": {
    "chapter_title": "Step 3",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/06 - Step 3.txt",
    "source_pages": "47-64",
    "char_start": 12370,
    "char_end": 19312,
    "checksum": "0db47bfb2cfd4859"
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
When we went back to the
drawing board on contact
pricing…

A customer’s measure of
success isn’t just how much
they can grow their database,
but how many leads in that
database are worthy of
nurturing. Thus, the idea of
PRICE TO SCALE
51
splitting marketing contacts
out from non-marketing
contacts — and only charging
customers for the contacts
they needed to interact with —
was born.

Our marketing contacts
pricing model allows
customers to only pay for the
contacts they want to market to
via email or ads.”

Outside of these, you will find a lot more examples in the case study section of
the book. In my personal experience, it is the case studies that truly help
illustrate the tradeoffs involved and the sizable impact of this decision. In
particular, I recommend you read about how:
1.
Nosto’s pricing evolved from being purely usage-based initially to
include elements of capability and platform pricing.
2.
Oracle solved the problem of pricing for its marketing automation
product when a part of their product saw significant hard costs related
to sending SMS.
Once you have a hypothesis of your main pricing variable, you can
move on to setting the core pricing structure.
I will first discuss pricing structures for consumption based models
(which are far more complex) and then touch upon capability based
models.
AJIT GHUMAN
52
Pricing Structure for Consumption-
based Models
Roughly, you have three options11 to set the pricing structure:
1. Linear Model. You charge a set unit price based on your main
pricing variable, per seat, per event, etc.
2. 2-Part Tariff. You charge a base ‘platform fee’ as a setup price
and add the unit price. E.g. $10,000 + $0.40 per unit.
3. 3-Part Tariff. Also known as the cell phone plan model.
Where you offer a set number of units for a base fee and then
an overage fee on top of that. E.g. 5GB of data for $40/month,
$0.10 for every MB afterward (consumption model) or 100
seats for $10,000 per month and $150 per seat for every
additional seat.
Here are some pros/cons that will help you select between these options:

Pros
Cons
Linear
Model
1. Very simple to understand
and easy to tie into client
value with high
predictability of usage.

2. Helps increase market
penetration as it reduces
risk for clients, they only
pay for what they use. (see
Nosto case study)

1. What you gain in ability
for higher market share,
you lose in margin. This
model brings in
unpredictable revenue and
can leave money on the
table.

2. Such a model requires
accurate instrumentation
to be able to measure what
a client’s usage is at any
time and bill them for it,
thereby increasing
overhead.

11 https://tomtunguz.com/three-part-tariffs/

PRICE TO SCALE
53
2-
Part
Tariff
1. This structure will
improve on the revenue
unpredictability of the
linear model, while still
enabling the upside of
greater usage.

2. Increasingly the most
common structure.
Customers are
accustomed to buying
software in this model and
will not push back for the
most part.
1. When this structure is
implemented to drive
pricing models it can lead
to ‘sawtooth edges’ which
product pricing
inconsistency. We will
discuss further this in this
section.

2. It neither optimizes for
highest
revenue capture or highest
market penetration.
Depending on your intent,
the other two plans might
be a better fit.
3-
Part
Tariff
1. According to academic
research12, this structure
maximizes revenue
capture and even incents
increased product usage,
as long as it is
implemented by a
dominant or
differentiated market
player.

2. Revenue will tend to be
even more predictable
since the customer has
committed to the highest
likely usage.
1. This approach may not
work for competitively
weaker firms where buyers
may be wary of over
committing spend.

2. It requires a good fit with
prospect needs. There is a
chance of buyer’s remorse
if their needs change or
didn’t increase as
expected. Thus opening up
downgrade or even churn
conversations.

Taking this concept further, how do we think about our pricing
structure for a particular plan, “Pro”?

12
https://res.cloudinary.com/dzawgnnlr/image/upload/q_auto/f_auto/w_auto/SSRN-
id1587149.pdf
AJIT GHUMAN
54
Let’s do this step-by-step. First, we will create basic strawmen of the
three pricing structures.
• In the linear model, we’d basically have a fixed $ per unit
price.
• Subsequently, in the 2-Part model, we’d want to add a
component of an upfront platform fee with a lower $-per-unit
price. (The $-per-unit price will naturally be lower than the
linear model if we assume customers will only bear roughly
the same total price for their usage)
• Then finally, in the 3-Part model we want to further
incentivize an upfront purchase of a bunch of units such that
the $-per-unit price is discounted because of the upfront
purchase and the overage fee is greater to ensure the
selection of the package.
The following table is a hypothetical example.

Linear Model
2-Part Tariff
3-Part Tariff
Pro Plan
$0.40 per unit
$20,000
Platform fee +
$0.30 per unit
$30,000
Platform fee
with 110,000
units included
+ $0.30 per
additional unit
Now let’s visualize side-by-side the resulting revenue chart (Figure
15) obtained by deploying these three models.
PRICE TO SCALE
55
`

Fig. 15: Comparison of Linear, 2-Part, and 3-Part Tariff Models
The linear model certainly looks fair on a plot. In reality, the revenue
is subject to consumption in any given time period and if a customer
reduces their consumption for any reason, so will your overall
revenue. While this can still work for a new entrant to a market by
providing no upfront fee and “pay only for what you use”, bigger
companies will want more predictable revenue. (See Nosto case study
later in the book).
Now let’s analyze the 2-Part and 3-Part models in relation to the
linear model.
1. The 2-Part tariff model introduces a platform fee to solve the
drawback of the linear model’s uncertain revenue but might
anchor down larger customers as the unit price increases
above 200,000. Furthermore, if a customer is going to pay
something like $150,000, then a guaranteed revenue of
$20,000 does not provide revenue predictability.
AJIT GHUMAN
56
2. The 3-Part tariff model can further provide a greater fixed
revenue but in its current avatar, it leads to a steep jump in
price as soon as a customer enters into overages.
Consequently, it works only for a sub-set of customers with
lower unit volume. We really need this model to work across
a wide swath of unit volume consumption.
3. Finally, in all models, we have straight lines that do not
inherently offer a way to provide “volume discounts”, which
are expected in almost every type of consumption pricing
model.
Therefore, for all three models, what we need are sub-levels (known
in industry parlance as “blocks/block pricing”) within our models.
Here is what they could look like:
Linear Model
To
From
$/Unit Fee

0
100,000
$0.40

100,001
250,000
$0.35

250,001
500,000
$0.30
>>>
