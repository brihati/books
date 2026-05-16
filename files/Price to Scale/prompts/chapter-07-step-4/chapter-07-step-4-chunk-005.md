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
  "chapter_id": "chapter-07-step-4",
  "chunk_id": "chapter-07-step-4-chunk-005",
  "source": {
    "chapter_title": "Step 4",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/07 - Step 4.txt",
    "source_pages": "65-98",
    "char_start": 23746,
    "char_end": 26982,
    "checksum": "9ad1d5d51bc3e736"
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
Then rank order this list such that you can plot a chart that
looks something like the one in Figure 26. (This exercise can be done
for either your entire customer base or just for a given tier/package)
AJIT GHUMAN
82
What we are trying to understand is:
• How much does the market really bear for this product?
• How much are we discounting?
• And, can we identify customer segments by looking at the
data that might have more price elasticity than others?
In this hypothetical example we assume our company has sold 10
customers so far on the product we are trying to price. We can
further label clients based on their consumed unit volume of our
product (assuming that was our key pricing metric)

Fig. 26: Understanding Your Customer Using Existing Pricing Data
What does the data show?
We can see that Large customers tend to pay 2-10x more than Small
customers. In this chart we can see that in some cases the company
is selling at prices higher than the list price, i.e. negative discounting.
We can also see that list prices are 30% to 50% higher than actual
per account ARR for Large customers.
PRICE TO SCALE
83
In general, in B2B software, one can expect commercial (i.e. smaller)
deal discounting to be upto 20% and for enterprise (i.e. your larger
customers) deal discounting to be upto 80%. Here we can clearly see
that we likely need to increase list prices to get into a positive
discounting range for smaller deals and while discounting for larger
customers seem to be in line.
Another instructive chart to look at for the same data set is to look at
unit pricing i.e. ACV divided by unit volume. In the chart in Figure
27, we can see a reduction in unit price as deal sizes become bigger.
Larger customers pay around $0.60 per unit but smaller customers
pay around $2.10 per unit. This is perfectly acceptable in SaaS
pricing as customers expect to get a ‘volume discount’ if they are
using more of the service or buying more licenses/seats, etc. What
this does help us with is give us our current ‘price points' across
different segments. If our sales motion was largely priced ad-hoc,
now we have more data around which price points our packages will
need to be close to, in order to work. However, if you plan to change
your key pricing variable, pricing structure or introduce new
customer segments, then don’t make the mistake of extrapolating
this data since it is derived from a sales motion with certain defining
pricing assumptions and customer segments.

Fig. 27: Unit Prices Versus Deal Size
AJIT GHUMAN
84
While the charts in Figures 26 and 27 helped more in understanding
the price point across segments, we can also do analysis to help
validate our packaging approach. What we can do now is to pick 5-7
critical features and see how the usage of these features align with
our customers.
Can we find a pattern in the data that some customers pay a unit
price premium when most of the features are used? In the example
in Figure 28 we can see that while Feature 1 and 2 are used by all
customers, features 4 and 5 are used more often by larger customers
with higher ACVs, but not at all my smaller customers. In a packaging
exercise, we now know to introduce these features only to our higher
end packages.
>>>
