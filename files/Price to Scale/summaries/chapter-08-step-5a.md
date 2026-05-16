# Chapter 08: Step 5a – Pricing Operations

## Detailed Chapter Summary

**Step 5a** focuses on **Pricing Operations**, defined as all systems, processes, and people involved in ensuring a new pricing model is fully adopted across an organization so the sales engine works smoothly. The chapter emphasizes that while pricing strategy is the "easy part," pricing operations is where implementation challenges emerge, requiring 3–5 times more effort than strategy creation and typically taking at least a quarter (3 months) to implement meaningfully—not 4–6 weeks.

### Seven Core Operational Components

The chapter outlines seven foundational components required to operationalize a pricing model:

1. **Packaging Reference Doc** – A single source of truth documenting all pricing tiers, features, geographic availability, and constraints
2. **Website Pricing Decision** – A deliberate choice aligned with GTM strategy (not automatic publication)
3. **Team Structure** – Defined roles including Pricing Strategy, Pricing Ops, and Deal Desk functions
4. **Pricing Calculator** – A simple tool (Excel or Google Docs) enabling sales and cross-functional teams to calculate scenarios
5. **Quoting System/CPQ** – A system forcing guardrails so sales adhere to the pricing model
6. **Product Metering** – Infrastructure for consumption-based or usage-tracking models
7. **Discounting Guardrails** – Rules and matrices controlling discount authority by sales hierarchy level

### Website Pricing Publication Strategy

The chapter challenges the SaaS consensus that publishing pricing is inherently beneficial. Instead, the decision should align with overall GTM strategy:

- **High-velocity, transactional sales** (mid-market focused): Publishing pricing improves selling efficiency by enabling self-service discovery
- **Complex, low-velocity deals** (Global 2000, Fortune 500): Reserving pricing for sales conversations is more appropriate

Four options exist for website pricing pages: (1) full publication of all tiers and pricing; (2) summarized approach showing starting prices; (3) packages only without prices; (4) value-focused approach without pricing details.

### Pricing Page Case Studies

Four companies illustrate different approaches:

- **Ahrefs** – Charges $7 for trial plans (versus free trials with 2–6% conversion rates) to filter non-serious users and increase conversion; clearly lays out all plans comparatively; highest plan is $12,000/year
- **Aftership** – Uses 3-Part Tariff structure with slide scale visualization; sets overage prices higher than per-unit tariff prices to incentivize plan upgrades
- **Intercom** – Uses sub-tabs to segment pricing for different use cases
- **Basecamp** – Charges flat fee of $99/month regardless of usage, prioritizing deep customer retention over high-growth, high-burn models; focuses on SMB/mid-market segment with product-led growth

### Team Structure and Organizational Roles

Three distinct functional owners are required:

**1. Pricing Strategy**
- Creates or revamps pricing model
- Reports quarterly on model effectiveness against KPIs
- Serves as stakeholder interface
- Provides pricing consultation to sales representatives

**2. Pricing Ops (Operations)**
- Operationalizes pricing model through systems and processes
- Implements CPQ systems
- Coordinates with finance on billing
- Interfaces with legal on contracts
- Manages consumption models and overage billing
- Builds processes for expansion/renewal motions

**3. Deal Desk**
- "Last mile" function ensuring latest price book is used by sales
- Provides fast turnaround on requests
- Controls discount approval authority
- Critical to successful pricing model rollout

The chapter emphasizes that the term **Monetization Team** is more accurate than "Pricing Team," reflecting broader responsibilities: market segmentation, competitive positioning, product bundling decisions, and pricing strategy development. This team is often understaffed and requires executive sponsorship.

### Pricing Calculators and CPQ Systems

**Pricing Calculators** (Excel or Google Docs) serve as powerful enablement tools for sales, product, operations, and finance teams to calculate pricing scenarios. Key design principles:

