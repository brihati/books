# Chapter 16: Interviews & Case Studies With Top Pricing Leaders

## Detailed Chapter Summary

This chapter presents 15 interviews and case studies with leading pricing and revenue executives from major SaaS and software companies. The chapter serves as a practical compendium of real-world pricing strategies, challenges, and solutions implemented by companies including Nosto, Coupa Software, Mixpanel, Oracle, Verint, Rubrik, Zoom, Infoblox, Narvar, DocuSign, Pushpay, GitLab, and Coralogix.

### Nosto: Evolution Through Multiple Pricing Models

Kevin Paiser from Nosto describes the company's transition through three distinct pricing phases. Initially, Nosto operated on a **pay-on-performance model** (cost-per-acquisition) starting in 2013, where clients paid a percentage commission for each product recommendation click that converted within the same online session. While this was "ostensibly 'risk-free'" for merchants, "it was actually very risky" for the business due to revenue unpredictability.

After four or five years, Nosto transitioned to a fixed fee model (2017-18) with three tiers: Starter, Premium, and Enterprise plans. Revenue bands determined pricing (e.g., a merchant with $5 million average revenue fell into a specific band). This enabled product expansion and incentivized clients to use more products. The company subsequently introduced modular packaging with "Build Your Own" options, allowing clients to add products à la carte.

A critical challenge emerged: salespeople initially confused customers by "sending three or four pricing options," causing clients to "see too many numbers on the slide and get confused." The solution involved clear discount approval processes and a single, focused pricing presentation.

Services charging for implementation, onboarding, and training became an unexpected revenue stream—salespeople were initially hesitant about charging for previously free services, but "clients expected and accepted the fees." The main outcomes included predictability, increased average deal size, upselling opportunities for Customer Success, and a new services revenue stream.

### Coupa Software (Johnny Cheng): From Good-Better-Best to Modular Solution-Based Pricing

Johnny Cheng at Gainsight (acquired by Coupa) restructured broken mid-market pricing. The original **good-better-best model** ($1,000-$2,000-$3,000 packages) resulted in constant selling of the middle tier at the same ASP and created shelfware and downsells. Enterprise pricing was completely discrete, with sales making up prices inconsistently ranging from $5 to $1,000 per user—"it was just like the Wild West, whatever money they could get, they just went for it."

The solution involved a five-step packaging exercise: **List** all features (hundreds typically), **Group** into modules (natural groupings of features that sets of users commonly use together), **Test** against customer segments, **Rearrange** for MECE principle (Mutually Exclusive and Completely Exhaustive), and **Categorize** by sophistication, price point, value, adoption, and historical performance.

The result was "modular solutions (Lego pieces)": "Here are your Lego sets, you can put them together however you want." This packaged-plus-à la carte hybrid model maintained discrete pricing per module while enabling solution selling. Value metrics based on users and/or customers determined module pricing structure, with zero to two value metrics per module for flexibility.

### Mixpanel (Pranav Kashyap): From Events-Based to Monthly Tracked Users

Mixpanel operated on an **events-based pricing model** since 2009, where each item tracked on a website was an event sent by the customer and charged accordingly. The problem: customers couldn't predict event volume and didn't see business value correlated with event tracking. A customer might pay for 100 million events instead of 10 million but be "unable to find value," leading to churn.

In 2019, Mixpanel transitioned to **Monthly Tracked Users (MTUs)**—the number of unique users tracked monthly. This metric won evaluation because it "correlated most with revenue through regression analyses" and satisfied five criteria: **Predictable**, **Acceptable** to customers, **Trackable**, **Scalable**, and **Aligned with Value**.

The company identified three main customer segments with different use cases: Engineering/Product/Design teams wanted to know if they were achieving product-market fit; Data teams wanted to connect their stack; Marketing teams wanted A/B testing and email/push notifications.

