# Chapter 7: Step 4 - Rate Setting

## Detailed Chapter Summary

**Step 4: Rate Setting** focuses on determining how much to charge for products through a systematic framework examining five pricing factors: Prospect Willingness To Pay (WTP), Competitive & Category Price Points, Cost of Delivery, Discounting For Procurement, and Pricing Strategy.

### Discovering Willingness To Pay

When market feedback is lacking, the chapter presents three primary methods for discovering WTP: surveys, conjoint analysis, and in-person interviews.

**Basic Pricing Survey** uses two anchoring questions to avoid bias from direct price inquiries. Rather than asking customers how much they would pay (which produces unreliable answers), the approach asks at what price the product becomes too expensive and at what price it becomes so cheap that quality is doubted. Data from these questions is converted to cumulative percentages and plotted to identify the Optimal Price Point (OPP)—the price where the highest percentage of people view it as neither too low nor too high.

**Van Westendorp Price Sensitivity Analysis** (also called Price Sensitivity Meter) establishes acceptable price ranges rather than single points. The method identifies two critical intersection points: the Price of Marginal Cheapness (PMC), where equal numbers think the product is too cheap versus not a bargain, and the Price of Marginal Expensiveness (PME), where equal numbers think it is too expensive versus not expensive. While Van Westendorp appears rigorous and provides directional guidance, it has limitations: it doesn't account for competitive prices or profit margins, survey respondents may not represent the eventual market, and it cannot estimate the relative value of different features.

**Conjoint Analysis** determines how customers value different product attributes and features through survey-based choice experiments. The method identifies key attributes (product dimensions like brand, data allowance, or cost) and their levels (specific values assigned to those attributes). Respondents evaluate profiles—specific combinations of attributes and levels—and their preferences generate quantitative measures called preference scores or partworth utilities. Multiple variations exist including Choice Based Conjoint (CBC), Adaptive Choice Conjoint, and Adaptive CBC (ACBC). Conjoint analysis is relatively inexpensive, can answer multiple business questions from one dataset, but requires large sample sizes and takes 2-3x longer than Van Westendorp analysis. It is best suited for simple products with online sales channels; complex enterprise products require qualitative research instead.

### Qualitative Research for Complex Products

For complex or enterprise products, conducting 5-10 to 40-50 customer interviews is more effective than quantitative methods. The chapter provides a structured interview template that sequences exploration strategically: establishing pain points through forced-ranking of pre-created statements, conducting a 15-20 minute product demo after validation, and analyzing packaging benefits using a $100 distribution exercise where customers allocate funds among package tiers to identify best fit.

Post-interview debrief uses 0-to-10 scale ratings for customer fit and purchase willingness. Customers should be probed on actual likelihood to purchase and urgency, not merely acceptance of positioning. All customer data should be compiled with firmographic data (revenue, employee size) for context.

### Analyzing Existing Customer Pricing Data

The chapter emphasizes using historical customer data to understand market pricing, discounting patterns, and segment-based pricing. Analysis should rank-order customers by pricing and calculate unit pricing (ACV divided by unit volume) to reveal patterns. In B2B software, commercial deal discounting up to 20% and enterprise discounting up to 80% are normal expectations. Large customers typically pay 2-10x more than small customers, though list prices are usually 30-50% higher than actual per-account ARR for large customers.

Feature usage analysis validates packaging by showing which features correlate with premium pricing. When analyzing 5-7 critical features, patterns often emerge showing customers pay unit price premiums when more features are used. Higher-end features should be reserved for higher-end packages. However, the chapter cautions against extrapolating from historical ad-hoc pricing data when changing pricing variables, structure, or segments.

### ROI-Based Pricing: A Cautionary Discussion

While theoretically attractive, ROI-based pricing is unreliable in practice. Most successful software companies (Salesforce, Workday, Google) do not sell based on ROI. The approach fails because organizations cherry-pick their best customers for case studies, it is difficult to isolate software's impact from other company factors, and buyers approach ROI arguments with skepticism. Examples of published ROI claims include Snowflake (612% ROI, $21 million benefits), New Relic (120% ROI), DataRobot (514% ROI), Snaplogic (498% ROI), Qualtrics (633% ROI), and Twilio (277% ROI)—claims that lack credibility because switching costs and productivity gains are rarely properly measured. ROI is better used for price justification than for actual pricing decisions.

### Market Type and Pricing Strategy

Pricing strategy depends significantly on market type. In **Blue Ocean** markets (products replacing a different way of doing things with less head-to-head competition), the same company may charge different customers 5-10x different prices. In **Monopolistic** markets (one dominant company like Zendesk or Salesforce setting benchmarks), smaller players exist only at margins and pricing becomes anchored to the incumbent's price point (e.g., Salesforce's $150/seat anchor in CRM). In **Renaissance** markets (multiple small players vying for dominance with no clear leader), focus shifts to pricing agility and serving your ICP rather than finding an exact price point.

### Cost Considerations in SaaS Pricing