- Invest significant time in UI design—as much as in formulae and reference tables
- Keep formulas simple and modular, referring to intermediate tables rather than long chains
- Maintain transparent formulas that executives can understand and trust
- Treat calculators as software requiring versioning and updates, not static documents
- Use protected sheets that reps copy when releasing updates

Building a comprehensive calculator (Narvar example) required over 2 weeks to cover all pricing scenarios and ensure sales rep usability.

**CPQ (Configure-Price-Quote)** systems impose guardrails forcing sales reps to adhere strictly to the pricing model. However:

- Implementation typically takes **2–3 times longer** than initially estimated
- Sales rep involvement during build phase is critical for adoption
- Fast-growing companies with evolving pricing may not benefit from heavy CPQ investment
- Spreadsheet-based calculators are recommended until companies reach approximately **15–20M in revenue**

Complexity in pricing tools slows deals; simplicity allows reps to defend price points effectively.

### Discounting Strategy and Authority

Discounting is a key B2B software pricing tool enabling flexibility across customer segments. Expected discounting ranges by segment:

- **Commercial**: 10–30%
- **Mid-sized**: 20–50%
- **Enterprise**: 30–70%

Companies should build padding into list prices accordingly (10–30% for commercial, 20–50% for mid-market, 30–70% for enterprise).

A **Discounting Matrix** allocates progressively higher discount authority to different sales hierarchy levels (account executives → managers → leadership). This built-in friction ensures higher discounts appear earned or negotiated rather than freely given—preserving their perceived value.

Discounting should be evaluated on two dimensions:
1. Customer behavior impact (higher close rates, faster sales cycles, longer commitments, multi-product purchases)
2. Correlation with sales performance (patterns should match customer attributes, not individual rep behavior)

### Pricing Analytics and Performance Measurement

Companies should measure six core metrics quarterly:

1. **Average Selling Price (ASP)** – Board-level revenue metric offering directional product-line performance information
2. **Median Selling Price** – Helpful when small deal samples allow outliers to swing ASP
3. **Number of Deals Closed** – Normalizes ASP impact
4. **Unit Price** – Dollar per seat/unit consumption; indicates pricing power independent of deal mix
5. **Average Volume Sold** – Quantity per deal
6. **Discounting %** – Indicates if price points are too high or too low

Data must be segmented by product family, package sold, add-ons, geography, sales sub-team, sales owner, closed quarter, and prospect attributes for actionable insights.

Perfect attribution is difficult (multiple variables change quarterly); instead, evaluate success by whether the model solves old problems: reduced ASPs, shelfware, and low package adoption.

---

## Key Points

- Pricing operations is where implementation challenges occur; strategy creation is the easy part
- Implementation requires **3–5x effort** of strategy creation and at least **one quarter** (not 4–6 weeks)
- Seven core components are required: Packaging Reference Doc, Website Decision, Team Structure, Calculator, CPQ, Product Metering, and Discounting Guardrails
- Website pricing publication should align with GTM strategy, not be automatic
- Mid-market transactional sales benefit from published pricing; enterprise low-velocity deals should reserve pricing for sales conversations
- Three functional owners needed: Pricing Strategy, Pricing Ops, and Deal Desk
- **Deal Desk is the critical "last mile" function** determining pricing model rollout success
- A centralized **Pricing and Monetization team** resolves strategic inconsistencies across functions (Product, Sales, Marketing, Finance, Legal)
- Pricing calculators (spreadsheet-based) are sufficient through ~15–20M revenue; CPQ implementation takes 2–3x longer than estimated
- **Complexity kills deals**; simplicity allows sales reps to defend price points
- Discounting ranges by segment: Commercial 10–30%, Mid-sized 20–50%, Enterprise 30–70%
- **Discounting matrices** allocate authority across hierarchy; friction makes discounts appear earned
- Six quarterly metrics track pricing performance: ASP, Median Price, Deal Count, Unit Price, Volume, and Discounting %
- Data segmentation is essential for actionable insights
- Trial conversion rates improve when charging nominal fees ($7) versus free trials (2–6% conversion)
- Overage prices should exceed per-unit tariff prices to incentivize plan upgrades
- Flat-rate pricing can support product-led growth and may correlate with higher retention

