# Chapter 12: Usage-Based Pricing

## Detailed Chapter Summary

Usage-Based Pricing (UBP) is a compelling pricing model that sounds attractive in theory but requires careful, nuanced implementation that is often underestimated by industry participants. While UBP is marketed as a panacea for SaaS companies, it is not universally appropriate and demands thorough analysis of market fit, product type, and organizational readiness.

### Core Concept and Market Appeal

UBP is defined as paying based on a specific pricing metric that is related or specific to the use of the product. The pitch of "paying only for what you use" is inherently compelling to buyers and markets very well. However, the underlying mathematics and implementation are significantly more complex than surface-level appeal suggests.

### Three Key Learnings

**1. Market Suitability and Customer Expectations**

Market and customer expectations matter more than the surface-level appeal of UBP. Not all companies and products are suitable for this model despite positive industry coverage. The author personally experienced a situation where executives pitched grandiose UBP strategies that would have caused a 50% revenue loss for their former product line, necessitating a rollback fight. Additionally, competitors adopting UBP can create FUD (Fear, Uncertainty, Doubt) that leads companies to chase unsuitable pricing models. The author's own competitive experience showed that customer analysis revealed a competitor's UBP move was inappropriate for a capability purchase category, yet it created internal pressure nonetheless.

**2. Product Type Alignment: Capability Purchases vs. Consumption Services**

Products purchased as capabilities—items that are needed but not used frequently—are poor fits for UBP models. The example of car purchases illustrates this principle: despite infrequent usage, shifting automobiles to usage-based pricing would not work because buyers expect to own a capability. Similarly, Kustomer's CEO was unable to innovate with pricing strategy because customer service software buyers expected traditional $ per agent pricing, revealing market expectations that override internal strategy desires. Salesforce app sellers are naturally compared to Salesforce's $ per user pricing model, constraining pricing flexibility. Conversely, data plans from Verizon and AT&T successfully employ usage-based pricing because they align with consumption patterns and customer expectations.

**3. Revenue Predictability and Valuation Challenges**

UBP reduces revenue and valuation predictability compared to subscription models. The fundamental valuation model of subscription-based software does not directly apply to usage-based companies. Traditional SaaS valuation multiples cannot be applied to variable revenue streams, and traditional metrics like ARR (Annual Recurring Revenue) and MRR (Monthly Recurring Revenue) may not fit well with usage-based models. Some analysts suggest "trailing spend" as an alternative metric.

The Snowflake case exemplifies these risks: In May 2023 (FY24 Q1), despite posting solid headline and bottom-line numbers that beat consensus expectations, Snowflake lowered its FY24 revenue growth outlook for a second time within two quarters, causing the stock to tumble approximately 13% after hours. The company pointed to degrading consumption patterns and a lack of predictability of when headwinds might subside as key reasons for the revision. While Snowflake achieved impressive Net Revenue Retention (NRR) rates of approximately 130% with UBP, the consumption model introduced unpredictability that traditional subscription companies do not face.

### Operational Complexity

Implementation of UBP requires metering, CRM/CPQ/ERP/Billing system integration, and is significantly more complex than subscription models, particularly in larger established organizations. The implementation timeline can span from 4 months to 2 years. The most ideal pricing strategy is certainly not always the best for an organization when operational readiness is considered.

### Sales and Compensation Restructuring

Sales compensation structures must be fundamentally rethought for UBP. Commission models must shift to be based on account growth when the initial sale price is minimal under UBP. The author experienced a situation where enterprise sellers refused to surface UBP to buyers until sales compensation questions were clarified. Sales forecasting becomes critical and difficult under UBP due to revenue unpredictability, and sales teams will not adopt UBP without clarity on compensation structure and payment timing.

### Revenue Predictability Within UBP

Tariff structures can provide some revenue predictability within UBP models. Linear pricing, 2-part pricing, and 3-part pricing are structured approaches that balance consumption-based mechanics with revenue stability.

---

## Key Points

- UBP sounds compelling but requires nuance in implementation that isn't obvious initially
- UBP is not appropriate for all companies and products despite positive industry coverage
- Market and customer expectations constrain the viability of UBP adoption more than the appeal of the model itself
- Capability purchases with low usage are not suitable for UBP models
- UBP reduces revenue and valuation predictability compared to subscription models
- Traditional SaaS valuation multiples cannot be directly applied to usage-based companies
- Tariff structures (linear, 2-part, 3-part) can provide revenue predictability within UBP
- Operational implementation of UBP requires metering and system integration (CRM/CPQ/ERP/Billing)
- Sales compensation structures must be rethought for UBP with commission models based on account growth
- Sales forecasting becomes critical and difficult under UBP due to revenue unpredictability

---

## Important Examples and Stories

**Snowflake's Valuation Challenges**
In May 2023 (FY24 Q1), Snowflake reported solid headline and bottom-line numbers that beat consensus expectations. However, the company lowered its FY24 revenue growth outlook for a second time within two quarters, citing degrading consumption patterns and unpredictable headwinds. This caused the stock to tumble approximately 13% after hours. Despite achieving ~130% NRR with UBP, the consumption model created unpredictability that subscription models avoid.

**Kustomer's Pricing Strategy Constraints**
Kustomer's CEO was unable to innovate with pricing strategy because customer service software buyers expected $ per agent pricing. This demonstrates how market category norms override internal strategic preferences.

**Internal Revenue Loss Risk**
The author had to fight to roll back executives' grandiose UBP pitches that would have caused 50% revenue loss for their former product line.

