Extract preservation notes for this book chunk.

Rules:
- Preserve concrete content: claims, examples, stories, names, dates, numbers, definitions, terms, and useful quotes.
- Keep wording faithful to the source; do not add outside facts.
- Quotes must be short and must appear in the chunk.
- If a field has nothing meaningful, leave it as an empty list or empty string.
- Return only valid JSON matching the schema.

Schema:
{
  "book_id": "the-strategy-and-tactics-of-pricing",
  "chapter_id": "chapter-18-financial-analysis-analyzing-costs-and-profits-f",
  "chunk_id": "chapter-18-financial-analysis-analyzing-costs-and-profits-f-chunk-006",
  "source": {
    "chapter_title": "Chapter 9 Financial Analysis Analyzing Costs and Profits for Pricing",
    "source_path": "/Users/sachin/books/files/The Strategy and Tactics of Pricing/chapters/18 - Chapter 9 Financial Analysis Analyzing Costs and Profits for Pricing.txt",
    "source_pages": "228-260",
    "char_start": 29672,
    "char_end": 35907,
    "checksum": "ddad382993712a76"
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
particular level of proﬁ tability. The larger the price change—or the smaller the EXHIBIT 9-2 EXHIBIT 9-2 Finding the Breakeven Sales Change Finding the Breakeven Sales Change Chapter 9 • Financial Analysis 217 contribution margin—the greater the volume change necessary to generate at least as much contribution as before. Assume for the moment that there are no incremental ﬁ xed costs in implementing Westside’s proposed 5 percent price cut. For convenience, we make our calculations in dollars (rather than in percentages or decimals). The contribution margin is: $CM = $10.00 – $5.50 = $4.50 Given this, we can easily calculate the breakeven sales change as follows: % $ . Breakeven sales change

.
or
−(
)
$ .
−
(
)
$ .
.
5. 0 +( $
−
0 125
12
1 . %
5
 Thus, the price cut is proﬁ table only if sales volume increases by more than
12.5 percent. Relative to its current level of sales volume, Westside would have
to sell at least 500 additional units to maintain the same level of proﬁ tability it
had prior to the price cut, as shown below:
 Unit breakeven sales change = 0.125 x 4,000 = 500 units
 If the actual increase in sales volume exceeds the breakeven sales change, the
price cut will be proﬁ table. If the actual increase in sales volume falls short
of the breakeven sales change, the price change will be unproﬁ table. If West-
side’s sales increase as a result of the price change by more than the break-
even amount—say, by an additional 550 units—Westside will realize a gain in
proﬁ t contribution. If, however, Westside sells only an additional 450 units as
a result of the price cut, it will suffer a loss in contribution.
 Once we have the breakeven sales change and the proﬁ t contribution,
calculating the precise change in contribution associated with any change in
volume is straightforward: It is simply the difference between the actual sales
volume and the breakeven sales volume, times the new contribution margin
(calculated after the price change). For Westside’s 550-unit and 450-unit vol-
ume changes, the change in contribution equals the following:
 (550 – 500)  × $4 = $200
 (450 – 500)  × $4 = –$200
 The $4 in these formulas is the new contribution margin ($9.50 – $5.50). You
might have noticed that the denominator of the percent breakeven formula is
also the new contribution margin.
 We have illustrated breakeven analysis using Westside’s proposed
5 percent price cut. The logic is exactly the same for a price increase. Since
a price increase results in a gain in unit contribution, Westside can tolerate
some reduction in sales volume and still increase its proﬁ tability. How much
of a reduction in sales volume can Westside tolerate before the price increase
becomes unproﬁ table? The answer is this: Until the loss in contribution due to
reduced sales volume is exactly offset by the gain in contribution due to the
price increase. As an exercise, calculate how much sales Westside could afford
to lose before a 5 percent price increase becomes unproﬁ table.
 It is important to note that the calculation resulting from the break-
even sales change formula is expressed as the percent change in unit volume
required to break even, not the percent change in monetary sales (for example,
Chapter 9 • Financial Analysis
218
the percent change in dollar sales) required to break even. In the case of a price
cut, the percent breakeven sales change in units necessary to justify the price
cut is larger than the percent breakeven sales change in sales dollars because
the price is now lower.
 To convert from the percent breakeven sales change in units to the per-
cent breakeven sales change in dollars, you can apply the following simple
conversion formula:
 % BE($) = % BE(units)  + % Price change [1  + % BE(units)]
 For example, for Westside’s proposed 5 percent price cut above, the percent
breakeven sales change in unit volume terms was 12.5 percent. What is the cor-
responding percent breakeven sales change in dollar sales terms? The answer
is calculated as follows:
 % BE($) = 0.125  + (–0.05)(1  + 0.125)
 = 6.88%
 Thus, to break even on the proposed 5 percent price cut, Westside would have
to increase its total dollar sales by 6.88 percent, which is exactly equivalent to
a 12.5 percent increase in unit volume.
 BREAKEVEN SALES INCORPORATING
A CHANGE IN VARIABLE COSTS
 Thus far, we have dealt only with price changes that involve no changes in
unit variable costs or in ﬁ xed costs. Often, however, price changes are made
as part of a marketing plan involving cost changes as well. A price increase
may be made along with product improvements that increase variable costs,
or a price cut might be made to push the product with lower variable selling
costs. Expenditures that represent ﬁ xed costs might also change along with a
price change. We need to consider these two types of incremental costs when
calculating the price–volume trade-off necessary for making pricing decisions
proﬁ table. We begin this section by integrating changes in variable cost into
the ﬁ nancial analysis. In the next section, we do the same with changes in
ﬁ xed costs.
 Fortunately, dealing with a change in variable cost involves only a sim-
ple generalization of the breakeven sales change formula already introduced.
To illustrate, we return to Westside Manufacturing’s proposed 5 percent price
cut. Suppose that Westside’s price cut is accompanied by a reduction in vari-
able cost of $0.22 per pillow, resulting from Westside’s decision to use a new
synthetic ﬁ ller to replace the goose feathers it currently uses. Variable costs are
$5.50 before the price change and $5.28 after the price change. By how much
would sales volume have to increase to ensure that the proposed price cut is
proﬁ table?
 When variable costs change along with the price change, managers
simply need to subtract the cost change from the price change before doing
the breakeven sales change calculation. Unlike the case of a simple price
change, managers must state the terms on the right-hand side of the equation
in currency units (dollars, euros, yen, and so forth) rather than in percentage
changes:
Chapter 9 • Financial Analysis
219
%
$
 Breakeven sales change =
−(
)
$
$ C
$
−
(
)
$
$
P
C
$
Δ
$
$
>>>