---

## Important Examples and Stories

**Natalie Louie, Sr Director of Product Marketing at Zuora:**
> "pricing strategy is the easy part. Pricing operations, that is where you start pulling out your hair. And that's where all you're faced with is 'no'. 'No, we can't do that.' 'No, we can't do this'"

**Ahrefs Pricing Case Study:**
- Charges $7 for trial plans to filter non-serious users
- Highest plan is $12,000/year
- Lays out all plans clearly and comparatively

**Aftership Pricing Case Study:**
- Uses 3-Part Tariff structure with slide scale visualization
- Sets overage prices higher than base unit tariff prices to incentivize upgrades

**Intercom Pricing Case Study:**
- Uses sub-tabs to segment pricing for different use cases

**Basecamp Pricing Case Study:**
- Flat fee of $99/month regardless of usage
- Focuses on SMB/mid-market with product-led growth
- Prioritizes deep customer retention over high-growth, high-burn model
- Eschews Silicon Valley high-burn startup model in favor of lifestyle business approach

**Narvar Pricing Calculator:**
- Revamp took over 2 weeks to cover all pricing scenarios
- Demonstrates significant time investment required for usable tools

**Strategic Inconsistency Example:**
- Product team building premium features while Marketing pursues high-volume leads represents clash between revenue-per-account and high-volume, low-cost models

---

## Definitions and Terms

| Term | Definition |
|------|-----------|
| **Pricing Operations** | All systems, processes, and people involved in ensuring the new pricing model is fully adopted across an organization so the sales engine works smoothly |
| **Packaging Reference Doc** | One production-ready place where a company's pricing resides; always referencible and providing complete guidance on features and constraints |
| **Pricing Strategy** | Role involving creation/revamping of pricing model, quarterly performance reporting, stakeholder interface, and pricing consultation with sales reps |
| **Pricing Ops** | Heavy-duty function creating processes and systems to operationalize pricing model; includes CPQ implementation, finance interfacing, billing understanding, and legal coordination |
| **Deal Desk** | "Last mile" function ensuring latest price book is used by sales, providing fast turnaround on requests, and controlling discount approval authority |
| **Monetization Team** | Broader designation than "Pricing Team" reflecting responsibilities including market segmentation, competitive positioning, and product bundling |
| **CPQ (Configure, Price, Quote)** | System allowing sales reps to configure packages, generate pricing quotes with discount approvals, and contractual paperwork in automated process for fast deal closure with transparency |
| **3-Part Tariff** | Pricing structure used by Aftership with slide scale visualization and overage fees |
| **Pricing Calculator** | Simple tool in Excel or Google Docs serving as enablement tool for sales, product, operations, and finance to calculate pricing scenarios |
| **Discounting Matrix** | Standard operational document specifying discount authority levels different sales people have to offer customers |
| **Average Selling Price (ASP)** | Board-level revenue metric offering directional information on product-line performance |
| **Unit Price** | Dollar amount per seat or per unit consumption; indicates pricing power of product or package |
| **Revenue Leakage** | Unnecessary discounting that does not yield desired results |
| **Product-Led Growth** | Go-to-market approach where product itself drives customer acquisition (vs. sales-led) |
| **GTM (Go-To-Market)** | Overall strategy for how company reaches and sells to customers |
| **Shelfware** | Software purchased but not actively used by customers |

---

## Names, Dates, Numbers, and Places

### Names
- **Natalie Louie** – Sr Director of Product Marketing at Zuora
- **Ajit Ghuman** – Author; pricing operations practitioner
- **Johnny Cheng** – Contributor on CPQ discussion
- **Marcin Krzych** – Contributor on CPQ and discounting discussion