The rollout strategy was **opt-in**, targeting customers most dissatisfied with the events model. Critically, "we wanted to see which of these metrics does best at keeping it cheap for a small company, by charging more for bigger companies." Revenue was kept flat during transition: "Look, if we assume that everyone was to move over to this new plan, we want to make exactly the same money. This is not a call to make more money off our customers."

A variant called **MTU Five** was introduced, where a user didn't count as one until they'd done five events, handling edge cases where ad campaigns inflated MTU counts with non-active users.

### Oracle (Natalie Louie): Mobile Messaging Pricing Complexity

Natalie Louie, head of Oracle Marketing Cloud Pricing Operations (2015-2018), tackled **SKU explosion** in mobile messaging. Initial complexity arose from multiple third-party telecom providers with different rates per country and region, creating **hundreds of SKUs** by country/region combinations. Customers like J. Crew, Apple, and others sending international mobile messages to US, Canada, Europe, and Japan each required separate SKUs.

Problems multiplied: text message responses incurred costs at different rates than initial messages; mobile charges had both directions of communication (sending and receiving) at two different rates. Customers struggled to predict costs and wanted flexibility to move unused credits between countries and channels.

The solution shifted burden from customer to Oracle: unified pricing across channels (SMS, email, display) with transparent hard cost exposure for mobile services through an aggregator marketplace. Coralogix implemented a **Cost Per Message (CPM)** fee uniformly across any messaging channel regardless of underlying hard costs.

Implementation required entire product re-architecture, creating significant internal resistance. Revenue goals were necessary to convince product management: "If we wanted to move the needle on revenue, this is how much we could bring in." The company revealed a sobering reality: "we were actually paying our aggregators more than we were collecting from the customer, because the customer had no idea."

### Verint (Rajeev Venkatraman): Perpetual to Subscription Transition

Verint, a legacy software company with **5,000 existing customers**, transitioned from perpetual licenses to subscription pricing. The pricing formula: **three years of perpetual license value plus maintenance at 18-20% for up to three years with 3-5% annual uplift**. Movement to cloud delivery added additional uplift due to offloaded hardware and IT costs.

The company shifted from seat-based to **named user/named employee-based licensing** for transparency. Critical insight: "Shift from perpetual to SaaS model can generate roughly 2x the maintenance revenue as average SaaS ACV." This opened access to previously unreachable market segments like DoorDash and Uber (Web 2.0/3.0 companies).

Research involved **20-40 customer samples across regions** and benchmarking with Salesforce, SAP, and Oracle. A critical principle: "measurement, tracking and reporting are of paramount importance" and "Customers need to understand exactly how we are measuring what they see in terms of usage."

Infrastructure matters: System inadequacies were major obstacles. Implementations required coordination across pricing, quote desk, order administration, and legal teams, with dedicated Sales Ops involvement essential for CPQ success.

### Pricing Tools and Operations

A consistent theme emerges: **pricing calculators** are used early in sales cycles for budgeting and rough numbers; **CPQ systems** scale as complexity grows and enable guidance selling. Natalie Louie noted: "CPQ is not a Deal Desk tool. It's a sales tool." Successful CPQ implementation requires partnership between pricing leader, sales ops, IT, and finance. "If you're missing any of the legs, it's guaranteed that implementation will be bad."

Revenue recognition (rev rec) is fundamental: "If you don't get rev rec right, your entire pricing falls apart." Rev rec must be coordinated across legal, contracts, billing, and quoting. Platforms like Zuora provide recurring revenue infrastructure handling CPQ, billing, usage data, payments, and tax—essential for managing metric-driven pricing and subscription lifecycle.

### Joshua Bloom (Simon-Kucher & Partners): Three-Phase Pricing Engagement

Joshua Bloom outlines the three phases of pricing projects: **Diagnostic** (establishing a straw-man view using internal data and pattern matching from competitors), **Primary Research** (conducting research with customers and prospects using specific scenarios—at least 80% of projects include this), and **Implementation** (customer migration strategy, change communication, sales training).

