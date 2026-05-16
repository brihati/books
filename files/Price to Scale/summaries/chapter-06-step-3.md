# Chapter 06: Step 3 – Selecting a Pricing Metric

## Detailed Chapter Summary

Step 3 focuses on selecting the pricing metric—the most consequential decision in the entire pricing exercise. Getting this decision right allows fine-tuning of other pricing model components; getting it wrong can slow sales velocity and leave money on the table.

The chapter introduces two main approaches at the highest level:

1. **Consumption-based pricing**: Scales with actual units of usage or per-seat allocations. This includes:
   - **Per-seat model**: Charges per user, allowing companies to charge more from larger clients
   - **Usage-based model**: Scales with actual units of usage of a product

2. **Capability-based pricing**: A lump-sum approach that charges a set amount for a piece of software capability, which may be fixed or scale based on customer size. This doesn't allow for usage growth over time.

The goal is to charge customers proportionally to both company size and perceived value derived.

### Evaluating and Selecting Metrics

A structured checklist with six criteria helps evaluate and rank candidate pricing metrics:
- Tie to client value
- Fit for clients
- Measurability
- Predictability
- Diminishing or scaled costs
- Deal economics

**When to use each approach:**
- Seat-based pricing works well for foundational "system of record" products like CRMs, HR, or Customer Support systems routinely used across departments
- Usage-based pricing can be more directly tied to the value a prospect receives and lead to easier client adoption
- Usage-based pricing is useful when there are hard costs that scale with usage (e.g., S3 storage, compute power)
- Capability pricing works well as add-on modules on top of a base platform utilizing consumption-based pricing

### Real-World Pricing Metric Changes

The chapter analyzes how three established SaaS companies adapted their pricing models during growth stages:

**Helpshift**: Changed from per-seat to MAU (monthly active users)-based pricing. A customer with 20 support agents at $100/month would have been $24,000/year with seat pricing. The same customer with 20 Million MAU paying $100 per 100,000 MAU resulted in $20,000/month or $240,000 annual ASP—a 10x revenue increase.

**Kustomer**: Despite wanting innovative consumption-based pricing, discovered customers preferred familiar, repeatable models mapping to existing budgets. Retained seat-based pricing model like Zendesk incumbents.

**Mixpanel**: Changed from Events to Monthly Tracked Users (MTUs) pricing when the Events metric became misaligned with customer value perception as the company grew across use cases and industries.

**HubSpot**: Changed from total Contacts to Marketing Contacts pricing metric. Discovered that sales activity in Sales Hub generated additional contacts that increased Marketing Hub subscription price without proportional marketing value. Marketing Contacts counts only contacts customers need to interact with via email or ads.

### Three Consumption-Based Pricing Structures

**Linear Model**:
- Charge a set unit price based on main pricing variable, per seat, or per event
- Simplifies but creates revenue unpredictability
- Reduces risk for clients, increasing market penetration
- Requires accurate instrumentation, increasing overhead costs
- Works best for newer products

**2-Part Tariff**:
- Charge a base platform fee as setup price plus a unit price
- Example: $10,000 + $0.40 per unit
- Increasingly common; customers accustomed to it
- Improves revenue predictability while enabling upside of greater usage
- Can lead to "sawtooth edges" creating pricing inconsistency

**3-Part Tariff** (also called "cell phone plan model"):
- Offer set number of units for base fee with overage fee on top
- Example: 5GB of data for $40/month, $0.10 for every MB afterward
- Or: 100 seats for $10,000 per month and $150 per seat for additional seats
- Or: 100,000 units with $35,000 tier fee and $0.45 overage rate
- Maximizes revenue capture according to academic research
- Incentivizes increased product usage
- May cause buyer's remorse if customer needs change
- Provides highest predictability and revenue

### Block Pricing for Volume Discounts

All three models can incorporate **block pricing** (sub-levels within pricing models) to provide volume discounts. Example with tiered rates:
- $0.40 per unit (0–100,000 units)
- $0.35 per unit (100,001–250,000 units)
- $0.30 per unit (250,001–500,000 units)

### Capability Pricing for Add-Ons

Capability pricing is most suitable for add-ons rather than base software. Three methods exist:

1. **Fixed pricing**: $5,000 flat fee for an add-on
2. **Percentage-based**: 10% of base ACV (e.g., 10% of $40,000 = $4,000)
3. **Percentage-based with min/max bounds**: Balances proportional sizing without extreme price points

Using capability pricing for base software leaves money on the table and dissuades enterprise adoption. Percentage-based add-on pricing without bounds may be too cheap for small customers or too expensive for large ones.

### Key Insights on Customer Preferences and Outcomes

Customers prefer repeatable, consistent pricing that maps to existing budgets over innovative but unfamiliar models. Changing pricing metrics can reduce customer churn when bills no longer feel disproportionate to value. Pricing metric changes also enable faster sales cycles by reducing the need for translation work between technical metrics and customer budgets.

---

