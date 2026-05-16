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
  "chunk_id": "chapter-07-step-4-chunk-001",
  "source": {
    "chapter_title": "Step 4",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/07 - Step 4.txt",
    "source_pages": "65-98",
    "char_start": 0,
    "char_end": 6913,
    "checksum": "ec752c4bd9fa66db"
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
61

STEP 4
Rate Setting

So far all we’ve done is built the foundations for the operations of
pricing. We haven’t yet determined how much to charge.
Recall our work in the previous chapter around packaging. Each of
our packages caters to a specific customer segment. We will now
cover how to find the right price for a given segment<>package and
the process can then be repeated across different segments.
What you end up charging for your product will be a function of the
following:
1. Prospect Willingness To Pay (WTP)
2. Competitive & Category Price Points
3. Your Cost of Delivery
4. Discounting For Procurement
5. Your Pricing Strategy
Let’s cover each of these starting with the WTP of our customers/
prospects.
Prospect Willingness To Pay (WTP)
Let us first start with trying to understand how to figure what our
prospects will be willing to pay for our product.
Note that to understand which tactic to deploy in order to find the
WTP, it is helpful to understand which one of the following two
camps you fall into:
AJIT GHUMAN
62
1. You lack market feedback: You are pricing a brand new
product OR you are selling an existing product to a brand
new customer segment.
2. You have some market feedback: You are moving from ad-
hoc pricing to more scalable, predictable pricing.
When You Lack Market Feedback
If you lack market feedback, then essentially you have two tools at
your disposal to elicit your prospect’s WTP.
1. You can conduct a survey in which solicit a price range feedback
based on the package you’ve designed for the target segment.
2. You can run a conjoint analysis that will help you refine the
features included in your package and the associated price
point of the package.
3. You can do in-person prospect interviews. If you are selling
a complex, enterprise B2B SaaS product then you may be
better served to do live customer pitch+feedback sessions.
Surveys
You can use surveys to illicit a given customer’s range of acceptable
prices.
Let’s see the example of a basic pricing survey and then the more
well known upgrade to the basic survey called the Van Westendorp
Analysis. While the latter is more popular, I personally find the basic
survey to be far easier to understand with clearer tradeoffs. I will
explain in the following two sections.
Basic Pricing Survey
For a basic pricing survey, the two questions used to anchor responses
are along the following lines:
1. At what point will the product be so expensive that you would
not consider buying it?
PRICE TO SCALE
63
2. At what point would you think the product is priced so low
that you would doubt its quality?
Note that it usually doesn’t work to ask a customer how much they’d
pay for a given product because the answers may get actively biased
too low if the customer feels they can influence the price of the
product. It is also the case that without reference points, a singular
price point answer may not be very revelatory as the customer
essentially is just guessing at that point.
The survey questionnaire itself should ideally be structured so that
first you can explain the context or product category you will query
the customer about and then provide context on the specific product
itself. By anchoring the customer in the type of solution (say CRM
software) you are setting the right context of the decision. It would be
fair to take through an explanation of the product with your product’s
purported value proposition so that the survey takers can
appropriately think about the value of the product to them.
If you were to run a survey just with the two questions above to a
representative population, you can then collate the results in a set of
tables which follow:
Note: For conducting the survey I would simplify the pricing structure
discussed earlier into a linear $ per unit. The 2-part or 3-part tariff
would simply get too complex to describe in a survey and can be
eventually backed into.
AJIT GHUMAN
64
Table 1

Table 2

Table 3

Table 1 contains the frequency distribution by which respondents
selected different price points being too low for the product to be of
high quality. The cumulative percentage column is then helpful to
find out, for how many people is a specific price not too low? In this
example. 75% of people think $40 per unit is not too low of a price
for this product. Table 2 does essentially the reverse of this. In the
example, 50% of people think $70 per unit price is too high.
These two tables can then be combined into Table 3 to find out the
% of people for which a given price is neither too low nor too high.
We observe a maxima at $50 at which point 85% of people think the
PRICE TO SCALE
65
price is neither too low nor too high, i.e. that they would be willing to
pay this price for the product. This is also called the Optimal Price
Point (OPP). (Note that the OPP is a singular price point and that this
analysis doesn’t necessarily help us create a reasonable price point
range, this is what the Van Westendorp approach will cover. Finally,
whether or not you price at the OPP will be your personal decision
taking into account costs, as well as strategic intent, i.e. optimize more
market share vs optimize for margin).
Van Westendorp Analysis
An alternative version of the basic pricing survey is the Van
Westendorp Price Sensitivity Analysis. The aim is to establish price
perceptions for a product in a market. Respondents are asked four
questions to determine what prices are too cheap, where a price is a
bargain, when a price is high and where a price is too expensive. By
plotting the cumulative curves for each of the four prices, the crossing
points are deemed to be optimum points according to different
criteria. The resultant price "space/range" helps to determine the
range of acceptable prices - and so pricing tactics - available.
This can easily be done in a spreadsheet, by first converting survey
data in cumulative percentages, then inverting two of the question
datasets and then using the histogram function to plot the curve. This
is a good article that describes this process in general:
https://www.dummies.com/software/microsoft-office/excel/excel-
dashboards-add-a-cumulative-percent-series-to-your-histogram/
When done you will get a chart that looks like the one in Figure 19.
It essentially shows a range of acceptable prices. The point of
intersection where the same number of people think the product is
Too Cheap and Not A Bargain, indicates a price of marginal
cheapness (PMC) - i.e. any lesser in price and a greater proportion
of people will find the product to be too cheap. The point of
intersection where the same number of people think the product is
Too Expensive and Not Expensive, indicates a price of marginal
expensiveness (PME) - i.e. any higher in price and a greater
AJIT GHUMAN
66
proportion of people will find the product to be too expensive.
Essentially giving us some reasonable bounds to play inside.
>>>