**Competitor FUD Impact**
The author personally experienced a competitor moving to UBP creating FUD in their company's executives, but customer analysis showed the competitor's product was actually a capability purchase unsuitable for UBP.

**Sales Team Resistance**
The author's experience launching UBP found that enterprise sellers refused to surface UBP to buyers until sales compensation questions were clarified.

**Product Category Examples**
- **Car purchases**: Are capability-based despite infrequent usage; shifting to usage-based pricing would not work
- **Salesforce app sellers**: Are naturally compared to Salesforce's $ per user pricing model
- **Verizon and AT&T data plans**: Successfully employ usage-based pricing aligned with consumption expectations

---

## Definitions and Terms

- **Usage-Based Pricing (UBP)**: Paying based on a specific pricing metric that is related or specific to the use of the product
- **Capability Purchase**: Products bought as capabilities that are needed but not used frequently
- **Net Revenue Retention (NRR)**: A metric measuring how much revenue from existing customers grows over time, including expansion and churn
- **Pricing Metric**: The specific unit of measurement used to calculate usage-based charges
- **Tariff Structure**: Predefined pricing tiers within UBP models (linear, 2-part, 3-part)
- **Linear Pricing**: Simple usage-based pricing with a single rate per unit
- **2-Part Pricing**: Fixed base fee plus variable usage charges
- **3-Part Pricing**: Fixed base fee, tiered usage rates, and potentially other variable components
- **Consumption Model**: Pricing based on actual product consumption/usage patterns
- **Subscription Model**: Recurring fixed-price billing model (contrasted with consumption-based)
- **ARR (Annual Recurring Revenue)**: Annual value of recurring revenue subscriptions (may not fit UBP models)
- **MRR (Monthly Recurring Revenue)**: Monthly value of recurring revenue subscriptions (may not fit UBP models)
- **Trailing Spend**: Suggested alternative metric for usage-based pricing models
- **Revenue Predictability**: Ability to forecast and predict future revenue streams
- **FUD (Fear, Uncertainty, Doubt)**: Competitive pressure created through uncertainty
- **Metering**: Technology infrastructure for tracking and measuring product usage
- **CPQ (Configure Price Quote)**: Enterprise software for configuring products and generating quotes
- **CRM (Customer Relationship Management)**: System for managing customer relationships and interactions
- **ERP (Enterprise Resource Planning)**: System integrating business processes across an organization
- **Feature Flag**: Software development technique for toggling features on/off
- **PLG (Product-Led Growth)**: Growth strategy driven by the product itself rather than sales

---

## Names, Dates, Numbers, and Places

**Names**
- Janelle Teng
- Ajit Ghuman
- Dave Kellogg
- Goldman Sachs
- Snowflake
- Monetizely
- Kustomer
- Salesforce
- Verizon
- AT&T

**Dates**
- May 2023 (Snowflake FY24 Q1 earnings)
- FY24 Q1
- 2023-24 period
- 2022

**Numbers**
- 130%: Snowflake's NRR rate with UBP
- 13%: Snowflake stock decline after hours following revised guidance
- 50%: Potential revenue loss from proposed UBP changes to author's former product line
- 4 months to 2 years: Implementation timeline for UBP operational setup
- 2 quarters: Timeframe in which Snowflake lowered revenue guidance twice

**Places**
- Not specified in source material

---

## Short Relevant Quotes or Standout Statements

- "UBP can \"feel/sound\" very good. It markets very well."
- "\"paying only for what you use,\" is a very compelling pitch when it comes to pricing"
- "companies with consumption models increased net new revenue faster than subscription peers"
- "Don't be this executive." (referring to those pushing grandiose UBP strategies without analysis)
- "Snowflake pointed to degrading consumption patterns and a lack of predictability of when headwinds might subside as key reasons for the revision"
- "the fundamental valuation model of subscription-based software will not directly apply to usage-based companies"
- "I really cannot overstate how complex this can get and the most ideal pricing strategy certainly is not the best for an organization"

---

## Actionable Lessons

1. **Pre-Implementation Validation**: Have representative sample conversations with customers before making bold claims about pricing metric changes. Do not adopt UBP simply because competitors do or to satisfy Industry Analysts.

2. **Product Type Assessment**: Evaluate whether your product is a capability purchase or a consumption-based service before implementing UBP. Analyze customer usage patterns before adopting UBP to ensure product type fits.

3. **Revenue Metrics Adaptation**: Understand that UBP introduces revenue variability that requires different valuation models than traditional SaaS. Traditional SaaS metrics like ARR and MRR may need replacement with alternatives like trailing spend.

4. **Sales Compensation Structure**: Address sales compensation questions upfront before asking sellers to surface UBP to buyers. Rethink commission models to be based on account growth when initial sale price is minimal under UBP.

5. **Operational Readiness**: Ensure pricing metrics are metered across all customers with data flowing to CRM, CPQ, ERP and Billing systems. Consider operational readiness and technology stack capabilities before committing to UBP as primary pricing strategy.

6. **Sales Forecasting**: Build sales forecasting models to support usage-based pricing motion, recognizing that this becomes critical and difficult due to revenue unpredictability.

7. **Revenue Predictability Options**: If implementing UBP, consider using tariff structures (linear, 2-part, 3-part pricing) to provide some revenue predictability within the consumption-based model.

---

## Source Chunk IDs Used

- chapter-12-usage-based-pricing-chunk-001
- chapter-12-usage-based-pricing-chunk-002

---

## Completeness Note

The summary above fully captures the content of the two provided chunks. Both chunks address overlapping but complementary aspects of UBP implementation. No chunk IDs are identified as needing additional extraction for a complete chapter summary based on the available notes.
