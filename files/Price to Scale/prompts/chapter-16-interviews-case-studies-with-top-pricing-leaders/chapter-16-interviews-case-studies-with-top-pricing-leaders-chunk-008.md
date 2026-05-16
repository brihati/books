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
  "chapter_id": "chapter-16-interviews-case-studies-with-top-pricing-leaders",
  "chunk_id": "chapter-16-interviews-case-studies-with-top-pricing-leaders-chunk-008",
  "source": {
    "chapter_title": "Interviews & Case Studies With Top Pricing Leaders",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/16 - Interviews Case Studies With Top Pricing Leaders.txt",
    "source_pages": "185-308",
    "char_start": 30456,
    "char_end": 35101,
    "checksum": "ca5d4efcfe89bb0e"
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
omers and volume discounts for the larger ones. We wanted to make sure that small customers who only have a budget of $100 a month could pay us alongside large customers who were paying us several million a year. The idea was to see if the model could be applied to both small companies and giant ones, and if growth could be comfortable with each. 5. Is it aligned with value: This was our key consideration. We ran regression analyses for every metric under consideration to see which correlated most with revenue. While Event volume didn’t pass the test, it was MTUs that won by a landslide. Our philosophy was that we didn’t want start-ups to pay too much. We wanted to see which of these metrics

does best at keeping it cheap for a small company, by

46 Danielle Kucera, ‘Inside Mixpanel:In 2019, we realized our pricing wasn’t good
for our customers. Here’s what we did.’ https://mixpanel.com/blog/pricing-mtu-
model/

AJIT GHUMAN
202
charging more for bigger companies. MTUs ended up
winning on that front. It was basically how many unique
people you track, and served as a proxy for MAUs.
The Roll-out of the New Model
At first, it was opt-in. We already knew which customers were finding
it hardest under the events model — we could analytically figure that
out. We also gave the pitch to our sales team to talk to customers who
were upset about the price they were paying. We did that and
basically kicked off a pilot. We had salespeople go out and ask if
someone would actually rather be on the new option, instead of the
events pricing model. So, many customers who were initially going
to churn actually liked it a lot, switched over to the new plan, and
stuck around with Mixpanel.
These were all existing customers. We already had Mixpanel data on
exactly how many MTUs they had — so we had a very good sense of
the numbers. Even for new customers, we found that almost
everyone had Google Analytics installed on their website or their
properties. Our sense of it was that we were roughly looking at Google
Analytics plus 20 percent.
We wanted to keep our revenues flat. So we said, "Look, if we assume
that everyone was to move over to this new plan, we want to make
exactly the same money. This is not a call to make more money off
our customers.” Thereafter, some customers who were significantly
better off with MTU would switch; and some who were significantly
worse off would never switch. So, net-net we expected to lose some
money as a result of the switch, but hoped to make it up with churn
rates - which we thought would actually decrease by 10-15 percent.
Optimizing the Model at Every Step
Thereafter, one learning on the sales front was that the switch did
make the process a lot easier. This was because the team could now
figure out how much the customer needed based on Google
Analytics.
PRICE TO SCALE
203
What got harder was that there was more uncertainty in the model
than we had realized. We’re trying to get around it now, but take for
instance a situation in which you’re tracking events on your
homepage and then run a Snapchat ad that loads your homepage.
Now, each person who sees that ad is pulling up your entire
homepage. That blows up your MTU count because there are way
more unique visitors — but they don’t do anything on your product.
And now that’s something to pay for.
So that was an unforeseen development. We did know that some
customers were very high MTU, but very few Events. To address this,
we had to come up with a different pricing model called MTU Five.
As part of this model, a user doesn’t count as one until they’ve done
five events. This approach tackled 90 percent of such cases.
Secondly, some things that were easier on our old model are a bit
harder now. With Events (value metric), it would have been a lot
easier, say if you joined on the 15th of a month and we could just
count events from the 15th to the 30th for the month. With MTUs, it’s
harder because a month is a defined timeframe - we can only bill
you on the first of every month. So, it would now require a new billing
logic to only charge you for 15 days for your first month; and then
do it on the first of every future month.
Managing Pricing Operations
I am not a fan of CPQ. What we did to get around CPQ was to have
an online Google Sheet to calculate. It just literally lists out every
single price point and MTU podium, and our salespeople just use
that. When they need to make up a quote, they go there, figure out
the price, and all of the back and forth with the customer happens
off the Google Sheet. Finally, when they’re ready to submit an actual
contract, they go into CPQ and put in the details.
>>>
