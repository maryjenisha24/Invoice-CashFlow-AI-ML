
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned/cleaned_dataset.csv")

# Convert date columns into datetime format
date_columns = [
    "clear_date",
    "posting_date",
    "due_in_date"
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Create Days to Pay
df["days_to_pay"] = (
    df["clear_date"] - df["posting_date"]
).dt.days

# Create Payment Delay
df["payment_delay"] = (
    df["clear_date"] - df["due_in_date"]
).dt.days

# Display results
print("ANALYSIS DATASET")
print("Shape:", df.shape)

print("\nNEW COLUMNS:")
print(df[[
    "total_open_amount",
    "days_to_pay",
    "payment_delay"
]].head(10))

print("\nMISSING VALUES:")
print(df[[
    "total_open_amount",
    "days_to_pay",
    "payment_delay"
]].isnull().sum())

# STEP 3: SUMMARY STATISTICS

print("\n========== SUMMARY STATISTICS ==========")

print("\n1. INVOICE AMOUNT:")
print(df["total_open_amount"].describe())

print("\n2. DAYS TO PAY:")
print(df["days_to_pay"].describe())

print("\n3. PAYMENT DELAY:")
print(df["payment_delay"].describe())

import matplotlib.pyplot as plt

# STEP 4: HISTOGRAMS

# 1. Invoice Amount Histogram
plt.figure(figsize=(9, 5))
plt.hist(df["total_open_amount"], bins=30, edgecolor="black")
plt.title("Distribution of Invoice Amount")
plt.xlabel("Invoice Amount")
plt.ylabel("Number of Invoices")
plt.tight_layout()
plt.savefig("data/reports/invoice_amount_histogram.png")
plt.show()

# 2. Days to Pay Histogram
plt.figure(figsize=(9, 5))
plt.hist(df["days_to_pay"].dropna(), bins=30, edgecolor="black")
plt.title("Distribution of Days to Pay")
plt.xlabel("Days to Pay")
plt.ylabel("Number of Invoices")
plt.tight_layout()
plt.savefig("data/reports/days_to_pay_histogram.png")
plt.show()

# 3. Payment Delay Histogram
plt.figure(figsize=(9, 5))
plt.hist(df["payment_delay"].dropna(), bins=30, edgecolor="black")
plt.title("Distribution of Payment Delay")
plt.xlabel("Payment Delay (Days)")
plt.ylabel("Number of Invoices")
plt.tight_layout()
plt.savefig("data/reports/payment_delay_histogram.png")
plt.show()

# STEP 5: BOXPLOT ANALYSIS

# 1. Invoice Amount Boxplot
plt.figure(figsize=(9, 5))
plt.boxplot(df["total_open_amount"])
plt.title("Boxplot of Invoice Amount")
plt.ylabel("Invoice Amount")
plt.tight_layout()
plt.savefig("data/reports/invoice_amount_boxplot.png")
plt.show()


# 2. Days to Pay Boxplot
plt.figure(figsize=(9, 5))
plt.boxplot(df["days_to_pay"].dropna())
plt.title("Boxplot of Days to Pay")
plt.ylabel("Days to Pay")
plt.tight_layout()
plt.savefig("data/reports/days_to_pay_boxplot.png")
plt.show()


# 3. Payment Delay Boxplot
plt.figure(figsize=(9, 5))
plt.boxplot(df["payment_delay"].dropna())
plt.title("Boxplot of Payment Delay")
plt.ylabel("Payment Delay (Days)")
plt.tight_layout()
plt.savefig("data/reports/payment_delay_boxplot.png")
plt.show()

# STEP 6: OUTLIER DETECTION USING IQR

def detect_outliers(column):

    data = df[column].dropna()

    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)

    outliers = data[
        (data < lower_limit) |
        (data > upper_limit)
    ]

    print(f"\nColumn: {column}")
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Outlier Count:", len(outliers))
    print("Outlier Percentage:", round(
        len(outliers) / len(data) * 100, 2
    ), "%")


print("\n========== OUTLIER ANALYSIS ==========")

detect_outliers("total_open_amount")
detect_outliers("days_to_pay")
detect_outliers("payment_delay")

# DAY 2 - BIVARIATE ANALYSIS

# STEP 1: INVOICE AMOUNT VS PAYMENT DELAY

plt.figure(figsize=(10, 6))

paid_df = df.dropna(
    subset=["payment_delay", "total_open_amount"]
)

plt.scatter(
    paid_df["total_open_amount"],
    paid_df["payment_delay"],
    alpha=0.3
)

plt.title("Invoice Amount vs Payment Delay")
plt.xlabel("Invoice Amount")
plt.ylabel("Payment Delay (Days)")

plt.tight_layout()

plt.savefig(
    "data/reports/amount_vs_payment_delay.png"
)

plt.show()

# DAY 2 - STEP 2: PAYMENT TERMS VS PAYMENT DELAY

# Select paid invoices
terms_df = df.dropna(
    subset=["payment_delay", "cust_payment_terms"]
)

# Calculate average delay and invoice count
terms_analysis = terms_df.groupby(
    "cust_payment_terms"
).agg(
    average_delay=("payment_delay", "mean"),
    invoice_count=("payment_delay", "count")
).reset_index()

# Keep payment terms having at least 50 paid invoices
terms_analysis = terms_analysis[
    terms_analysis["invoice_count"] >= 50
]

# Sort by average payment delay
terms_analysis = terms_analysis.sort_values(
    "average_delay"
)

print("\nPAYMENT TERMS VS PAYMENT DELAY")
print(terms_analysis.to_string(index=False))

