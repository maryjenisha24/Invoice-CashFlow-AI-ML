# Week 2 – Insights & ML Hypotheses

## Insight 1: Customer Payment Behaviour

**Finding:**
Some customers consistently make late payments.

- Customer CCU013: 534 paid invoices, all 534 were late.
- Customer 140106408: 427 paid invoices, all 427 were late.

**Business Interpretation:**
These customers may represent higher payment risk.
The business should monitor their outstanding invoices
and consider prioritizing collection follow-ups.

**ML Hypothesis:**
Historical customer payment delay, late payment percentage
and invoice count may help predict future customer payment risk.

**Supporting Chart:**
customer_vs_payment_delay.png
## Insight 2: Customer with the Highest Average Payment Delay

**Finding:**

Customer 140106181 has an average payment delay of 63.05 days across 95 invoices. Out of these, 92 invoices were paid late (96.84%).

**Business Interpretation:**

This customer shows a significant payment delay pattern. Such customers may require closer monitoring and early collection follow-ups to reduce cash-flow uncertainty.

**ML Hypothesis:**

Customer's historical average payment delay and late payment percentage may help predict future invoice payment delays.

**Supporting Chart:**

customer_vs_payment_delay.png
## Insight 3: Monthly Payment Delay Pattern

**Finding:**

February 2019 recorded the highest late-payment percentage of 45.47%, based on 2,696 paid invoices.

**Business Interpretation:**

Certain months show higher late-payment rates. Businesses should monitor monthly payment patterns to improve cash-flow planning.

**ML Hypothesis:**

Invoice posting month and historical monthly payment behaviour may help predict payment delays.

**Supporting Chart:**

monthly_late_payment_percentage.png

---

## Insight 4: Payment Terms and Delay

**Finding:**

Payment term NAX2 recorded the highest average payment delay of 42.69 days across 540 invoices.

**Business Interpretation:**

Different payment terms are associated with different payment delay patterns. Identifying high-delay payment terms can help businesses manage collection risks.

**ML Hypothesis:**

Customer payment terms may be an important feature for predicting invoice payment delays.

**Supporting Chart:**

payment_terms_vs_delay.png
## Insight 5: Repeat Customer Behaviour

**Finding:**

The dataset contains 1,099 customers. Among them, 788 are repeat customers with 48,528 invoices, while 311 are one-time customers with 311 invoices.

**Business Interpretation:**

Most invoices come from repeat customers. Understanding their historical payment behaviour is important for managing customer relationships and cash flow.

**ML Hypothesis:**

Customer invoice frequency and previous payment behaviour may help predict future payment delays.

**Supporting Chart:**

customer_vs_payment_delay.png

---

## Insight 6: Weekday Payment Delay Pattern

**Finding:**

Friday recorded the highest average payment delay of 1.16 days, while Tuesday recorded the lowest average delay of approximately 0.66 days.

**Business Interpretation:**

Payment delays vary across weekdays. Businesses can study weekday patterns to improve payment follow-up scheduling.

**ML Hypothesis:**

Invoice posting weekday may provide useful information for predicting payment delays.

**Supporting Chart:**

weekday_vs_payment_delay.png
## Insight 7: Outstanding Invoice Aging Pattern

**Finding:**

The 31–60 Days aging bucket contains 4,427 outstanding invoices, representing an outstanding amount of 155,609,420.53 (48.16% of the total outstanding amount).

**Business Interpretation:**

Most outstanding invoices fall within the 31–60 days aging bucket. Businesses should prioritize collection follow-ups for these invoices to reduce overdue balances.

**ML Hypothesis:**

Invoice age and days past due may help predict collection risk and prioritize overdue invoices.

**Supporting Chart:**

aging_analysis_report.csv

---

## Insight 8: Invoice Amount and Payment Delay Correlation

**Finding:**

The correlation between invoice amount and payment delay is approximately 0.00685, indicating almost no linear relationship.

**Business Interpretation:**

Higher invoice amounts do not necessarily mean higher payment delays. Businesses should consider other factors such as customer history and payment terms.

**ML Hypothesis:**

Customer payment history and payment terms may provide more useful predictive information than invoice amount alone.

**Supporting Chart:**

correlation_heatmap.png