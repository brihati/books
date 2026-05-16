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
  "chapter_id": "chapter-08-step-5a",
  "chunk_id": "chapter-08-step-5a-chunk-006",
  "source": {
    "chapter_title": "Step 5a",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/08 - Step 5a.txt",
    "source_pages": "99-124",
    "char_start": 26712,
    "char_end": 32331,
    "checksum": "e3394d6c72e83e5f"
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
process and revert back to a totally manual way of selling — if this happens you will be left cleaning the mess on the other hand. There are a ton of resources online that offer best practices on CPQ implementation. One that I liked is a book on the topic, CPQ Implementation Guide by Marcin Krzych26. As a final note of personal opinion, fast growing companies where pricing structure may undergo evolution every other quarter, may not want to overinvest in this CPQ capability. Primarily because CPQ implementations take a long time, and by the time you have put something into product use, new requirements come up - sinking a lot of time and resources in this never ending process. At some point

you may still need to do this, I would personally live on a Google spreadsheet based calculator until ~15-20M revenue which would provide (hopefully) enough time to have a mature internal deal closure process. Discounting One of the tools that always works to your advantage in B2B software pricing is discounting, as long as customers can’t just put their credit card information in and buy which is the only case where disco- unting is bound to be 0. In most other cases where customers negotiate the price with sales, discounting not only needs to be baked into the price point you come with due to industry-default expectations of the sales process, but it also lets you survive without very robust statistical models to arrive at the price point(s) for your product as the price point can vary somewhat even amongst lookalike customers.

26 https://www.amazon.com/CPQ-Implementation-Guide-implementing-
organisation-ebook/dp/B07H64F4SM
PRICE TO SCALE
115
This is the closest tool that lets us reach a price optimized local
maxima that can account for variations in price elasticity between
customers.
As a very rough rule, you can expect discounting in different
customer segments to obey the following ranges:
• Commercial: 10 to 30%
• Mid-sized: 20 to 50%
• Enterprise: 30 to 70%
If you have three customer segments that can be defined by size and
map to the descriptions above, then you can simply pick a rough
number from the ones above and essentially pad the price point you
would have come up with by that amount, e.g. your commercial plans
will have a buffer padding increasing the price point by 10 to 30%.
Additionally, but limiting the discounting authority of your reps,
managers and leadership in sales to steadily increasing approval
limits, you actually create a sales tool for your reps that helps them
build trust with their prospects as they end up fighting for a better
deal for the customer. The best analogy is that you are purposely
adding some friction to the sales process. Just remember a little
friction goes a long way, a lot of friction leads to a disgruntled sales
team and customers who balk at the initial number they see.
Evaluating the Effectiveness of Discounting Strategies
Once a discounting structure has been implemented, it’s essential to
evaluate whether it is functioning as intended. There are two critical
aspects to assess:
1. Customer Behavior Impact: The primary goal of any discounting
strategy is to influence specific customer behaviors. It’s important to
verify whether the discount is indeed driving the desired outcomes,
such as a higher close-rate, faster movement through the sales
pipeline, longer-term commitments, or an increase in multi-product
purchases. The effectiveness of the discount should be measured by
AJIT GHUMAN
116
its ability to achieve these objectives. If the anticipated behavioral
changes are not materializing, it may indicate that the discounting
strategy needs to be re-evaluated or adjusted.
2. Correlation with Sales Performance: Another key factor to examine
is whether the level of discounting is more closely correlated with the
attributes of the customer or with the actions of the sales
representative. In other words, is the discount being applied based
on the characteristics and needs of the customer, or is it largely
dependent on the individual sales rep’s approach? If discounting
patterns are more reflective of who is selling rather than who is
buying, this could suggest inconsistencies in how discounts are
applied across the sales team. Such a scenario might indicate the
need for retraining the team or it could highlight flaws in the
discount design itself.
By regularly monitoring these two aspects, organizations can ensure
that their discounting strategies are not only effective in achieving
their intended goals but also that there is no ‘revenue leakage’
occurring as a result of unnecessary discounting that does not yield
the results.
Discounting Matrix
In order to make this usable, a very standard operational document
is something called a Discounting Matrix. It lets your Sales team
know the level of discounting authority different people in the team
have to offer a discount to the customer. Even if you may have built
say a 40 to 50% padding in list prices, you should give your AEs lesser
discounting authority than that -- the idea is to include a little bit of
friction in the process that lets an AE run a discount up their
hierarchy and be able to offer something that the customer wants.
Yes it is artificial, but it works. Higher discounts must appear to
prospects as being earned or negotiated and not just given away by
any sales representative - which will dilute the value of the discounts.
PRICE TO SCALE
117
Figure 31 presents one example of such a discounting matrix table. It
shows a progressively increasing discounting and deal term authority
structure across sales hierarchy levels.
>>>