Different pricing challenges emerge at different company stages:
- **Early stage**: focuses on business model and pricing measures
- **Growth stage**: addresses packaging and multi-product complexity
- **Mature companies**: focus on pricing operations and discounting

Pricing structures exist on a spectrum from continuous consumption-based to fixed t-shirt sizing (M, L, XL). The good-better-best packaging model "assumes one linear upgrade path" and doesn't work for all portfolios. Selection should be driven by three factors: **metric predictability**, **usage growth rates**, and **correlation to underlying infrastructure costs**.

### Rubrik (Mehul Sahni): Perpetual to Subscription in Backup & Recovery

Rubrik disrupted the backup and recovery industry by simplifying from multiple hardware/software products to a single plug-and-play appliance. The company launched subscription pricing in **April 2019** after two-three years on a CapEx model with over 1,000 customers.

Subscription pricing was set at comparable levels to CapEx with slight premium, "similar to iPhone lease vs. outright purchase model"—there's "a little premium for that cash flow."

A six-month customer study identified three main pain points: high upfront CapEx costs, cloud migration mandates, and unpredictability around hardware refresh costs. The subscription model (Rubrik Go) included three solutions: prepay upfront option, license transferability between hardware and cloud, and a free evergreen hardware refresh program.

Critical mistake: Sales teams initially confused customers by presenting both CapEx and subscription simultaneously, "leading to deals being slowed." Solution: **Go/No-Go table** positioning only one model at a time based on customer type and budget constraints.

Value metrics for SaaS products are more strategic than for appliances "which remain tied to raw backend terabytes." The pricing page "is one of the most powerful messaging pages." Sales enablement must focus on understanding value metrics, packaging logic, and competitive positioning—not just price points.

### Infoblox (Kevin Christian): Three Legs of Pricing

Kevin Christian outlines a **pricing program** with three main areas:
1. **Strategy** (programs, policies, financial and market analysis)
2. **Transaction-level pricing** (Deal Desk and special discounts)
3. **Tools/Processes** (price setting systems and quoting)

