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
  "chunk_id": "chapter-16-interviews-case-studies-with-top-pricing-leaders-chunk-024",
  "source": {
    "chapter_title": "Interviews & Case Studies With Top Pricing Leaders",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/16 - Interviews Case Studies With Top Pricing Leaders.txt",
    "source_pages": "185-308",
    "char_start": 121295,
    "char_end": 126883,
    "checksum": "a3f2bf9df48b3839"
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
pective usage metric of each of the five
product components within that bundle.
So it was apparent that this would become really quite complex and
yet it would never fit exactly for any single customer; they are always
going to need more of some item and less of some other. And even
then they may feel they are overpaying for something.
AJIT GHUMAN
254
Even though this arrangement is complex, a number of companies
price their offerings like this. One example of this could be
Cloudflare47. As Figure 34 shows, Cloudflare has a Free plan and then
Pro, Business and Enterprise plans. Then if the customer needs more
they can take from a set of Add-Ons on top of these plans as depicted
in Figure 35.

Fig. 34: Cloudflare Pricing Plans

Fig. 35: Add-Ons for Cloudflare Pricing Plans

47 https://www.cloudflare.com/en-in/plans/
PRICE TO SCALE
255
For Newco it made more sense to have a single metric for everything.
Newco needed to not only look at what was theoretically best for
them, but also their established sales motion. In Newco’s case they
decided to go with a single metric because  that was the preference
of their Sales and field leadership and that group values simplicity
more than anything else. The field leadership wants to do big deals
where the customer buys all the products.
In Newco’s case the single metric used became IP addresses for
everything, even though IP addresses are not the most natural metric
for some of those items. In this case, they would be using a
suboptimal metric for some of the items, but the reason they were
well advised to do it was to have the simplicity of the same metric for
all the items. Using this single metric, they were been able to develop
the Essentials, Business and Advanced packages for each of
Networking and ITAM, ITOA and Information Security.
Considerations For Rollout
At this point Newco has been over the transformation and
simplification of packaging that they attempted and the single metric
approach to pricing that they liked. Now they have to deal with how
they roll this out to customers and their own field teams.
We start with a metric that we wish to use, and in Newco’s case it is
the number of IP addresses.
Newco has multiple ways in how they can make the customer pay for
what they consume. The first method is that the customer pays for a
certain quantity and they cannot go over the ceiling. The second
method is that the customer consumes what they need and Newco
bills them for the actual arrears based on what they consumed for a
period that has been chosen, say per month. That is the method AWS
and Azure use. It is also possible to bill the customer in advance for
a certain amount but they can go over the ceiling and at the end of
the period their ceiling gets resized. This flex method has now
AJIT GHUMAN
256
become quite popular with the larger cloud vendors and has become
a recommended model as well.
Having developed a mature and elegant model Newco still has the
challenge of getting it implemented internally. If we go over the
process again we have four steps to complete:
• The first is of course deciding the metric to price on, that
being the number of IP addresses for Newco.
• Then there is the need to build the ability to measure the
chosen metric into the product and that is non-trivial. The
product managers and the engineers have a tendency to not
want to do this. Typically, when engineering enhancements
are discussed and decided, this aspect takes very low priority.
As the product marketer with ownership for the pricing
model, it is likely that you will have to approach someone like
the CEO to drive this part from the top down. Even then, this
is quite difficult and the actual changes may take like a year
or more to work out. The lack of instrumentation when
transitioning from licensing to metric driven subscriptions
seems to get repeated across companies.
• The next step in implementing the model is to collect all the
data into a database, or more likely, a data lake.
• And finally you have to manifest it, that is put it across to your
customers and to the internal teams. Most companies are
trying to do this through a Customer Service Management
(CSM) team. The customer service managers are responsible
for all the follow on sales to the customers. Obviously, to do
this your entire compensation model, your field model, the
sales motions, the Go To market (GTM) strategy, and the Sales
Ops features like territory assignments has to change.
In this transformed approach, the Sales teams get compensated for
upselling a customer on new functionality, or they get compensated
for increasing the quantity that the customer is buying or some
similar change. They don't get compensated for anything else
because the CSM team has taken on most of the post sales work. In
PRICE TO SCALE
257
that sense, the CSM team is fully focussed on the data being
generated out of the selling and consumption.
The key challenge with this approach is that the CSM team cannot be
a success unless they have all the data on usage being generated.
Having the data ready is critical for the way we want to price now -
pick the metric, count it, collect it in a data lake, show it in a
dashboard. Unless we can do those four things we cannot get the new
pricing model implemented well. This is not a problem that is
confined to one company but is prevalent quite widely. The PMM or
Pricing leaders often face an uphill climb to influence Product or
Engineering in a manner that prioritises this instrumentation for
pricing. But it is important to get the new Pricing actually work.
>>>
