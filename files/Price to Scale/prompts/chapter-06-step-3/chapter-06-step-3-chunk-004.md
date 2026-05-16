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
  "chunk_id": "chapter-06-step-3-chunk-004",
  "source": {
    "chapter_title": "Step 3",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/06 - Step 3.txt",
    "source_pages": "47-64",
    "char_start": 19251,
    "char_end": 25212,
    "checksum": "df42e1b1a7e2f918"
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
0
100,000
$0.40

100,001
250,000
$0.35

250,001
500,000
$0.30

Here we introduce different pricing for different unit volume ranges,
and the prices are lower at higher volume ranges as one would expect
(allowing for volume based discounts). Note that this pricing is still “pay
as you go” with no platform fee included.
2-Part Model
To
From
$/Unit Fee
Platform Fee
0
100,000
$0.30
20,000
100,001
250,000
$0.25
30,000
250,001
500,000
$0.20
40,000
We introduce similar sub-levels in the 2-Part structure, and here provide
lower $/unit consumption fees but introduce graded platform fees to
provide revenue predictability. This is one of the most common pricing
structures being used in SaaS today.
PRICE TO SCALE
57
3-Part Model
Included Units
Tier Fee
Overage $/unit
(Inferred $/unit)
100,000
35,000
$0.45
$0.35
250,000
75,000
$0.40
$0.30
500,000
125,000
$0.35
$0.25
In the 3-Part structure, we again create further levels with higher
tier/platform fees with a sizable chunk of units included in the price.
Further, we keep an overage fee that is higher than the $/unit inferred
fee at the top end of the units included. For example at 100,000 units for
$35,000 the inferred price is 35 cents per unit but the overage price is 45
cents. This is done to incentivize movement into a fixed bundle as
otherwise clients may choose to just pay as they go.
When we plot out the price chart for the models above we see the
chart in Figure 16. With our fix we now have better looking price-
volume curves that can capture increasing value for the two and
three part models as the price increases.
Note the jagged saw-tooth edges at the unit range breakpoints for
both the linear and 2-part models, that is expected and is a feature
of these models. When implemented in the real world we usually try
to optimize the numbers to reduce these edges but some of the price
jumps or increases at these breakpoints will remain.
Note that we are able to model our Two-part price curve to be very
similar to the Linear model while retaining the advantages of
guaranteed revenue through the platform fee. The price at every new
unit volume range in the two-part model is actually the minimum
price at that range, providing us more predictability overall.
Finally, the Three-part model does not suffer from the sawtooth
problem at all. The price curve in this model is the lowest price
possible while including overage payments such that there will be a
point at which it will make more economic sense for a prospect to
AJIT GHUMAN
58
select a higher tier/bundle. This is what we want. It gives us even
higher predictability and more revenue as per academic research.
The counter consideration to predictable revenue is client adoption.
If your product is newer then clients are less likely to opt for a 3-part
model and much more likely to adopt a linear model.
At the end of the day, it is your decision on which structure to
implement. But my hope is that this gives you a sense of the pros and
cons involved in this decision.

Fig. 16: Price Chart with Sub-Levels
So where are we now?
We have understood the selection of the key pricing variable and a
supporting pricing structure for a consumption based pricing model,
the predominant approach for base pricing in SaaS.
Before we move on, let’s take a look at capability pricing models.
PRICE TO SCALE
59
Capability price is as defined, charging a set amount for a piece of
software capability. A great example is Basecamp’s pricing13 at a flat
$99/month independent of usage. Now I would argue that in general,
this pricing approach isn’t the best for the base software, since you
are more likely not only to leave money on the table but actively
dissuade enterprise adoption. (The reason for the latter is best
described on Tom Tonguz’s blog14)
Where it does make a lot of sense, and where capability pricing
shows up a lot is for add-on pricing. Let’s say you want to add a
specific piece of higher-end capability to your existing packages. Now
for pricing these add-on features, you really don’t want to create a
whole other pricing variable for consumption pricing. In my
experience, it would make your sales and sales operations teams go
crazy with the complexity. This is where a capability pricing approach
really helps (see Figure 17).

Fig 17: Add-On Capability Pricing
Now even though it is a lump-sum amount it still need not be a fixed
price. Some add-ons can be priced as a percentage of the base fee
(this enables the add-on price to scale with the size of the customer)
and others can be a fixed fee (see Figure 18).

13 https://basecamp.com/pricing
14 https://tomtunguz.com/obscure-economic-concept-behind-saas-pricing-
challenges/
AJIT GHUMAN
60

Fig. 18: Add-On Capability Pricing as Percentage of Base Price
Taking this forward, capability pricing for add-ons can basically be
done in three ways:
1. Create a fixed price structure for your add-ons. For example,
just say that this add-on is $5000 and call it a day. This isn’t
very methodical, and if this is a strategic add-on, then it limits
your revenue potential for large customers, and it may even
seem too expensive for small customers.
2. Create a % of base fee structure for your add-ons. In this
case, you can say the add-on is 10% of base ACV. For our
example, it would work out to $4000. This is actually better
and the price is proportional to the size of your customer.
Even still if this feature has a high cost to deliver, it may yet
become cheap for smaller customers. Alternatively, for your
largest customers, it could seem too expensive.
3. Create a % of base fee structure with a min and max. In this
approach, you essentially have the benefits of option #2, with
a minimum and maximum price to bound the price range so
as not to make it too cheap or too expensive.
At this point you should have enough information to decide on your
hypothesis of a) your key pricing variable(s) and b) a pricing
structure for each of your product tiers.
>>>