# Create bar chart
plt.figure(figsize=(10, 6))

plt.barh(
    terms_analysis["cust_payment_terms"],
    terms_analysis["average_delay"]
)

plt.title("Average Payment Delay by Payment Terms")
plt.xlabel("Average Payment Delay (Days)")
plt.ylabel("Payment Terms")

plt.tight_layout()

plt.savefig(
    "data/reports/payment_terms_vs_delay.png"
)

plt.show()

# Save analysis results
terms_analysis.to_csv(
    "data/reports/payment_terms_analysis.csv",
    index=False
)

# DAY 2 - STEP 3: CUSTOMER VS PAYMENT DELAY

# Select paid invoices
customer_df = df.dropna(
    subset=["payment_delay", "cust_number"]
)

# Calculate customer payment statistics
customer_analysis = customer_df.groupby(
    "cust_number"
).agg(
    average_delay=("payment_delay", "mean"),
    invoice_count=("payment_delay", "count"),
    late_invoices=(
        "payment_delay",
        lambda x: (x > 0).sum()
    )
).reset_index()

# Calculate late payment percentage
customer_analysis["late_percentage"] = (
    customer_analysis["late_invoices"]
    / customer_analysis["invoice_count"]
) * 100

# Keep customers with at least 10 paid invoices
customer_analysis = customer_analysis[
    customer_analysis["invoice_count"] >= 10
]

# Sort customers by average delay
customer_analysis = customer_analysis.sort_values(
    "average_delay",
    ascending=False
)

print("\nCUSTOMER VS PAYMENT DELAY")
print(
    customer_analysis.head(15).to_string(index=False)
)

# Select top 15 customers
top_customers = customer_analysis.head(15)

# Create bar chart
plt.figure(figsize=(12, 7))

plt.barh(
    top_customers["cust_number"].astype(str),
    top_customers["average_delay"]
)

plt.title("Top 15 Customers by Average Payment Delay")
plt.xlabel("Average Payment Delay (Days)")
plt.ylabel("Customer ID")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    "data/reports/customer_vs_payment_delay.png"
)

plt.show()

# Save complete customer analysis
customer_analysis.to_csv(
    "data/reports/customer_payment_analysis.csv",
    index=False
)

# DAY 2 - STEP 4: INVOICE COUNT VS AVERAGE PAYMENT DELAY

# Use customer analysis data from Step 3

plt.figure(figsize=(10, 6))

plt.scatter(
    customer_analysis["invoice_count"],
    customer_analysis["average_delay"],
    alpha=0.5
)

plt.title("Customer Invoice Count vs Average Payment Delay")
plt.xlabel("Number of Paid Invoices")
plt.ylabel("Average Payment Delay (Days)")

plt.tight_layout()

plt.savefig(
    "data/reports/invoice_count_vs_payment_delay.png"
)

plt.show()

# Calculate correlation
correlation = customer_analysis[
    ["invoice_count", "average_delay"]
].corr().iloc[0, 1]

print("\nINVOICE COUNT VS PAYMENT DELAY")
print("Correlation:", round(correlation, 3))

# DAY 2 - STEP 5: MONTH VS PAYMENT DELAY

# Select paid invoices
monthly_df = df.dropna(
    subset=["payment_delay", "posting_date"]
).copy()

# Extract invoice month
monthly_df["invoice_month"] = (
    monthly_df["posting_date"].dt.to_period("M")
)

# Calculate monthly average delay and invoice count
monthly_analysis = monthly_df.groupby(
    "invoice_month"
).agg(
    average_delay=("payment_delay", "mean"),
    invoice_count=("payment_delay", "count")
).reset_index()

# Keep months with at least 30 paid invoices
monthly_analysis = monthly_analysis[
    monthly_analysis["invoice_count"] >= 30
]

print("\nMONTH VS PAYMENT DELAY")
print(monthly_analysis.to_string(index=False))

# Create line chart
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_analysis["invoice_month"].astype(str),
    monthly_analysis["average_delay"],
    marker="o"
)

plt.title("Monthly Average Payment Delay")
plt.xlabel("Invoice Month")
plt.ylabel("Average Payment Delay (Days)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "data/reports/month_vs_payment_delay.png"
)

plt.show()

# Save monthly analysis
monthly_analysis.to_csv(
    "data/reports/monthly_payment_analysis.csv",
    index=False
)

# DAY 2 - STEP 6: WEEKDAY VS PAYMENT DELAY

# Select paid invoices
weekday_df = df.dropna(
    subset=["payment_delay", "posting_date"]
).copy()

# Extract weekday
weekday_df["weekday"] = (
    weekday_df["posting_date"].dt.day_name()
)

# Calculate average delay and invoice count
weekday_analysis = weekday_df.groupby(
    "weekday"
).agg(
    average_delay=("payment_delay", "mean"),
    invoice_count=("payment_delay", "count")
).reindex([
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]).dropna().reset_index()

print("\nWEEKDAY VS PAYMENT DELAY")
print(weekday_analysis.to_string(index=False))

# Create bar chart
plt.figure(figsize=(10, 6))

plt.bar(
    weekday_analysis["weekday"],
    weekday_analysis["average_delay"]
)

plt.title("Average Payment Delay by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Average Payment Delay (Days)")

plt.tight_layout()

plt.savefig(
    "data/reports/weekday_vs_payment_delay.png"
)

plt.show()

# Save analysis
weekday_analysis.to_csv(
    "data/reports/weekday_payment_analysis.csv",
    index=False
)
