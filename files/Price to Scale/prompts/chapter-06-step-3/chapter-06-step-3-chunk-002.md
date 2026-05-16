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
  "chunk_id": "chapter-06-step-3-chunk-002",
  "source": {
    "chapter_title": "Step 3",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/06 - Step 3.txt",
    "source_pages": "47-64",
    "char_start": 6460,
    "char_end": 12883,
    "checksum": "b020c2189d4ea5e8"
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

“So pricing’s a really difficult
thing, right? It’s something that
we wrestled with in the earliest
days of Kustomer. We wanted
to be innovative. We quickly
learned as we started talking to
customers that they didn’t want
innovative pricing. They wanted
repeatable, consistent pricing
that mapped to the budget they
already had in place.
In 2020 Facebook acquired
Kustomer for $1 Billion. And
while we don’t have specific
information on the impact
on the pricing model. We do
know that Kustomer was able
to get a sizable chunk of
mid-market customers by
providing a superior product
that was significantly
differentiated from
incumbents but within a
familiar, predictable pricing
model.

8 https://tomtunguz.com/should-your-startup-differentiate-on-pricing/
AJIT GHUMAN
48

Now as we are going mid-
market and above, we’re mostly
replacing existing solutions,
whether it be Zendesk or
Salesforce. So they (customers)
already had a budget in place,
so they just said, “Hey, we have
X amount allocated for a
solution. Our solution is better,
it’s robust, it does more, but this
is the budget that we have.”

So they wanted a pricing model
that, frankly, mapped to the
way they’re accustomed to
doing business It was highly
predictable. So while we wanted
to think about doing a
consumption model here at
Kustomer, because we thought
that was innovative, we
realized our customers didn’t
want a consumption model.”

Established
Stage
Pricing
Evolution

Mixpanel
(longer case
study later
on in the
book)
In 2019, Mixpanel changed its
key pricing metric to Monthly
Tracked Users (MTUs) whereas
earlier they had used the
concept of Events for a long
period of their existence as an
analytics software provider.

They made the decision to
change their pricing metric
because the older metric of
‘Events’ while being very
measurable was no longer
fitting with client perception of
value as the company grew
across use cases and
industries. Some customers’
usage-based bills increased
substantially but they didn’t
feel they received
proportionate value. On the
other hand, their sales team
found it was hard to size up
While we don’t have hard
publicly available metrics on
impact, this change had a
bunch of cascading benefits
for the company:

1.
Reduced customer
churn: As now
customers wouldn’t
be saddled with
paying
disproportionately
more compared to
value derived.
2.
Faster sales motion:
Deals close faster as
Sales don’t have to
play the role of
translator and can
keep the discussion
focussed on value.

PRICE TO SCALE
49
new prospects and had to do
more work to translate from a
prospect’s actual value to the
company’s ‘event’ based
pricing.

They landed upon Monthly
Tracked Users (MTUs) (very
similar to MAUs in the last
example) that checked many of
the criteria I alluded to earlier:
tied to value, measurable,
predictable, and so on.
Established
Stage
Pricing
Evolution

Hubspot
Hubspot is a company that has
come to change the field of
marketing and has essentially
birthed the term ‘inbound
marketing’ around its set of
marketing automation
capabilities. While it initially
began with a single product
that priced based on the
number of contacts in their
Hubspot instance, the
company eventually made
other products that weren’t in
congruence with being priced
based on the number of
contacts. In 2020, Hubspot
made the change to its pricing
metric to ‘Marketing Contacts’
from the original ‘Contacts’
metric, removing the friction
that affected the company’s
ability to go to market with a
multi-product platform.

This medium post9 by its CTO
Dharmesh Shah explains the
evolution of its pricing model:

“In 2006, we were a single-
product company selling what
Hubspot’s pricing change is
too recent to know what the
impact is, but it's CFO’s
comment in its recent
quarterly earnings report
indicates that the company
expects a change in its
customer mix due to the
pricing change.

Kate Bueker A Chief
Financial Officer, HubSpot,
Inc10.
“And then over the course of
Q3 and Q4, what we saw is a
much more balanced set of
customer
additions, which is what sort
of leads me to the comments
that from one quarter to the
next, there's going to be
some difference in the kinds
of customers we add, as we
introduce different
functionality and make
pricing and
packaging changes.”

9 https://medium.com/swlh/marketing-contacts-pricing-lessons-38eef8301e95
10
https://ir.hubspot.com/hubfs/Q4%202020%20Earnings%20Call_Corrected%20Tra
nscript_2021-02-11-20-36-05.pdf
AJIT GHUMAN
50
we now call Marketing Hub...
Since then, we have added
HubSpot CRM, Sales Hub,
Service Hub, and CMS Hub to
our portfolio.

...Marketing Hub was billed on
a base price with included
contacts, and database size —
i.e. how many contacts were in
the database, which we felt
reflected the value they got
from our software.

When we transitioned into a
multi-product world, the
interaction between our
products started creating
pricing issues. HubSpot CRM is
free and Sales Hub is priced
on a per-seat basis. Not only
did our pricing philosophy
differ across Hubs, sales
activity would often generate
additional contacts that would
then raise the subscription
price of Marketing Hub,
whether or not those contacts
were valuable from a
marketing perspective. This
created friction and confusion
for customers. Our approach
had not been designed for a
multi-product world. As we
entered a new phase of growth,
it became apparent that we
needed a new strategy.

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
>>>
