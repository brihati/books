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
  "chunk_id": "chapter-07-step-4-chunk-006",
  "source": {
    "chapter_title": "Step 4",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/07 - Step 4.txt",
    "source_pages": "65-98",
    "char_start": 26282,
    "char_end": 30975,
    "checksum": "979e859a964cbbf7"
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

Fig. 28: Discovering the Link between Features and Unit Price Premium
Note that we are not looking to create a pricing model that fits
historical data, but only use historical data to get enough signals to
know whether list prices should be increased or decreased, and
whether new packaging can be created on the basis of features that
drive more value.
If in fact you are either changing your unit pricing variable, structure
and/or changing packages then I would still recommend combining
empirical data analysis with market/prospect research methods
described in the prior section.
PRICE TO SCALE
85
At this point we have the bulk of customer feedback based infor-
mation required to finalize our packaging and pricing approach. The
next sections cover some other practical areas (such as cost of
delivery, type of market and discounting) that need to be considered
before deciding that the price will be.
About ROI: Justification vs Price setting
There is an oft repeated ROI-based pricing sentence I’ve heard along
the years which goes something like “Mr Customer, I will aim to
deliver you 5x to 10x ROI and in return I only want [1% to 10%] of the
benefits accrued to you”. In theory this is an attractive approach,
customers can get the majority of the value delivered and we get a
small but proportional chunk of change for our value delivered.
This is theoretically very lucrative if the value proposition was actually
as strong as many companies suggest. A common mechanism by
which this is demonstrated is by doing a study with an external
consultant. Forrester’s Total Economic Index is one such example.
Let’s take a look at ROI claims across a few of these studies. Here
is a sampling of what a Google search throws up when I searched
for a well known report produced by Forrester known as Total
Economic Impact - TEI:
1. Snowflake: Forrester reveals a customer ROI of 612% and
total benefits of over $21 million over three years for
Snowflake’s cloud data platform.
2. New Relic: Forrester’s interview with an existing customer
and subsequent financial analysis found that the
interviewed organization experienced benefits of
$13,277,754 over three years versus costs of $6,047,192
adding up to a net present value (NPV) of $7,230,562 and
an ROI of 120%.
3. DataRobot: Forrester Total Economic Impact Study of
DataRobot: 514% ROI and Payback within 3 Months
AJIT GHUMAN
86
4. Snaplogic: Over a three year period, 498% ROI $3.9
Million Benefits Present Value $3.3 Million Net Present
Value ~6 Months Payback
5. Qualtrics: Forrester Consulting estimates the 3-year
benefit of Qualtrics experience management software at
$38.4 million – which is an ROI of 633%.
6. Twilio: $12.6 million in benefits versus costs of $3.3
million, resulting in a net present value (NPV) of $9.2
million and an ROI of 277%.
When  I look at these numbers, what comes to mind is an interview
I had with a CEO for a Marketing role, where he kept pushing me
to explain the difference between correlation and causation.
He was miffed about a phenomenon around how marketing
organizations take credit for everything a company did to be
successful where in reality the software was just one small piece.
What’s going on with these reports is something similar. One the
one hand they may not be able to isolate purely the impact of the
software in question and on the other hand, organizations cherry
pick their best customers to be used in these case studies.
This sentiment is echoed by Tomas Tunguz in his own blog, The
Siren Song of ROI Based Pricing25
“If we reflect on the most successful software companies, the very
largest, very few sell based on ROI. What is the return on investment
of a Salesforce or a Workday deployment? How do you calculate it?
How does an AE defend it?
Many times these ROI calculations assert unquestionable numbers.
But most buyers approach these kinds of arguments with skepticism
and even cynicism. Sometimes, they have been burned in the past
making kind of arguments.
>>>