## Key Points

- Selecting the pricing metric is the most consequential decision in the entire pricing exercise
- Getting it right allows fine-tuning of other components; getting it wrong can slow sales velocity
- Two main pricing approaches: Consumption-based (per-seat and usage-based) and Capability-based (lump-sum)
- The goal is to charge customers proportionally to both company size and perceived value
- A structured checklist with six criteria helps evaluate candidate pricing metrics
- Customers prefer familiar, repeatable pricing mapped to existing budgets
- Changing pricing metrics can achieve 10x revenue increases while reducing churn
- Three consumption pricing structures exist: Linear, 2-Part Tariff, and 3-Part Tariff
- Block pricing provides volume discounts within all models
- Capability pricing works best for add-ons, not base pricing
- Pricing metrics must be tied to customer success and value outcomes

---

## Important Examples and Stories

**Helpshift case study (10x revenue increase)**:
- Changed from per-seat to MAU-based pricing
- Customer scenario: 20 support agents at $100/month
  - With seat pricing: $24,000/year
  - With MAU pricing (20 Million MAU @ $100 per 100,000): $20,000/month or $240,000 annual ASP
  - Result: 10x revenue increase

**Kustomer**: Wanted innovative consumption-based pricing but discovered customers wanted familiar models mapping to existing budgets. Retained seat-based pricing like Zendesk.

**Mixpanel**: Events-based pricing became misaligned with customer value as company expanded across use cases. Switched to Monthly Tracked Users (MTUs) pricing.

**HubSpot**: 
- Sales Hub activity generated unrelated contacts that increased Marketing Hub bills without proportional marketing value
- Changed from total Contacts to Marketing Contacts (only contacts engaged via email or ads)
- Customer insight: "A customer's measure of success isn't just how much they can grow their database, but how many leads in that database are worthy of nurturing"

**Nosto**: Evolved pricing from purely usage-based to include capability and platform pricing components.

**Oracle**: Solved marketing automation pricing when SMS sending created significant hard costs.

**Basecamp**: Flat $99/month pricing independent of usage—example of capability-based approach.

---

## Definitions and Terms

| Term | Definition |
|------|-----------|
| **Pricing Metric** | The unit of measurement used to charge customers (e.g., seats, events, users, contacts) |
| **Consumption Pricing** | Pricing that scales with actual units of usage or per-seat allocations |
| **Capability Pricing** | Pricing a product as a lump-sum amount for the capability offered |
| **Seat-based Model** | Charge per user, allowing companies to charge more from larger clients |
| **Usage-based Model** | Scales with actual units of usage of a product |
| **Linear Model** | Charge a set unit price based on main pricing variable |
| **2-Part Tariff** | Base platform fee plus unit price (e.g., $10,000 + $0.40/unit) |
| **3-Part Tariff** | Set number of units included in base fee with overage fee on top (cell phone plan model) |
| **Block Pricing** | Sub-levels within pricing models providing volume discounts |
| **MAU (Monthly Active Users)** | Monthly active users metric for usage-based pricing |
| **MTU (Monthly Tracked Users)** | Similar to MAUs, used by Mixpanel as pricing metric |
| **Marketing Contacts** | HubSpot's metric counting only contacts customers engage with via email or ads |
| **System of Record** | Foundational products like CRMs, HR, or Customer Support systems used across departments |
| **ASP (Annual Subscription Price)** | Annual contract value |
| **Hard Costs** | Infrastructure or variable costs that scale with usage (e.g., storage, compute) |
| **Sawtooth Edges** | Pricing inconsistencies created in 2-part models due to fee breakpoints |
| **Overage Fee** | Charge per unit beyond included units in a tier |
| **Platform Fee** | Fixed recurring fee component in 2-part and 3-part models |
| **Add-on Pricing** | Pricing for additional capabilities added to base packages |

---

## Names, Dates, Numbers, and Places

### Names
- **Tien Tzuo** – Zuora CEO
- **Brad Birnbaum** – Kustomer CEO
- **Dharmesh Shah** – HubSpot co-founder
- **Kate Bueker** – HubSpot executive
- **Ajit Ghuman** – HubSpot executive
- **Tom Tonguz** – Pricing expert
- **Nosto** – Personalization platform
- **Oracle** – Enterprise software company
- **Basecamp** – Project management software
- **Amplitude** – Analytics platform
- **Google Drive** – Cloud storage
- **Twilio** – Communications platform
- **Zendesk** – Customer support platform

