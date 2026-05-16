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
  "chunk_id": "chapter-07-step-4-chunk-003",
  "source": {
    "chapter_title": "Step 4",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/07 - Step 4.txt",
    "source_pages": "65-98",
    "char_start": 12183,
    "char_end": 19083,
    "checksum": "169f61cb49d6aa90"
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
Understanding_Student_Pref
erences_for_Postpaid_Mobile_Services_using_Conjoint_Analysis
AJIT GHUMAN
70
Figure 21 shows one “Task” given to the respondent, where they make
a choice between four profiles. It is possible, and often needed, to
present more than one task to the respondents if we need that
amount of analysis. For example, we may have follow up choice tasks
for Add-Ons or Top-Ups for each of the example plans in Figure 21.
Once we have the survey results, we can obtain a quantitative
measure, called a “preference score” or “partworth utility”, for each
attribute. Figure 22 shows an example of preference scores for
attributes and levels of the mobile phone plans under consideration.

Fig. 22: Utility Scores for a Mobile Phone Plan19
Using the preference scores derived from the survey responses, we
can simulate how the customers will express their choices for new
products and concepts that do not yet exist and forecast market
shares for multiple offerings in the market. We can also find out
which features and pricing provide a balance between value
perceived by the customer and what it would cost to bring those to
market. Figure 23 shows how different data amounts in the example
mobile plan will affect a company’s market share. For a more
comprehensive discussion of the conjoint simulator, I will refer you

19 Source: https://conjointly.com/guides/what-is-conjoint-analysis/
PRICE TO SCALE
71
to this content20 from Sawtooth Software. You can also try out a
simulation using a workbook21 from Conjoint.ly.
While the standard conjoint analysis was based on respondents
providing ratings for features or choices, the availability of
automated platforms and more capable respondent devices has led
to many types22 of conjoint analysis becoming prevalent, each with
its pros and cons. In practice, you can readily do enough conjoint
analysis to meet your needs with workbooks you create on your own.
With online surveys now par for the course, variations like Choice
Based (or Discrete Choice) Conjoint (CBC), Adaptive Choice Conjoint,
and Adaptive CBC (ACBC)  are what you could use for bigger groups
or complex analyses.

Fig. 23: Impact of Data Amount in a Mobile Plan on Market Share23
Later in this book you will read my interview with Jan Pasternak who
routinely uses this approach to weigh trade-offs between competing
packages for SaaS products. In a webinar on the topic of pricing
research methods, he shared some simplifying insights for the type
of inputs and outputs we can expect from conjoint analysis, as well

20 https://sawtoothsoftware.com/resources/technical-papers/introduction-to-
market-simulators-for-conjoint-analysis
21 https://conjointly.com/guides/conjoint-preference-share-simulator/
22 https://www.dobney.com/Conjoint/conjoint_flavours.htm
23 https://conjointly.com/guides/what-is-conjoint-analysis/
AJIT GHUMAN
72
as pros and cons of the approach. I am summarizing these insights
below.
SaaS Software Example
Figure 24 shows different package options for a fictional SaaS prod-
uct and how conjoint analysis helps to understand the customer
preferences/”take rate” as well as resulting revenue impact (normal-
ized) across the packages.
Here we can see that ‘Better’ and ‘Best’ packages have more takers
compared to ‘Good’ and ‘Best+’, with ‘Best’ garnering the highest revenue.

Fig. 24: Understanding Customer Preferences for a SaaS Product
(credit: Jan Pasternak)
Now we cover both the pros and cons of this approach so that we have
an understanding of when and when not to deploy this technique.
PRICE TO SCALE
73
Pros
Cons
Relatively Inexpensive: The
conjoint approach is suited for
scale and is relatively inexpensive
compared to in-person interviews.
(Those are covered in the next
section)

Flexible: One of the beauties of
the conjoint approach is that a
dataset can answer many different
business questions and what-if
scenarios. Even if your product
team is unable to deliver on a key
differentiator, you can simply re-
run the model with the feature
removed. This saves a lot of
heartache of re-doing surveys.

Accurate: Since the output of
conjoint analysis is often very
precise, it can help in making
recommendations to your CFO.
Large Sample Sizes Needed: This
approach requires a high volume
of responses, and this can be a
challenge because a typical
conjoint survey will take 2-3x
more time than the Van
Westendorp approach to take the
survey and requires some amount
of explaining of the product
features. (Approaches to get
enough samples can involve using
survey firms like Qualtrics for
~$100/survey or using in-house
demand generation with direct
offers of low priced Amazon gift
cards and finally expert networks
like GLG can be for specialized
personas such as CXOs.)

Mainly suited for simple products
and online/web sales motion:
Generally if the packaging
structure is too complex and not
published on the web, then it may
not be suited to be put in a
conjoint survey. If you think the
product needs to be explained in-
person then conjoint will not
work. Customers should be able to
understand the full value in a few
minutes.

AJIT GHUMAN
74
Qualitative Customer Research
Approach
In many cases, the above mentioned approaches of surveying
methodologies may not work well for complex and/or enterprise
products, as a prospect would require having a robust understanding
of the product, its features and benefits.
In such situations, we can revert to qualitative research approaches
involving directly interviewing customers in one-on-one settings.
In general we aim to interview a representative sample of our
customer/market base, which can be as few as 5-10 interviews to upto
40-50 interviews depending on the size of the pricing change as well
as size of the overall business and customer base.
For each interview, we will aim to probe both open-ended feedback
on product, packaging and pricing, as well as get the customer to
force rank features, benefits and pricing options. Below I provide a
suggested template24 that you can design your own customer
interview slide deck on.
Purpose
Slide
This is the first
slide of the deck,
meant to be a
context setter for
the discussion.
Here it is a brief
snapshot of the
product in
question with high
level benefits and
features.

24 You can download my template from here: http://bit.ly/qualitativetemplate
PRICE TO SCALE
75
This second slide
will then go into
the goals of what
we are looking for
in the discussion
and provide a
brief agenda.
Depending on how
you want to
sequence the
interview and the
areas you’d like to
probe you can now
start to ask
questions around
specific areas of
interest.

Here we are
forcing the client
to force-rank pre-
created pain point
statements, such
that we can
aggregate
responses across a
set of customers to
validate our
hypotheses. We
aren’t yet talking
about features as
the client doesn’t
understand the
product yet.
>>>
