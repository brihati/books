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
  "chunk_id": "chapter-06-step-3-chunk-001",
  "source": {
    "chapter_title": "Step 3",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/06 - Step 3.txt",
    "source_pages": "47-64",
    "char_start": 0,
    "char_end": 6928,
    "checksum": "d79c8a3c8b3788a6"
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
43

STEP 3
Pricing Metric

Selecting your key pricing variable is perhaps the most consequen-
tial decision you will make in your entire pricing and packaging
exercise. If you get it right, almost every other piece of your pricing
model and operations can be fine tuned. If you get it wrong, you may
not only waste the time taken in conducting this project but can
significantly slow down sales velocity and introduce completely
unneeded friction in the sales engine.
At the end of the day the goal for pricing is to find a way to charge
your customer based on a heuristic that allows a) You to obtain
revenue for your product that maximizes the return from the market
(i.e. larger companies are able to pay more) b) Your client to pay a
price that is proportional to the value perceived to be derived by them.
There are many ways to think about this variable, including pricing
on usage, license, seat, cost, and so on. As mentioned by Zuora’s CEO
Tien Tzuo in his book Subscribed7, I’ve found it very clarifying to look
at two main approaches at the highest level as Capability and
Consumption based pricing (see Figure 14). (The simplifying caveat
here is we assume subscription based pricing models.)

7 https://www.amazon.com/Subscribed-Subscription-Model-Companys-
Future/dp/0525536469
AJIT GHUMAN
44

Fig. 14: Consumption and Capability based Pricing
1. Consumption Pricing includes both traditional per seat
based pricing models, as well as usage-based pricing models
that are prevalent in newer SaaS products in the market
today.
− The seat-based model is essentially a way to ‘size’ the
client account. The ‘per seat’ allows the brand to
charge more from larger clients, with a sort of im-
plicit assumption that value-derived also scales
proportionately. This approach works well when the
product is a more foundational ‘system of record’ to
an organization’s technology stack, such as a CRM,
HR, or Customer Support system that is going to be
routinely used by various departments as a way to run
the business. There is unlikely to be one key unit of
activity that can easily be distilled into a usage
parameter.
− The usage-based model scales with the actual units of
usage of a product. For e.g. Amplitude charges per
analytics event processed, Google Drive charges on
storage consumed. Twilio charges per SMS sent.
Some fraud detection companies charge based on the
number of transactions processed. Usage-based
PRICE TO SCALE
45
pricing is used for a number of reasons. Depending on
the chosen metric, it can be more directly tied to the
value a prospect receives from the product and thereby
lead to easier client adoption. It can also be useful when
there are hard costs that scale with usage, think S3 stor-
age or compute power (more often in the infrastructure
layer vs. the application layer). Finally, this approach is
easier to adopt when the usage of the product is actually
measurable across customers.
2. Capability Pricing refers to pricing a product as a lump-sum
amount for the capability offered. This could be a fixed price
or a price that scales based on the size of the customer. Since
it is a lump-sum model, this approach doesn’t really allow for
usage growth over time and is more akin to paying for a fixed
piece of hardware or set capability. While it would definitely
play well in a hardware setting, it also tends to work well for
add-on modules that sit on top of a base platform that utilizes
a consumption-based pricing model.
Given this information, how do you decide on your main pricing
metric/variable?
Here is a proposed checklist:
1. Decide the larger model - Consumption or Capability.
2. If Capability, then the unit of pricing is per product or module
and you can move on selecting the right price point. The next
section explains how to do just that.
3. If Consumption, then you need a way to decide what your key
metric will actually be. Will it be a traditional per-seat model?
Or will it be based on usage? If it is usage, then what is the
metric of usage? I propose that you come up with a few
candidates and then rank/assess them with the following list:
a) Tie to client value: Is the metric proportional to client
value? And to what extent?
AJIT GHUMAN
46
b) Fits for clients: Will clients perceive it to fit with the
value they derive?
c) Measurable: Can you instrument your product so that
the metric is easily measurable?
d) Predictable: Can clients estimate how much they will
spend with this metric? If the metric isn’t predictable
then clients could be hit by unexpected bills that
could take them by surprise.
e) Diminishing or Scaled Costs: As your metric
increases, do your costs level out, or do they scale with
usage? Sometimes there may not be much choice in
the matter but this is important to note as the subse-
quent decisions on pricing structure, price point, and
discounting will be critical in case costs increase
steadily with consumption.
f) Deal Economics: Does this model help you create a
workable sales engine? There can always be two
different metrics that check all the above boxes but
differ considerably in the resulting revenue and mar-
gin you accrue for each deal. Everything else being
equal, you’d want to maximize revenue capture.
Now let me illustrate how this decision can have a meaningful impact
with a few real-life examples:
Company
Pricing Metric Decision
Impact
Early Stage
Pricing

Helpshift
Helpshift is a customer service
software platform that
originally grew due to its focus
on solving mobile customer
support use cases.

Earlier on, the company had to
make a decision on how to
price its platform. Had the
company used the industry-
standard approach of
implementing per-seat pricing,
Selling to a company with a
support team of 20 agents at
$100 per month would only
work out to a $24,000 annual
deal price.

But the same company could
have 20 Million MAU and be
willing to pay $100 per
100,000 MAU. Leading to a
monthly price of $20,000 and
an annual ASP of $240,000.
PRICE TO SCALE
47
it would have significantly
hampered its growth since
there are not a lot of support
agents in many companies
offering mobile applications,
while at the same time these
apps support tens of millions
of users.

The company chose to price
based on the number of MAU
(monthly active users) and was
able to convince the key
‘Product Manager’ persona
that this price was justifiable
and tied to value since MAU
was how these products were
already being managed.

This was a 10x increase in
revenue capture with the
second pricing metric!!

Early Stage
Pricing

Kustomer
Kustomer is another provider
in the customer service space.
Unlike Helpshift, it made a
decision to retain a seat-based
pricing model as followed by
incumbents such as Zendesk.
Do note that Kustomer in some
cases directly competed with
Zendesk in the web-based
support space.

Kustomer’s CEO, Brad
Birnbaum, shared his thoughts
on pricing on a Saastr
podcast8:.
>>>
