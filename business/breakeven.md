# breakeven.md

## Unit Economics & Break-even Analysis

### Cost per Active User
- **Compute Costs**: $0.05 per user per month (based on average cloud compute costs for running analysis tools)
- **Storage Costs**: $0.01 per user per month (average storage cost for user data and analysis results)
- **Bandwidth Costs**: $0.02 per user per month (average bandwidth cost for data transfer)
  
**Total Cost per Active User**:  
**$0.05 + $0.01 + $0.02 = $0.08 per user per month**

### Pricing Tiers
| Tier Name        | Price ($/mo) | Features                                                                 |
|------------------|--------------|--------------------------------------------------------------------------|
| **Basic**        | $10          | Basic code analysis, Issue identification, Community support            |
| **Pro**          | $30          | All Basic features + Optimization suggestions, Priority support         |
| **Enterprise**   | $100         | All Pro features + Custom integrations, Dedicated account manager       |

### Customer Acquisition Cost (CAC) Range
- Estimated CAC: $50 - $100 per user (includes marketing, sales, and onboarding costs)

### Lifetime Value (LTV) Estimate
- Average user lifespan: 24 months
- Average revenue per user (ARPU) across tiers: 
  - Basic: $10
  - Pro: $30
  - Enterprise: $100
- Weighted ARPU (assuming 70% Basic, 20% Pro, 10% Enterprise):  
  LTV = (0.7 * $10 + 0.2 * $30 + 0.1 * $100) * 24 months  
  LTV = ($7 + $6 + $10) * 24 = $23 * 24 = **$552**

### Break-even Users Count
- Break-even point = CAC / (ARPU - Cost per Active User)  
- Using weighted ARPU of $23:  
  Break-even users = $75 / ($23 - $0.08)  
  Break-even users = $75 / $22.92 ≈ **3.27 users** (rounded up to 4 users)

### Path to $10K MRR
- Target MRR: $10,000
- Average revenue per user (ARPU) across tiers: $23
- Users needed to reach $10K MRR:  
  Users = $10,000 / $23 ≈ **435 users**

#### Tier Strategy
- **Basic Tier**: 70% of users  
  Users = 0.7 * 435 = **305 users**  
  Revenue = 305 * $10 = $3,050

- **Pro Tier**: 20% of users  
  Users = 0.2 * 435 = **87 users**  
  Revenue = 87 * $30 = $2,610

- **Enterprise Tier**: 10% of users  
  Users = 0.1 * 435 = **43 users**  
  Revenue = 43 * $100 = $4,300

**Total Revenue**: $3,050 + $2,610 + $4,300 = **$9,960** (close to $10K MRR)

### Summary
To achieve $10K MRR, we would target approximately 435 users distributed across the pricing tiers, with a focus on acquiring 305 Basic users, 87 Pro users, and 43 Enterprise users.