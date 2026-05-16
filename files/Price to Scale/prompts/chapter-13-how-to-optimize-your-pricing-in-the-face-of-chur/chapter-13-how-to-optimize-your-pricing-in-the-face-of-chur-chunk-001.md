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
  "chapter_id": "chapter-13-how-to-optimize-your-pricing-in-the-face-of-chur",
  "chunk_id": "chapter-13-how-to-optimize-your-pricing-in-the-face-of-chur-chunk-001",
  "source": {
    "chapter_title": "How To Optimize Your Pricing in the Face of Churn & Inflation in SaaS",
    "source_path": "/Users/sachin/books/files/Price to Scale/chapters/13 - How To Optimize Your Pricing in the Face of Churn Inflation in SaaS.txt",
    "source_pages": "165-174",
    "char_start": 0,
    "char_end": 5881,
    "checksum": "aa09b55a2ad17f1c"
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
161

HOW TO OPTIMIZE YOUR
PRICING IN THE FACE OF
CHURN & INFLATION IN
SAAS

Since 2020, U.S. inflation has experienced significant volatility, peak-
ing at 8.3% in 202235 due to pandemic-related disruptions, supply
chain issues, and geopolitical events36. Efforts to control inflation,
including Federal Reserve interest rate hikes, have helped to
moderate it to around 3.3% by mid-202437.
In the SaaS industry, decision-making about price adjustments often
revolves around discussions on inflation. However, a closer examina-
tion reveals that the real driver behind pricing changes is not inflation
but regime change, characterized by shifts in interest rates.
Regime Change vs. Inflation
Inflation is typically measured by the change in the price of a basket
of goods and services over time. From January 2000 to June 2022, (as
illustrated in the Fig.138), we observe significant price increases in
sectors like hospital services and college tuition, while technology

35 https://www.bls.gov/opub/mlr/2023/beyond-bls/what-caused-inflation-to-spike-
after-2020.htm
36 https://www.weforum.org/agenda/2023/05/us-monthly-inflation-rate-chart/
37 https://tradingeconomics.com/united-states/inflation-cpi
38 https://www.aei.org/carpe-diem/chart-of-the-day-or-century-5/
AJIT GHUMAN
162
products, specifically computer software, have become more afford-
able. This trend highlights an important point: inflation impacts
industries differently, and for SaaS companies, the usual inflation
metrics do not directly correlate with software pricing dynamics.

Fig.1: Diverging Trends in U.S. Consumer Prices and Wages (2000-2020)
As SaaS products mature and the market becomes more crowded,
companies face a common challenge: commoditization. This means
PRICE TO SCALE
163
that the unique features that once commanded high prices start be-
coming standard, available from many competitors at lower prices –
resulting in deflation. Additionally, Moore’s law applies and the
underlying storage and hosting costs become both cheaper over time
as well as amortized over large customer bases.
AJIT GHUMAN
164
Example of Software Deflation: DocuSign
DocuSign is an example of this dynamic. Early on in its lifecycle
DocuSign was able to charge premium prices for its e-signature
product line. But as the market grew, more companies like Pan-
daDoc and HelloSign entered the scene, offering similar services
at lower prices. This increased competition led to commoditiza-
tion, where digital signatures became a standard offering, not a
unique feature.
It led to:
• Market Saturation: Suddenly, there were many companies
offering digital signature solutions. Customers now had
plenty of options. This abundance of choices naturally
drove prices down because competitors were trying to
attract customers with lower prices.
• Price Wars: To win over customers, companies engaged in
price wars, continually lowering their prices to outdo each
other. This competition further pushed down prices across
the board.
• Feature Parity: Features that were once unique to
DocuSign, like secure signing and document storage,
became standard. Almost every provider offered them. As
a result, customers began to expect these features as a
given, reducing their willingness to pay more for them.
In the below graph39, ( see Figure 2), you will see the relationship
between SaaS valuations and the 10-year treasury rate. It's evident
that SaaS valuations are highly sensitive to interest rate changes. Low
interest rates have historically encouraged investment and higher
valuations for growth-oriented SaaS companies. As rates rise,

39 https://cloudedjudgement.substack.com/p/clouded-judgement-8224-uncertainty
PRICE TO SCALE
165
however, the cost of capital increases, pressuring companies to prove
profitability and efficient cash flow management.

Fig.2 : SaaS Valuations vs. 10-Year Treasury Rate: The Impact of Interest
Rate Fluctuations
Given these insights, SaaS businesses must reconsider their pricing
strategies. Rather than merely adjusting prices in response to general
inflation, understanding how regime changes influence customer
behavior and investment becomes crucial. This knowledge allows for
optimizing operational efficiencies and realigning pricing models to
better match the economic conditions customers are facing.
Based on another piece of research by Jamin Ball40, for a cohort of
software companies the FCF (Free Cash Flow) has consistently gone
up in response to higher interest rates. See image below:

40 https://cloudedjudgement.substack.com/p/clouded-judgement-53124-software
AJIT GHUMAN
166

Fig.3 : Trends in Median Free Cash Flow (FCF) Margin from
Q1 2020 to Q1 2024
Efficiency in SaaS is also measured through metrics like revenue per
employee. The data in Jason Lemkin’s blog post indicates that the
average public SaaS company now generates about $300,000 in
revenue per employee41.
For some companies like Canva, this figure is even higher, reaching
$500,000 in revenue per employee even at $2B ARR and 4000
employees.
To put this into perspective, in the past year 2022-24, the benchmarks
for employee efficiency have risen significantly. In 2023, the average
revenue per employee for companies at scale was around $188,000.
This number has now increased, with companies like Canva setting
new standards. The higher revenue per employee indicates that each
employee is more productive, allowing companies to operate with
fewer people and better margins.
At the same time, for the same reason of trying to maximize margin
and cash flow, companies are also relooking at software spend.

41 https://www.saastr.com/the-new-normal-700-employees-at-200000000-in-arr/
PRICE TO SCALE
167
Median software NRR is now the lowest since 2020, see image below.
Here we see the other impact of increasing FCF, a close relook at
spend and thereby a concurrent impact on Churn and NRR.
>>>