Effective pricing models must be **Simple** (explainable in an elevator ride), **Measurable** (able to count what's being charged), and **Scalable** (capturing more returns as customer value scales). Four additional attributes: **Predictability**, **Flexibility**, operational ease of implementation, and **Fairness**.

IT infrastructure software historically priced based on hardware specifications under management. Public cloud providers like AWS and Azure introduced granular, elastic provisioning models. Traditional on-premise deployment charged based on hardware size specifications.

### NewCo Case Study: Hardware-Based to Consumption Pricing

The fictional NewCo operates in networking, IT asset management (ITAM), IT operations and automation (ITOA), and Information Security. Traditional IT Infrastructure deployment on physical systems created vendor distance from customers, leading to licenses matching infrastructure specifications.

Evolution: physical devices → virtual devices → cloud. Packaging evolved similarly: one/two point products → many point products → bundles → simplification to **Good-Better-Best (GBB)**.

NewCo implemented three packages: **Good** (minimal viable product), **Better** (vast majority), **Best** (sophisticated/complete). Sales teams can upsell from Essentials to Business to Advanced tiers. Growth opportunities emerge through pricing metrics/variables as customers expand usage.

Challenge: Different metrics across product lines (DNS Queries, Leases, number of assets, devices, users) created complexity requiring 15-16 bundles—"they are always going to need more of some item and less of some other. And even then they may feel they are overpaying for something."

Solution: Choose a single unified metric (e.g., IP addresses) for simplicity, even if theoretically suboptimal. "The field leadership wants to do big deals where the customer buys all the products... they would be using a suboptimal metric for some of the items, but the reason they were well advised to do it was to have the simplicity of the same metric for all the items."

Four critical implementation steps: pick the metric, build measurement capability, collect data in a data lake, present in a dashboard. "The lack of instrumentation when transitioning from licensing to metric driven subscriptions seems to get repeated across companies."

### Narvar (Ajit Ghuman): Failed Standardization and Recovery

Ajit Ghuman joined Narvar as Director/Head of Product Marketing in 2019 with focus on pricing. He discovered dissatisfaction in sales and marketing teams due to a failed prior pricing model—a CRO had implemented a new structure that failed (ASPs dropping, tiers not selected, high-end tiers heavily discounted) then left within months without iteration.

Core issue: Rapid pricing standardization without proper execution creates discord. SMB-style fixed-tier packaging doesn't work for enterprise sales teams accustomed to bespoke selling. Forced upgrades to higher tiers create shelfware and block upsell opportunities. "You can't change their needs or willingness to pay for your product; anything 'forced' will only backfire."

Narvar Track became de facto standard for shipment tracking, but the pricing model failed with 50-60% tier jumps for what should have been $3-5k add-ons. A fictional B2B product with 4 tiers where middle tiers restricted 'emails' and 'domains,' forcing SMB customers into Enterprise tier at high discount.

Recovery required extensive stakeholder alignment. "Listening and aligning perspectives" was "the most instructive in where the gaps were in the pricing model." The solution involved comprehensive interviews with sales representatives on how they created custom packages, reviewing Salesforce data on closed won/lost opportunities, and distinguishing packaging problems from core strategy issues.

Results: 100% sales adoption and 15-40% ASP increases across tiers. Key lesson: **Distinguish between packaging problems and core pricing strategy problems before making changes.**

### DocuSign: Usage-Based to Feature-Based Pivot

DocuSign initially used usage-based pricing based on envelope volume—customers were charged for each e-signature processed. As the e-signature market became saturated, technology commoditized. DocuSign faced the **four-phase commoditization cycle**:
1. **Innovative product launch**
2. **Low-price competition**
3. **Market bisection** (division into premium and budget segments)
4. **Revenue growth challenges**

"The commoditization of core features makes it difficult to maintain high margins, as customers become increasingly unwilling to pay a premium for features they can obtain elsewhere at a lower cost." Supporting features like automated workflows, integration capabilities, and advanced security became primary monetization drivers.

Transition to feature-based pricing faced resistance: Sales teams and CFO strongly resisted due to concerns about losing envelope upsell revenue. The gradual implementation strategy reduced risk. A **dual pricing metrics** approach served as transitional solution before full feature-based model.

Controlled price reduction per envelope stimulated volume while maintaining revenue. Aggressive volume discounting and site-license options encouraged broad adoption. By Q4 2023, DocuSign achieved $675 million revenue (vs. $469 million Q1 2022), 30,000 new customers (vs. 20,000), and 92% retention rate (vs. 85%).

Key insight: "Most innovative features eventually become commoditized, dropping in per-unit price and losing monetization capability." "Any pricing model is only appropriate and revenue-maximizing for a certain period of time."

### Zoom: Complexity Management Through Simplification

Zoom's rapid expansion between 2014-2020 led to **over 14 add-ons** and **1,000+ SKUs**, creating convoluted pricing structure impacting conversions. Product overload exceeded customer experience limits.

Strategic response: Establish dedicated Pricing Operations team, conduct **Conjoint studies** to optimize packaging, consolidate add-ons into main packages, and introduce the Zoom One bundle. Cross-functional **Tiger Team** collaboration (Sales, Customer Care, Product, Engineering, Accounting, Legal) ensured alignment. Iterative A/B testing validated findings.

Results: Zoom streamlined from 5-item product suite with 11 advertised add-ons to simplified offering. Zoom One bundle drove **115% net dollar expansion rate** among enterprise customers with **27% year-over-year growth** in customers contributing over $100,000 in trailing 12 months revenue.

### Pushpay: Proactive Price Reductions for Retention

Pushpay operated on subscription-based model with monthly recurring revenue (MRR) from subscription fees and transaction fees. Facing increasing churn due to competitive pressure, the company identified an alternative to premium feature development: **proactive price reductions for at-risk customers**.

Churn prediction based on five metrics: usage frequency, recent usage
