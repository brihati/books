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
  "chapter_id": "chapter-11-pricing-example",
  "chunk_id": "chapter-11-pricing-example-chunk-004",
  "source": {
    "chapter_title": "Pricing Example",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/11 - Pricing Example.txt",
    "source_pages": "143-158",
    "char_start": 13302,
    "char_end": 19618,
    "checksum": "00be5e4ba5bd732f"
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
roader market we are not so constrained, so we will attempt to survey a few hundred enterprise companies (this will generally give us a 10-15% response rate) and live conversations again with ~10 companies. For primary research we will use the template described in the earlier chapter. Specifically our live deck will have the following sections: • Intro to the technology/product PRICE TO SCALE 147 • Force rank pain points (relating to handling customer support issues) • Demo • Unprompted feedback • Force rank benefits • Open-ended feedback on pricing metric • Low price (poor quality) and High price (too expensive) bounds To test a specific price point we would need to translate our metric to

approximations that a business will understand. Let’s take the example of warbyparker.com, on checking its traffic from sitechecker.pro the total monthly visits are around 4 Million, with an average order volume of ~$150 and a 2% total conversion rate, it would work out to a monthly revenue of $12Million. Now how do we create numeric options, both for in-person interviews or surveys? We need anchors and industry standard assumptions. Assuming a company such as Warbyparker spends about 10% of revenue on customer support and gets a 50-50 split in phone calls vs online support needs, and that roughly 10% of monthly visitors need help via chat. We can estimate a total spend of $1.2 Million/month on support, $600k of which is via the online channel, from about 400,000 interactions (assuming this will also automate any email support). So their customer support spend is about $1.5 per online interaction. Now we estimate that we can reduce this number by 50%, we arrive at 75cents per interaction as the ceiling of upside we bring. Will clients be willing to pay 10% of this? A fourth? Half? Another way to look at this is we reduce the $600k/month number by half ~$300k/month and as a percent of revenue it works out to 2.5%. Can we charge .25% of revenue or .5%? These are our anchors which we will quote side-by-side with the cost per interaction. AJIT GHUMAN 148 While this can be explained in-person, it will need to be posed a few different ways in a survey for us to converge on a good answer. Here is what one of the survey questions will look like with different anchors: Q. Below what price (cost per interaction) will you question the product’s quality or effectiveness? 1. 60 cents per interaction (~2% of revenue) 2. 50 cents per interaction 3. 40 cents per interaction 4. 30 cents per interaction 5. 20 cents per interaction 6. 10 cents per interaction 7. 5 cents per interaction (~0.20% of revenue) Here is another way to ask this question again, with different anchors. Q. Below what price (cost per interaction) will you question the product’s quality or effectiveness? 8. 60 cents per interaction (~20% of total support costs) 9. 50 cents per interaction 10. 40 cents per interaction 11. 30 cents per interaction 12. 20 cents per interaction 13. 10 cents per interaction 14. 5 cents per interaction (~2% of support costs)

PRICE TO SCALE
149
Let’s now assume we conduct the primary research across our two
key segments, the following is an example of what aggregated
feedback could look like:
Topic
Mid-market customers
Enterprise customers
Top pain
points (from
force rank)
● Top rank by 7/10
customers, “personnel
crunch with inability
to scale to demand at
peak times”
● Second rank by 5/10
customers, “high cost
of phone support”
● Third rank by 6/10
customers, “customer
complaints due to long
phone and chat wait
times”
● Top rank by 8/10
customers, “customer
complaints due to long
phone and chat wait
times”
● Second rank by 5/10
customers, “personnel
crunch with inability to
scale to demand at peak
times”
● Third rank by 6/10
customers, “cumbersome
agent-side workflows”
Unprompted
feedback on
the demo
“This is cool, seems like
we can offload a large
chunk of our support
issues to a bot”
“It will help reduce our
need to constantly hire”
“As a tech company, we
like such a seamless tech
solution vs throwing
humans at the problem”
“This looks like it could
mitigate customer hold
times and improve NPS”
“Would be a nice addition to
have during peak season”
“I wonder if we can also
offer the automation to our
agents who have to deal with
clunky manual workflows in
our current system”
Unprompted
feature on
features
within
package
“I like it, it's simple yet
effective”
“We might want a little bit
more service available as
this is a new tech for us”
“The BI capability is
important for us to measure
our performance. Can we
equip all our managers with
it”
“Can we build customer
feedback bots to measure
quality?”
AJIT GHUMAN
150
Top benefits
(from force
rank)
● Top rank by 8/10
customers, “reduce
personnel costs”
● Second rank by 5/10
customers, “move to
digital channels”
● Third rank by 6/10
customers, “increase
customer NPS”
● Top rank by 7/10
customers, “increase
customer NPS”
● Second rank by 6/10
customers, “move to
digital channels”
● Third rank by 5/10
customers, “reduce
personnel costs”
Open-ended
feedback on
pricing
metric
“I think it can work as
long as the price isn’t
exorbitant”
“I like that it scale with
usage, we don’t like paying
a large capex type
amount”
“Our online analytics
vendor uses a similar
metric”
“We pay our current
vendor on a pay per seat,
but I understand this is a
different concept”
“The metric is fine, I hope
you can discount it because
our usage will be high”
“We’re ok with the metric as
long as the product actually
automates as much as you
claim. A pilot will help”
“We will use this with our
main support solution, so it
would help to only pay for
when we really use it”
Price below
which
product will
be deemed
poor quality
The mode (highest freq
selection) for this
question comes out to be
10 cents per interaction
The mode (highest freq
selection) for this question
comes out to be
30 cents per interaction
Price above
which
product will
be deemed
too
expensive
The mode (highest freq
selection) for this
question comes out to be
40 cents per interaction
The mode (highest freq
selection) for this question
comes out to be
70 cents per interaction

PRICE TO SCALE
151
And here is a summary of the output of the WTP survey (refer our
discussion on cumulative survey tables in the prior chapter):
Mid-market-Enterprise
-
>>>
