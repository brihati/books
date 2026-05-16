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
  "chunk_id": "chapter-07-step-4-chunk-002",
  "source": {
    "chapter_title": "Step 4",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/07 - Step 4.txt",
    "source_pages": "65-98",
    "char_start": 6213,
    "char_end": 12883,
    "checksum": "73b1bf4f307e27ca"
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
l get a chart that looks like the one in Figure 19.
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

Fig. 19: Van Westendorp Analysis15
But this approach still has some issues. The analysis looks rigorous
but is more suited for easily explainable (e.g. cpg) products where
price and quality are strongly linked. This isn’t always the case for
software, and while the VW method gives us price ranges they have
nothing to do with competitive prices or even one’s own margin.
Finally, the dataset is a function of the respondents, and designing a
survey at the outset to be representative of your eventual market may
be difficult, in which case it is possible the bounds you see here could
have more give on the higher side, allowing you to increase the price.
All this means is that this should definitely be a tool in your toolkit
but that it provides us with a directional guidance that should be
combined with your initial hypothesis, qualitative interviews as well
as strategic intent to arrive at the right price point for your
company/product.

15 Source: https://www.5circles.com/van-westendorp-pricing-the-price-sensitivity-
meter/
PRICE TO SCALE
67
While the Van Westendorp analysis gives us more clarity than a
simpler pricing survey, neither approach let’s us estimate the relative
value of different features or capabilities. To answer this, the conjoint
approach offers us some more options.
Conjoint Analysis
Conjoint analysis is a powerful survey-based research technique that
helps determine how people value different attributes (feature,
function, benefits) that make up an individual product or service.
The objective of conjoint analysis is to determine what combination
of a limited number of attributes (for example, a tier or bundle) has
the most influence on respondent choice or decision making.
A controlled set of potential products or services is shown to survey
respondents and by analyzing how they make choices among these
products, the implicit valuation of the individual elements making
up the product or service can be determined. These implicit
valuations (“utilities”) can be used to create models that can help us
understand how survey takers value different features or capabilities.
In the early years, conjoint analysis was applied to automobile design
using a deck of conjoint cards and the respondents sorted the
supplied cards from best to worst. Based on the responses, it was
possible to make deductions about the importance of “attributes” and
the preference for “levels”. Conjoint analysis saw good adoption in
the 80s with Green and Wind publishing a case study16 in 1989 on
the use of conjoint analysis in the design of Marriott Courtyard
hotels (which I do prefer over other brands, but I digress).
Let us look at Figure 20 to understand the basic elements of conjoint
analysis.

16 https://pubsonline.informs.org/doi/abs/10.1287/inte.19.1.25
AJIT GHUMAN
68

Fig. 20: Attributes and their Levels for Conjoint Analysis
Attributes are ‘dimensions’ of the product (brand, size, performance,
price, etc.) or pricing plans (we use pricing plans in our example
adapted from Conjoint.ly17). It is important to use attributes that you
think drive your customers’ decision making. To arrive at this list of
attributes, you may do a first survey with a focus group and a few
experts. You would also include attributes whose importance to the
buying decision you really want to investigate. While the technique
itself is elegant, be mindful of the customers’ limitations in being
able to engage with your analytical approach at a very detailed level
of granularity. In general, anything more than 6-7 attributes is not
advisable.
Levels are the specific values that the attribute under consideration
may be assigned. These values could be real if we are comparing
existing products or plans or they may be proposed values if we are
designing a new product or plan or want to try out newer
combinations. It is important that the name and value chosen for a

17 https://conjointly.com/guides/what-is-conjoint-analysis/
PRICE TO SCALE
69
Level is understood by the respondents. Any attribute should have at
least two levels if we want to consider its impact in some combination.
Once we have done the basic design of attributes and levels, we need
to choose the actual combinations that we want to test out. These
combinations are referred to as a Profile. Figure 21 depicts four
profiles from our chosen attributes and levels. If you look back at
Figure 20, you may quickly realise that all the levels and attributes
can be used to generate a very large number of unique Profiles. Since
such an approach is not practical, we use some heuristics and
knowledge of the industry to reduce the number of Profiles we offer
to the respondents. Of course, for a complex product or plan
analysis, there are more robust analytical methods available but we
do not usually get involved in that level complexe analysis. If you are
of an analytical bent, I can refer you to a somewhat dated study18 by
Kuzmanovic et al where they explain in great detail the design of a
conjoint analysis to study the preference of students for postpaid
mobile services. There need to be at least two profiles shown to the
respondent at any stage.

Fig. 21: Example of a Conjoint Task for Mobile Plan Choice

18
https://www.researchgate.net/publication/260515194_Understanding_Student_Pref
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
>>>
