# WEEK 2 – EXPLORATORY DATA ANALYSIS (EDA) REPORT

**Project Title:** Invoice Payment Delay & Cash-Flow Intelligence Platform  
**Organization:** Orvians Technologies  
**Dataset:** Customer Invoices Dataset  
**Week:** 2 – Data Visualization & Exploratory Data Analysis

---

## 1. Introduction

The objective of this project is to analyze historical invoice payment data to understand customer payment behaviour, identify payment delays, and study outstanding invoice patterns.

During Week 2, Exploratory Data Analysis (EDA) was performed to identify trends, patterns, relationships, and business insights from the cleaned invoice dataset.

## 2. Dataset Overview

The cleaned dataset contains:

- Total records: 48,839
- Total columns: 18
- Paid invoices: 39,158
- Open invoices: 9,681

The dataset includes invoice amounts, customer information, posting dates, due dates, clearing dates, payment terms, and invoice status.

## 3. Exploratory Data Analysis

The following analysis activities were completed:

### 3.1 Univariate Analysis
- Invoice amount distribution
- Invoice amount outlier analysis
- Days to pay distribution
- Payment delay distribution

### 3.2 Bivariate Analysis
- Invoice amount vs payment delay
- Payment terms vs payment delay
- Customer vs payment delay

### 3.3 Time-Based Analysis
- Monthly invoice volume
- Monthly late payment percentage
- Month vs payment delay
- Weekday vs payment delay

### 3.4 Customer Analysis
Customer payment behaviour was explored to understand differences in payment delays across customers.

### 3.5 Invoice Overview and Aging Analysis

| Metric | Result |
|---|---:|
| Total invoices | 48,839 |
| Paid invoices | 39,158 |
| Open invoices | 9,681 |
| Total outstanding amount | 323,093,316.19 |
| Average overdue days | 34.2 |
| Maximum overdue days | 85 |

**Aging Classification:**

| Aging Category | Invoice Count |
|---|---:|
| 0–30 Days | 3,673 |
| 31–60 Days | 4,427 |
| 61–90 Days | 1,187 |
| Not Yet Due | 394 |

**Outstanding Amount by Aging Category:**

| Aging Category | Outstanding Amount |
|---|---:|
| 0–30 Days | 122,268,100 approximately |
| 31–60 Days | 155,609,420.53 |
| 61–90 Days | 38,024,830 approximately |
| Not Yet Due | 7,191,002 approximately |

### 3.6 Correlation Analysis

Correlation analysis was performed to understand the linear relationship between invoice amount and payment delay.

**Correlation Result:**

Invoice Amount vs Payment Delay: **0.007**

This indicates a very weak linear relationship between invoice amount and payment delay.

The analysis suggests that invoice amount alone is not a strong indicator of customer payment delay.

## 4. Key Business Insights

1. The dataset contains 48,839 invoices.
2. Out of these, 39,158 invoices are paid and 9,681 remain open.
3. Total outstanding invoice value is 323,093,316.19.
4. The average overdue period for open invoices is 34.2 days.
5. The 31–60 days category has the highest number of open invoices.
6. The 31–60 days category contributes 48.16% of the total outstanding amount.
7. The 0–30 days category contributes 37.84% of outstanding value.
8. The 61–90 days category contributes 11.77% of outstanding value.
9. Invoice amount has almost no linear correlation with payment delay (0.007).

## 5. Business Recommendations

- Monitor invoices in the 31–60 days aging category carefully.
- Prioritize collection activities for overdue invoices.
- Study customer payment history to identify high-risk customers.
- Consider payment terms and historical payment behaviour when building prediction models.
- Use historical invoice data to support future cash-flow forecasting.

## 6. Conclusion

Week 2 successfully covered Exploratory Data Analysis of the cleaned customer invoice dataset.

Univariate, bivariate, time-based, customer, aging, and correlation analyses were performed. Visualizations were created to understand invoice distributions, customer payment behaviour, payment delays, and outstanding amounts.

The findings provide a foundation for the next stages of the Invoice Payment Delay & Cash-Flow Intelligence Platform, particularly payment delay prediction, customer payment risk scoring, and cash-flow forecasting.

**Project Status:** Week 2 – EDA Analysis Completed.