### Companies/Products Mentioned
- **Zuora** – Subscription billing software (Natalie Louie's company)
- **Citrix** – Enterprise software company
- **Ahrefs** – SEO and content marketing tool
- **Aftership** – Logistics and shipping software
- **Intercom** – Customer communication platform
- **Basecamp** – Project management software
- **Zendesk** – Customer support platform
- **Narvar** – Post-purchase experience platform (author's example)

### Numbers and Metrics
- **3–5x** – Effort multiplier of implementation vs. strategy creation
- **3 months (quarter)** – Minimum meaningful rollout time
- **4–6 weeks** – Insufficient implementation timeline
- **2–3x** – Time multiplier for CPQ implementation beyond estimates
- **2 weeks** – Time required to build comprehensive pricing calculator (Narvar example)
- **2–6%** – Free trial conversion rates
- **$7** – Ahrefs trial plan charge
- **$12,000/year** – Ahrefs highest plan
- **$99/month** – Basecamp flat fee
- **10–30%** – Commercial segment discounting range
- **20–50%** – Mid-sized segment discounting range
- **30–70%** – Enterprise segment discounting range
- **15–20M** – Revenue threshold for transitioning from spreadsheet to CPQ
- **40–50%** – Recommended padding in list prices for high-discount segments

### Places/Regions
- **AMER** – Americas region
- **UK/EU** – United Kingdom and European Union regions
- **Global 2000** – Top 2,000 global companies by revenue
- **Fortune 500** – Top 500 U.S. companies by revenue
- **Silicon Valley** – Technology industry center (referenced regarding startup models)

### Dates
- **COVID-19** – Example of external market condition significantly reducing deal volume

---

## Short Relevant Quotes or Standout Statements

> "pricing strategy is the easy part. Pricing operations, that is where you start pulling out your hair."
— Natalie Louie, Zuora

> "Not even the best pricing model can yield any result if it's not operationalized to enable a smooth sales process and 100% adoption by the sales, professional services, ops and finance teams."

> "Be kind to the people in this role, they are often short staffed and need a good amount of enablement as well as sponsorship to fill the role properly."
— On Deal Desk and Pricing Operations teams

> "My fundamental belief is that in order to do value selling, you need a lot of flexibility, a ton of flexibility"

> "complexity is a deal killer, it slows down deals, complexity makes it so that the reps can't defend the deal"

> "Ahrefs leaves nothing to conjecture. They lay out all their plans clearly and comparatively."

> "Free trial conversion rates are historically really poor to convert (2–6%) and take a significant amount of resources to sustain."

> "The overage price ends up being more than the per unit price of the tariff structure to incent customer to move up in plans"

> "I find Basecamp's pricing to be truly unique and somewhat of a mold breaker."

> "Think of Pricing not only as a function responsible for delivering the new line-up design but also as a key player in uncovering opportunities for organizational alignment"

> "Establishing a centralized owner for pricing can greatly enhance a company's ability to align its various functions and optimize for value"

> "you may still need to do this, I would personally live on a Google spreadsheet based calculator until ~15–20M revenue"

> "This is the closest tool that lets us reach a price optimized local maxima that can account for variations in price elasticity between customers"

> "Just remember a little friction goes a long way, a lot of friction leads to a disgruntled sales team and customers who balk at the initial number they see"

> "Higher discounts must appear to prospects as being earned or negotiated and not just given away by any sales representative"

> "Basecamp has always eschewed the high-growth, high-burn Silicon Valley startup model, opting instead for a close to lifestyle business approach"

---

## Actionable Lessons

### Packaging and Documentation
1. Create a **Packaging Reference Doc** listing features by tier, geographic availability, constraints, and implementation notes
2. Update the packaging grid **quarterly** as a single source of truth
3. Make deliberate decisions about website pricing publication based on GTM strategy, not automatic adoption
4. Choose one of four website pricing approaches: full publication, summarized with starting prices, packages only, or value-focused

### Implementation Timeline and Effort
1. Allocate **at least one quarter (3 months)** for meaningful rollout—not 4–6 weeks
2. Plan
