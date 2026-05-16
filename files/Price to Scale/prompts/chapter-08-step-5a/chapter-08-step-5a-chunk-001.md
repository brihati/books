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
  "chunk_id": "chapter-08-step-5a-chunk-001",
  "source": {
    "chapter_title": "Step 5a",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/08 - Step 5a.txt",
    "source_pages": "99-124",
    "char_start": 0,
    "char_end": 6981,
    "checksum": "e87e5ba532d49a18"
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
95

STEP 5A
Pricing Operations

Ok, so we’re now. We’ve finally done all the strategic decision making
and analysis to arrive at the pricing structure.
Time to celebrate? Not in the least.
Later in the book, I’ve documented my interview with Natalie Louie
who is currently the Sr Director of Product Marketing at Zuora. One
of her quotes really resonates with my own experience of implement-
ing a new pricing model inside a company, “I would almost argue,
for me at least, pricing strategy is the easy part. Pricing operations,
that is where you start pulling out your hair. And that's where all
you're faced with is ‘no’. ‘No, we can't do that.’ ‘No, we can't do this’”
Pricing Operations involves all systems, processes and people
involved in ensuring the new pricing model is fully adopted in your
company and such that the sales engine works like a smoothly run-
ning machine.
Not even the best pricing model can yield any result if it's not
operationalized to enable a smooth sales process and 100% adoption
by the sales, professional services, ops and finance teams.
This is especially true of sales-driven cultures where ad-hoc deal by
deal pricing has been part of a company’s history.
So let’s make sure we get this right. What do we need to do?
AJIT GHUMAN
96
1. Packaging Reference Doc: One production-ready place where
your company’s pricing resides such that it is always referen-
cible by anyone inside your company and provides complete
guidance on all available features as well as constraints.
2. Website: Decide whether to publish your pricing and packag-
ing on your website.
3. Team: Understand the different roles required to man pric-
ing operations and then staff these roles. In fact, we dedicate
the next chapter solely to the Deal Desk function.
4. Pricing Calculator: Build an easy way for your sales team to
run pricing scenario analysis at the early stages of the sales
team.
5. Quoting System/CPQ: Build an easy way for your sales team
to quote pricing to their prospects.
6. Product Metering: Decide if you need to build a metering sys-
tem for the key value metric such that you can bill customers
if they are on a consumption based model.
7. Discounting: Set and operationalize guardrails and rules
around discounting across sales reps, sales leadership and
the CEO/CFO.
That’s a lot! It really is.
Compared to the creation of the pricing model, the implementation
takes 3-5x the amount of effort (depending on which items you check
off this list above). I say this to caution you before committing a full
implementation in 4-6 weeks (been there, done that) and that any
meaningful rollout will take at least a quarter (3 months), often more.
With that caution out of the way, let’s now discuss each of these items.
Packaging Grid
One document that will help truly align your packaging with all GTM
stakeholders internally (product, sales, sales engineering, finance,
you name it) is a simple shared (and up to date) product packaging
PRICE TO SCALE
97
grid that lists out the features included in each Tier, as well availa-
bility across geos, constraints and implementation notes.
The following table below shows a simplified version of such a grid
that I’ve used, and one that has been very convenient to rid of any
confusion during the regular sales motions. The effort taken to keep
the document current (mostly once-a-quarter updates) is always well
worth it in having clarity about basic questions, ‘what can we sell?’,
‘what’s in the elite plan?’, ‘does this work in Europe?’, ‘how complex
is the integration?’ and so on.
Once in place you can bet that it will drive projects to improve your
website product pages, provide answers for RFP questions, serve as a
source of truth by the company and limit one off questions on a fea-
ture or package set (of which there will be plenty once a new pricing
model is released).
Product
Customer
Facing
Feature
Name
Pro
Elite
Constraints AMER
UK / EU
Need to know
about
implementation
Product A Widget A
TRUE
TRUE

Avail
Avail

Widget B
TRUE
TRUE

Avail
NA

Widget C

TRUE

Avail
Avail

Widget D
TRUE
Does not
work in EU Avail
Avail

Add-on:
Feature X TRUE
TRUE

Avail
Avail
Requires
special
integration,
delaying
implementation

Add-on:
Feature Y
TRUE

Avail
NA

Add-on:
Feature Z
TRUE
Does not
work in EU Avail
Avail

AJIT GHUMAN
98
Website Pricing Page
The decision to publish pricing on your website is not to be taken
lightly, and it should align with your overall GTM strategy.
There is today a general consensus within SaaS circles that publish-
ing your pricing is a de-facto good thing -- on this point I disagree.
This is a decision that requires thought.
Publishing pricing on the website makes more sense for high velocity
sales engines with a more transactional sale and cut and dry
packages, but less so when the deals are complex, low velocity with
larger deal sizes. As soon as you publish your pricing on the website
it forces you to have robust differentiation between tiers as all types
of customers, channel partners and even competitors will start to use
this as a reference.
Publishing pricing will also lead prospects to comparison-shop and
question their software needs, existing customers may also start to
want downgrades (this scenario is covered in the Citrix case study
later in the book).
Every company’s GTM is different and the decision should align with
the GTM strategy.
1. A company selling into only the mid-market could perhaps
benefit from this approach and improve selling efficiency.
2. While a company selling mostly to Global 2000 and Fortune
500 firms is likely to have more involved deals, and
customers whose price sensitivities vary more. Publishing
pricing on the website in this case may not be helpful.
3. Companies who sell both into the mid-market as well as
enterprise have a tougher decision, but as listed below they
can choose to publish just the packages online and reserve
the pricing to sales conversations.
PRICE TO SCALE
99
What you should know is there are many options here:
1. You can publish your pricing and packaging in full
2. You can summarize your pricing (e.g. starting from $xx,xxx
with yyy units included) and packaging but leave complex
questions to sales calls
3. You can publish a summary your packages and leave pricing
discussions to sales
4. You can choose to make the pricing and packaging more
about value delivered and use it as a lead source
There are thousands of examples of pricing pages out there. Let’s
consider a few pricing pages as mini case studies and try to analyze
why a company in question may have selected to build their pricing
page a certain way - a process that will guide your own thinking as
you build your pricing page. Note that we may not find pricing pages
for truly enterprise facing GTM companies, so note that this
discussion of analyzing publicly available pricing pages inherently
suffers from an inherent self-selection bias.
Company & Page
Commentary
https://ahrefs.com/pricing
>>>