### Key Numbers and Metrics
- **10x** – Revenue increase from second pricing metric
- **$240,000** – Helpshift's new annual ASP with MAU pricing
- **$24,000** – Helpshift's annual price with seat-based pricing
- **20 Million MAU** – Example customer scale at Helpshift
- **$100 per 100,000 MAU** – Helpshift's MAU pricing rate
- **$20,000/month** – Helpshift's example customer monthly bill
- **$1 Billion** – Facebook's acquisition of Kustomer (2020)
- **20 agents** – Example customer seat count
- **$100/month** – Example seat-based price point
- **5GB** – Example data allocation in 3-Part model
- **$40/month** – Example base price for 5GB storage
- **$0.10** – Example overage rate per MB
- **100 seats** – Example 3-Part Tariff tier
- **$10,000/month** – Example tier fee
- **$150/seat** – Example overage rate
- **100,000 units** – Example tier size
- **$35,000** – Example tier fee with $0.45 overage
- **$0.40/unit** – Linear model pricing example
- **$20,000** – 2-Part Tariff platform fee example
- **$0.30/unit** – 2-Part Tariff usage fee example
- **$30,000** – Example graded platform fee
- **$0.35/unit** – Mid-tier usage fee
- **$40,000** – Higher tier platform fee
- **$0.20/unit** – Highest tier usage fee
- **$99/month** – Basecamp flat pricing
- **$5,000** – Example fixed add-on price
- **10%** – Example percentage-of-base add-on fee
- **$4,000** – Example add-on price (10% of $40,000 ACV)
- **$99/month** – Basecamp's flat pricing

### Dates
- **2006** – Reference period for Mixpanel
- **2019** – Reference period for metric changes
- **2020** – Facebook's $1 billion Kustomer acquisition; Q3 and Q4 reference periods
- **Q3 and Q4** – Time periods referenced in case studies

### Places
- **Web-based support space** – Market context for Helpshift/Kustomer
- **Mid-market** – Customer segment preferring familiar pricing

---

## Short Relevant Quotes and Standout Statements

> "If you get it right, almost every other piece of your pricing model and operations can be fine tuned. If you get it wrong, you may not only waste the time taken in conducting this project but can significantly slow down sales velocity."

> "they didn't want innovative pricing. They wanted repeatable, consistent pricing that mapped to the budget they already had in place"

> "they already had a budget in place, so they just said, 'Hey, we have X amount allocated for a solution'"

> "our customers didn't want a consumption model"

> "A customer's measure of success isn't just how much they can grow their database, but how many leads in that database are worthy of nurturing"

> "Our marketing contacts pricing model allows customers to only pay for the contacts they want to market to via email or ads"

> "Reduced customer churn: As now customers wouldn't be saddled with paying disproportionately more compared to value derived"

> "Faster sales motion: Deals close faster as Sales don't have to play the role of translator"

> "bigger companies will want more predictable revenue"

> "it works only for a sub-set of customers with lower unit volume"

> "you are more likely not only to leave money on the table but actively dissuade enterprise adoption"

> "it would make your sales and sales operations teams go crazy with the complexity"

> "This is what we want. It gives us even higher predictability and more revenue"

> "Subscribed" (source reference)

---

## Actionable Lessons

1. **Use the evaluation checklist**: Evaluate and rank candidate pricing metrics using six criteria: tie to client value, fit for clients, measurability, predictability, diminishing or scaled costs, and deal economics

2. **Match pricing approach to product type**:
   - Use per-seat pricing for foundational "system of record" products (CRMs, HR, support systems)
   - Use usage-based pricing when value is directly tied to usage and hard costs scale with usage
   - Use capability pricing as add-on modules on top of base consumption-based pricing

3. **Consider customer maturity**:
   - For newer products, prefer linear pricing models for better client adoption
   - For established products, consider 2-part or 3-part models for revenue predictability

4. **Test against customer preferences**:
   - Validate that innovative pricing models align with customer budget constraints and familiarity before implementation
   - Customers prefer repeatable pricing mapped to existing budgets

5. **Align metrics with customer success**:
   - Use pricing metrics tied to customer success and value outcomes rather than raw usage metrics
   - Ensure metrics remain aligned with customer value perception as company expands across use cases

6. **Reconsider metrics for multi-product offerings**:
   - When expanding across products, evaluate whether single metrics work consistently across all products
   - Avoid situations where one product's usage drives disproportionate pricing in another product

7. **Implement block pricing strategically**:
   - Provide volume discounts within any pricing model using tiered block pricing
   - Set overage prices higher than inferred per-unit price to incentivize tier upgrades

8. **Structure add-on pricing carefully**:
   - Use percentage-of-base-fee pricing with min/max bounds for add-ons
   - This balances proportional sizing without extreme price points for small or large customers
   - Avoid capability pricing for base software (leaves money on table and dissuades enterprise adoption)

9. **Monitor pricing edge effects**:
   - Watch for "sawtooth edges" in 2-part models that create pricing inconsistency
   - Test pricing models against revenue charts to visualize impact at different usage levels

10. **Ensure measurability and instrumentation**:
    - Confirm your product can be instrumented to easily measure the chosen metric
    - Ensure the metric is predictable for customers

---

## Source Chunk IDs Used

- chapter-06-step-3-chunk-001
- chapter-06-step-3-chunk-002
- chapter-06-step-3-chunk-003
- chapter-06-step-3-chunk-004

**Source Pages
