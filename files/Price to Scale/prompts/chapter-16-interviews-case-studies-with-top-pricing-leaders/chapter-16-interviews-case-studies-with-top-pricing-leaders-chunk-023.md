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
  "chunk_id": "chapter-16-interviews-case-studies-with-top-pricing-leaders-chunk-023",
  "source": {
    "chapter_title": "Interviews & Case Studies With Top Pricing Leaders",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/16 - Interviews Case Studies With Top Pricing Leaders.txt",
    "source_pages": "185-308",
    "char_start": 114939,
    "char_end": 121995,
    "checksum": "ba293937678c6c36"
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
y has offerings in the complete infrastructure space - from
networking, IT asset management (ITAM), IT operations and
automation (ITOA) to Information Security. This is a fairly typical
profile for companies in this space.
Traditional IT Infrastructure and Operations software was deployed
on physical systems that were mostly on-premise, where the vendor
was far removed from physical access and customers bought
licenses to match the specifications of their infrastructure.
In this regime, pricing was anchored by the hardware oriented
deployment model, where the customer paid a small price for
software running on a smaller machine and a bigger price for the
software running on a bigger machine.

Fig. 32: The Evolution of Pricing from Perpetual Licensing Models
PRICE TO SCALE
251
However with cloud computing this model is changing and so is
NewCo’s Pricing. As shown in Figure 32, the evolution can be
described using three dimensions of the problem, each having an
impact on packaging:
• First, the deployment model has changed over time. Software
used to be deployed at first on a physical device, then moved
to being deployed on virtual devices, and eventually moved to
being in the cloud.
• Second, is the packaging. A company such as Newco may start
off with one or two point products. Then, if they are
successful and grow, they end up with many point products
until they get to the point where there are too many point
products at which point they start creating bundles. Further
down the road they land up with many bundles which turns
out to be too confusing. Eventually, they get to a point where
they realize that they have to simplify the packaging.
• Third, is that metric on which customers are asked to pay for
is also changing. In the beginning, it used to be a perpetual
license plus annual maintenance charges. Then it became a
subscription. And now it is moving to more of a meter style
pricing - like what AWS or Azure do today - where it is based
on some kind of a capacity or usage based metric.
In NewCo’s case its packaging had grown very complex with the
addition of many point products and the company moved to a more
simpler packaging structure. In its case it reverted back to a Good,
Better, Best style of packaging. (This is something we’ve covered earlier
in the book)
It starts with a small (or Good) package which is the minimal viable
product that creates value for a customer. The medium (or Better)
sized package is designed for the vast majority of customers. Finally,
the everything (or Best) package is for the customers with the most
well defined needs or the most sophisticated customers who have to
have every single feature and function. In this model, the point
AJIT GHUMAN
252
products and bundles are gone and the company is left with just
those three packages.
Implications of Simpler Packaging
As part of their own packaging transition, Newco has  also arrived at
a GBB packaging that covers all of Newco’s offerings consisting of
Networks & ITAM, ITOA and Information Security. The customer does
not get to pick and choose individual items but gets one complete
package.
One problem in this three level packaging is that the Sales people
would like to sell an entry or lower level package first and be able to
go back later to try and sell the higher one. That is because they like
to sell more to existing customers. To grow, the Sales team would
take an ITAM customer and sell them ITOA or Information Security.
Similarly, if they have an Information Security customer, they sell
them ITAM or ITOA, or, if they have an ITOA customer, they sell them
ITAM or Information Security. Customers don't buy all three
products, initially.
For Newco, how this works out is that they now have their Essentials,
Business and Advanced packages. So if you have a customer who
bought Essentials, Sales would try to upsell them to Business, and if
they had bought Business, Sales would try to upsell them to
Advanced. Now, if they have already bought your best version there
is no upsell because they are already at the top.
One way to get over this situation is to look at another approach to
growth, and that is to look at the pricing metrics or variables in each
of these packages. For example, Newco can use the size of the
customer’s network in terms of the number of IP addresses. In this
case, Newco can capture growth if the customer’s network grows
from 10000 IP addresses to, say, 50000, thus scaling five times.
There is a case to be made here for still having a very small number
of point products on top of the Good, Better and Best packaging.
When a company introduces this type of packaging it works for a
PRICE TO SCALE
253
year or two. At this point they could start introducing a very small
number of very expensive point products. Of course these would have
to be very specific high value, expensive to deliver, point products.
Because they are expensive to deliver, they would have to be priced
high in order to make any money on them. In this way the Good,
Better, Best model is still able to accommodate point products.
Choosing the Right Pricing Metric
Taking the example of Newco, they had similar decisions to make
across their Networking and ITAM, ITOA, Information Security
portfolio. The key decision they had to arrive at was whether and how
to have a single usage metric and if they would need different metrics
for their three offering groups.
Since the Networking and ITAM offering itself has multiple products
lines they could, technically, have different metrics for each of those.
These could include the number of DNS Queries or Queries Per Sec
(QPS) for DNS services, and for DHCP services it could be the number
of Leases or Leases Per Second.
Similarly, the ITAM pricing could be based on the number of assets
or the number of IP addresses. The ITOA pricing could be based on
the number of devices being managed. The Information Security part
could be priced on the number of users or employees.
Now if they used all of those metrics then they could either sell them
separately or convert them into 15-16 bundles starting with what
would be appropriate for a small attorney’s office and going up to a
large Walmart type of facility and then the typical corporate office of
a large multi location corporation. For each bundle, they would need
to specify a ceiling for the respective usage metric of each of the five
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
>>>