Software pricing should be based on perceived value to customers, not cost of production. A critical distinction exists between average cost (total expenditure spread across users) and marginal cost (cost of providing service to one additional user). In SaaS, many costs—development, infrastructure, support—are fixed and do not scale with users, making marginal cost significantly lower than average COGS. Relying solely on average cost can lead to overestimating acquisition costs and missing growth opportunities in price-sensitive segments. Understanding marginal cost reveals opportunities for more aggressive pricing, including freemium tiers.

Companies should evaluate whether market segments are viable by analyzing setup costs, deal sizes, and acquisition costs together. Implementation costs typically represent 10-15% of software ACV as an industry standard. When third-party consumption costs are high (e.g., SMS at 12 cents per message), they should be priced separately using consumption-based models.

### Three Strategic Pricing Approaches

There are three main pricing strategy intents: **margin maximization** (prioritized by enterprise-focused products), **revenue optimization** (finding the middle path), and **market-share maximization** (prioritized by bottom-up products). Getting the pricing structure right matters more than the specific price point. The structure establishes the fundamental economics of acquiring and servicing customers, which determines SaaS business success.

---

## Key Points

- **Five pricing factors** drive rate setting: WTP, competitive price points, cost of delivery, discounting, and pricing strategy
- **Avoid direct price questions** due to customer bias; use anchoring questions instead
- **Van Westendorp Analysis** establishes acceptable price ranges via PMC and PME intersection points
- **Optimal Price Point (OPP)** is where highest percentage view price as neither too low nor too high
- **Conjoint analysis** quantifies how customers value different product attributes through preference scores
- **Limit conjoint to 6-7 attributes** and ensure respondent understanding of attribute levels
- **Qualitative interviews (5-10 to 40-50)** are superior for complex enterprise products
- **Large customers typically pay 2-10x more** than small customers
- **Unit pricing analysis** (ACV/unit volume) reveals pricing distribution across segments
- **Feature usage patterns** should align with package tiers based on customer analysis
- **ROI-based pricing fails** in practice despite theoretical appeal; most large software companies don't use it
- **Market type determines pricing freedom:** Blue Ocean allows 5-10x variation; Monopolistic anchors to incumbent; Renaissance requires agility
- **Marginal cost is significantly lower** than average cost in SaaS, enabling aggressive pricing strategies
- **Cost-plus pricing doesn't work** for software due to minimal production costs per user
- **Pricing structure matters more** than specific price points for long-term business success

---

## Important Examples and Stories

**Pricing Survey Example:** In a basic pricing survey, $40 per unit was not considered too low by 75% of respondents; 50% thought $70 was too high; at $50, 85% considered it neither too low nor too high.

**Mobile Phone Pricing:** Conjoint analysis applied to mobile plans with attributes like brand, data allowance, cost, and contract duration to understand how customers value different features.

**SaaS Package Distribution:** A fictional SaaS product tested 'Good', 'Better', 'Best', and 'Best+' packages with different take rates and revenue impacts through customer interviews.

**Customer Pricing Analysis:** Hypothetical example with 10 customers showing large customers pay ~$0.60 per unit while smaller customers pay ~$2.10 per unit; features 4 and 5 used only by larger customers with higher ACVs.

**Implementation Cost Reality:** SMB-focused app with $3,000 average implementation costs on $1,000-$10,000 annual deal sizes and $1,000-$3,000 acquisition costs per customer demonstrates viability challenges.

**ROI Case Studies (Published Claims):**
- Snowflake: 612% ROI, $21 million benefits over 3 years
- New Relic: 120% ROI, $13.3M benefits vs. $6M costs
- DataRobot: 514% ROI, payback within 3 months
- Snaplogic: 498% ROI, $3.9M benefits PV over 3 years
- Qualtrics: 633% ROI, $38.4M benefits over 3 years
- Twilio: 277% ROI, $9.2M NPV

**CEO Interview Story:** An executive questioned correlation versus causation in software ROI, criticizing how companies take credit for success when software was only one small piece of broader company performance.

**Historical Market Example:** In Blue Ocean markets, a national bank may pay 5-10x more than a national retailer for the same product based on differential value perception.

---

## Definitions and Terms

**Prospect Willingness To Pay (WTP):** The price prospects are willing to pay for a product.

**Optimal Price Point (OPP):** A singular price point where the highest percentage of people think the price is neither too low nor too high.

**Price of Marginal Cheapness (PMC):** The price intersection where equal numbers think the product is too cheap and not a bargain.

**Price of Marginal Expensiveness (PME):** The price intersection where equal numbers think the product is too expensive and not expensive.

**Van Westendorp Price Sensitivity Analysis:** A pricing survey method that establishes price perceptions by asking four questions about price acceptability to identify acceptable price ranges rather than single points.

**Conjoint Analysis:** A survey-based research technique that determines how people value different attributes (features, functions, benefits) of a product or service through choice modeling.

**Attributes:** Dimensions of the product (brand, size, performance, price) or pricing plans that drive customer decision-making.

**Levels:** Specific values that an attribute may be assigned, either real for existing products or proposed for new designs.

**Profile:** A specific combination of attributes and levels shown to respondents for evaluation.

