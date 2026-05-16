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
  "chapter_id": "chapter-13-how-to-optimize-your-pricing-in-the-face-of-chur",
  "chunk_id": "chapter-13-how-to-optimize-your-pricing-in-the-face-of-chur-chunk-002",
  "source": {
    "chapter_title": "How To Optimize Your Pricing in the Face of Churn & Inflation in SaaS",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/13 - How To Optimize Your Pricing in the Face of Churn Inflation in SaaS.txt",
    "source_pages": "165-174",
    "char_start": 5598,
    "char_end": 10317,
    "checksum": "7ff5c138264abb04"
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
41 https://www.saastr.com/the-new-normal-700-employees-at-200000000-in-arr/
PRICE TO SCALE
167
Median software NRR is now the lowest since 2020, see image below.
Here we see the other impact of increasing FCF, a close relook at
spend and thereby a concurrent impact on Churn and NRR.

Fig.4 :Median Retention Rate for the Software
AJIT GHUMAN
168
What we therefore observe is a double sided knife problem.
That,
1. Companies feel compelled to raise pricing to generate FCF
but
2. Reducing NRR is causing churn pressure where simple price
increases are unlikely to fly.
What options do you have then from a pricing and packaging
perspective?
Let us consider our options first from a packaging perspective: The
image below provides a set of packaging options from a one-size-fits
all model on the left to a completely a-la-carte option on the right.
If you’d like to generate more FCF, then what you really want to do is
to monetize areas of your product that there is a market demand for
that is currently not being well monetized. In that case you want to
move more to the right side of this spectrum. This means that if you
have a sort of GBB model, then you can consider creating more add-
ons that could be used to fulfill upsell motions.
In many cases there are already inefficiencies in packaging that can
help you here (we are not advocating you nickel-and-dime custom-
ers), where some capabilities were added to packages but actually
were valued by a smaller segment of customers but because they
were included in the packages, they had become blocked from being
upsells. Alternatively, you can consider using an a-la-carte option for
a sliver of your enterprise segment (i.e. where you see “whale” behav-
ior) and the act of custom scoping each deal across capabilities will
likely lead to an increase in Average Sales Prices/Average Deal Sizes.
In the 2021 environment, for growth you would have wanted more
simplicity to increase deal velocity but now in the 2024 environment
you may want to focus more on granular/flexible pricing to increase
deal sizes.
PRICE TO SCALE
169

Fig.5 : Packaging Strategies as Potential Solutions to Margin Pressure
At the same time if churn is an issue, then a defensive maneuver to
add a “lite” package option could help move customers to a lower
plan so as to not lose these customers completely. See table below.

Lite
Good
Better
Best

$9
$19
$29
$49
Feature X
X
X
X
X
Feature Y

X
X
X
Feature Z

X
X
Feature V

X
X
New Feature

X

Let us consider our options next from a pricing metric perspective:
1. Offloading non diminishing costs to the customer: Often-
times, companies offering some sort of a $/user cost will have
bundled in costs for high cost capabilities such as sending
AJIT GHUMAN
170
SMS messages or data storage or even high cost AI components.
Generally customers will be more accommodating to paying for
the underlying costs of things like SMS if a new cost-based
metric on $/SMS was created. Most companies offering an ad-
joining co-pilot may have a $/execution or $/completion metric
in addition to their $/user base platform fee. These tactics, if
well selected and accepted by customers, can help increase FCF
and protect margin.
2. Changing mis-aligned pricing metrics: In some cases (see
Mixpanel case study in this book), customers may want to
change their pricing metric if the current metric is cited as a
reason for customers’ churning. If the customers are billed
for their usage but the usage is not proportional to the growth
of their business (just a growth in usage), then there is a
broken link to ROI and the customer is likely to churn.
Increasing storage costs in infrastructure-as-a-service
players is one such way this happens. Metrics such as a
$/MAU or $/customer visits are more proportional to how
your clients win and could be better alignment vehicles
depending on context.
Only once packaging and pricing metric changes have been
considered should outright pricing metric changes be considered
(especially if they don’t provide any further value). See article by
Jason Lemkin42 where he says, “Incessant Price Increases on The
Base: They just keep going up and up and up. Especially unearned
price increases on the existing customer base. Same product, same
features, now priced higher. Many have raised prices every year the
past 3 years. We used to hesitate here, to keep NPS up. But if growth
has slowed to say 20%? Then a price increase is the simplest way to
hit the plan. On paper at least.  Raise prices for new customers?  At
least they get to choose.  Force annual pricing increases on existing
customers?  That’s something quite different.”

42 https://www.saastr.com/the-brut-sales-pltoo-many-are-running-today
>>>
