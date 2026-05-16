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
  "chunk_id": "chapter-16-interviews-case-studies-with-top-pricing-leaders-chunk-009",
  "source": {
    "chapter_title": "Interviews & Case Studies With Top Pricing Leaders",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/16 - Interviews Case Studies With Top Pricing Leaders.txt",
    "source_pages": "185-308",
    "char_start": 34401,
    "char_end": 42068,
    "checksum": "0912d3c02b196362"
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
efined timeframe - we can only bill
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

AJIT GHUMAN 204 Pricing With Complex Underlying Costs at Oracle, with Natalie Louie Natalie Louie is a pricing guru and is currently Sr Director of Product Marketing at Zuora. She is also a pricing SME at Impact Pricing, LLC. I spoke to Natalie about her time at Oracle. As the head of Oracle Marketing Cloud’s (OMC) Pricing Operations from 2015 to 2018, Natalie Louie has extensive experience in value creation through creative subscription pricing and packaging strategies. Her innovative strategies made it easier for customers to buy Oracle products, as well as for the sales team to sell and drive more revenue, profits and lifetime value. She elaborates on some of the innovative price changes made during her time with the company, and more. A Case Study in Re-Pricing Mobile Messaging If I were to detail one specific pricing journey during my stint at Oracle, it would be in the mobile space. At the time, many years ago when I was there, Oracle was making its foray into a mobile-first world. Mobile can be a really complicated domain, thanks to the variety of messaging channels. When you’re sending out mobile marketing messages, there is a whole network of third-party partners you have to work with. When you send that text message from your phone, it actually comes from a phone company, which sets the price of how much it costs. So, you don’t completely own pricing. There are several people taking a piece of that pie, and you have to play by all of their rules and regulations. Every country has their version of networks like Sprint, T-Mobile, AT&T. In each country, every region sets its own rate. It’s something like the stock market — pricing keeps changing every minute. For instance, the rate of a phone call changes rapidly, and each mobile PRICE TO SCALE 205 company has their own framework for it. All in all, it becomes a really complex thing to price. The challenge was — how do we work with this very complicated network of different providers that ultimately set the price of one thing? Why Messaging Pricing Got Messy When we priced and rolled out our first mobile product, we just took on the cost of sending a text message and marked it up before selling, in a very transactional one-time product sale type manner. In creating a Stock Keeping Unit (SKU) for each one, we soon had literally hundreds of SKUs for our mobile product. Each time, we (those of us in the marketing space) worked with an end customer. Say if a J. Crew or an Apple wanted to send international mobile messages, they would be sending them to the US, Canada, Europe, Japan, etc. Each country had a separate SKU, because there’s a different cost to do business. It really all just ended up being an SKU explosion. While this was also just the easiest way to go and price, over time, when we started looking at the pricing, we realized that it had become very hard to manage. It was also hard for the customers. Soon, they started coming back and asking why they should send more mobile messages to one country than another. They asked whether they could apply unused credits elsewhere. Alternatively, they asked if they could use what they are paying for - on email and apply it to mobile, since they are using the latter more. Basically, everyone was saying that it was hard to predict what they were going to send, because they couldn’t control it. Further, they might have been able to relatively control text messages, but not responses, because there’s a cost both ways —and at two different rates! This increased the complexity. We looked at all AJIT GHUMAN 206 of this and asked ourselves what would just make it easier for the customer. We needed to make product changes in a way that we are no longer passing on the complexity to the customer. That experience of how the customer used these messages and bought them, needed to be easy. What needed to be done was the hard work behind the scenes, to ensure an easier customer experience. So, we began meeting and debating on what to do. The Solution: Absorbing the Customer’s Burden Finally, we came up with an idea — a world where customers who are sure they want to do a whole marketing cloud with us can pay just one price, whether they want to send an SMS, email or display message, via whatever marketing channel. Nowadays, it’s all about talking to the customer on the right channel at the right moment. This is hard to predict, especially when you bring in Artificial Intelligence (AI) that tells you when and where to send a message. At this point, we could manage pricing wherein you just buy a bucket of messages and apply cost to every channel, depending on use. We owned email, web and display, and those had some hard costs. But mobile had many hard costs. How were we to make it really easy? After going to the drawing board, we thought — how about when people log into our product, we aggregate all of these different countries and telephone companies for them. Customers can come into the product and pick countries. There’s a hard cost and there was full transparency involved in presenting that. They pay the hard cost directly to the aggregators and get a bill for it. As for Oracle, we charge you the same fee for sending a message — across any channel. What this means is that we moved the burden of hard costs that we couldn’t control. We gave full transparency to the customer, but in a PRICE TO SCALE 207 really easy way so that they could see what the costs of doing business were. Usually, complex expenses are not exposed. Customers just keep negotiating because they just see one price and don’t realize all the third-party hard costs. We needed to expose those hard costs to them, but we had to do it really easily. We couldn’t just tell them to go to all these different aggregators, because that’s not what they wanted to do. To remedy this, we built (almost) a marketplace for aggregators to come in and showcase their hard costs. Then, customers could pick whoever they wanted to work with directly, and know which bill they would get. But then, with Oracle, they would be just paying that usage fee, like Cost Per Message (CPM) — some kind of fee for any message, to be sent across any channel they wanted. The only channel that was going to have a hard cost was mobile, which is what we exposed. Convincing Management to Embrace the New Process Pricing elegantly is like the Holy Grail. We came up with a pricing strategy and I spoke to my product managers and engineers. Our roadmap was baked out, but we would require a re-architecture of the entire product. So, we got a lot of pushback. That’s the hard thing with pricing— you can come up with all these great ideas, but it gets hard to actually implement and build it. So, how can you use tools to actually support that? How do you convince product management? Over time, we were able to convince them to do it because we started taking on revenue goals. I made a case of how pricing impacts revenue directly.
>>>