**Preference Score / Partworth Utility:** Quantitative measures obtained from conjoint survey results showing the value of each attribute.

**Choice Based Conjoint (CBC):** A variation of conjoint analysis for larger groups or complex analyses.

**Adaptive Choice Conjoint:** A variation of conjoint analysis using automated platforms.

**Adaptive CBC (ACBC):** An advanced variation combining adaptive and choice-based approaches.

**Pricing Metric:** The unit used to determine pricing (e.g., per seat model or usage-based model).

**Ideal Customer Profile (ICP):** Target profile for sales motion optimization.

**Average Cost:** Total expenditure spread across all users, giving a broad view of cost structure.

**Marginal Cost:** Cost of providing service to an additional user or seat, usually significantly lower than average COGS in SaaS.

**Cost-Plus Pricing:** Approach adding a margin amount to cost of production.

**Blue Ocean Market:** Product replacing a different way of doing things with lesser head-to-head competition.

**Monopolistic Market:** One dominant company sets benchmark for functionality and price, with smaller players existing only at margins.

**Renaissance Market:** Multiple small players vying for dominance with no clear leader, converging pricing variables and similar value propositions.

**Consumption Model:** Pricing based on usage of a specific capability or service.

**Volume Discount:** Price reduction for customers using more service or buying more licenses/seats.

**Unit Pricing:** ACV divided by unit volume.

**Negative Discounting:** Selling at prices higher than list price.

**Total Economic Index (TEI):** A Forrester method for demonstrating ROI through external consultant studies.

**B2B Software Discounting Standards:** Commercial deal discounting up to 20%; enterprise deal discounting up to 80%.

---

## Names, Dates, Numbers, and Places

**Names:**
- Ajit Ghuman
- Van Westendorp
- Green and Wind
- Kuzmanovic et al.
- Tomas Tunguz
- Jan Pasternak

**Software Companies & Benchmarks:**
- Salesforce (CRM, $150/seat pricing anchor)
- Workday
- Google
- Zendesk (customer service)
- Slack
- Yammer
- Snowflake
- New Relic
- DataRobot
- Snaplogic
- Qualtrics
- Twilio
- Marriott Courtyard

**Research & Technology Platforms:**
- Sawtooth Software
- Conjoint.ly
- Qualtrics
- GLG (expert networks)
- Forrester

**Dates:**
- 1989 (Green and Wind Marriott Courtyard conjoint analysis)
- 1980s (early conjoint analysis with physical cards)

**Numbers & Metrics:**
- **Pricing Examples:** $40, $70, $50 per unit
- **Survey Results:** 75%, 50%, 85% response rates
- **Tariff Structures:** 2-part tariff, 3-part tariff
- **Conjoint Parameters:** 6-7 attributes (maximum), 2-4 profiles
- **Interview Ranges:** 5-10 to 40-50 customer interviews
- **Demo Duration:** 15-20 minutes
- **Scales:** 0-to-10 scale (customer fit and purchase willingness)
- **Customer Pricing Variance:** 2-10x difference between large and small customers
- **Price Discounting from List:** 30-50% for large customers
- **Deal Discounting Standards:** 20% (commercial), 80% (enterprise)
- **Unit Pricing Examples:** $0.60 (large customers) vs. $2.10 (small customers)
- **Implementation Costs:** 10-15% of software ACV (industry standard), $3,000 average in competitive segments
- **ROI Claims:** 612% (Snowflake), 120% (New Relic), 514% (DataRobot), 498% (Snaplogic), 633% (Qualtrics), 277% (Twilio)
- **Benefit Dollar Examples:** $21M (Snowflake), $13.3M (New Relic), $38.4M (Qualtrics), $12.6M (Twilio)
- **Time Multiplier:** 2-3x longer for conjoint vs. Van Westendorp
- **SMS Cost Example:** 12 cents per SMS

---

## Short Relevant Quotes or Standout Statements

**On Direct Price Questions:**
- "It usually doesn't work to ask a customer how much they'd pay for a given product because the answers may get actively biased too low."
- "Without reference points, a singular price point answer may not be very revelatory as the customer essentially is just guessing."

**On Van Westendorp Analysis:**
- "The resultant price 'space/range' helps to determine the range of acceptable prices."
- "Essentially giving us some reasonable bounds to play inside."

**On Feature Valuation:**
- "Neither approach lets us estimate the relative value of different features or capabilities."

**On Conjoint Complexity:**
- "Be mindful of the customers' limitations in being able to engage with your analytical approach at a very detailed level of granularity."
- "Customers should be able to understand the full value in a few minutes."

**On Interview Scope:**
- "We aim to interview a representative sample of our customer/market base, which can be as few as 5-10 interviews to up to 40-50 interviews."

**On ROI-Based Pricing:**
- "Mr Customer, I will aim to deliver you 5x to 10x ROI and in return I only want [1% to 10%] of the benefits accrued to you."
- "If we reflect on the most successful software companies, the very largest, very few sell based on ROI."
- "Many times these ROI calculations assert unquestionable numbers. But most buyers approach these kinds of arguments with skepticism and even cynicism."
- "So if you base
