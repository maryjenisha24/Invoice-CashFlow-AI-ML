import pandas as pd
import os

# Load cleaned dataset
df = pd.read_csv("data/cleaned/cleaned_dataset.csv")

# Convert date columns
date_columns = [
    "posting_date",
    "clear_date",
    "due_in_date"
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")

print("DATASET INFORMATION")
print("-------------------")

print("Total Records:", len(df))
print("Columns:", df.columns.tolist())

print("\nDATE RANGE")
print("----------")

for col in date_columns:
    print(f"\n{col}")
    print("Minimum:", df[col].min())
    print("Maximum:", df[col].max())

print("\nPAYMENT DELAY CALCULATION")
print("------------------------")

df["payment_delay_days"] = (
    df["clear_date"] - df["due_in_date"]
).dt.days

print(df["payment_delay_days"].describe())

print("\nFirst 10 Records:")
print(
    df[[
        "posting_date",
        "due_in_date",
        "clear_date",
        "payment_delay_days"
    ]].head(10)
)# STEP 2: MONTHLY INVOICE TREND ANALYSIS

print("\nMONTHLY INVOICE TREND")
print("---------------------")

# Extract month from posting date
df["posting_month"] = df["posting_date"].dt.to_period("M")

# Group invoices month-wise
monthly_trend = df.groupby("posting_month").agg(
    total_invoices=("doc_id", "count"),
    paid_invoices=("clear_date", "count"),
    unpaid_invoices=("clear_date", lambda x: x.isna().sum())
).reset_index()

# Convert month to string
monthly_trend["posting_month"] = (
    monthly_trend["posting_month"].astype(str)
)

print(monthly_trend.to_string(index=False))

# Save monthly analysis
os.makedirs("data/reports", exist_ok=True)

monthly_trend.to_csv(
    "data/reports/monthly_invoice_trend.csv",
    index=False
)

print("\nMonthly invoice trend saved successfully!")
# STEP 3: MONTHLY PAYMENT DELAY ANALYSIS

print("\nMONTHLY PAYMENT DELAY ANALYSIS")
print("------------------------------")

# Consider only invoices with actual payment dates
paid_df = df[df["clear_date"].notna()].copy()

# Group by invoice posting month
paid_df["posting_month"] = (
    paid_df["posting_date"].dt.to_period("M")
)

# Calculate monthly payment behaviour
monthly_delay = paid_df.groupby("posting_month").agg(
    total_paid_invoices=("doc_id", "count"),
    average_delay=("payment_delay_days", "mean"),
    median_delay=("payment_delay_days", "median"),
    late_payments=(
        "payment_delay_days",
        lambda x: (x > 0).sum()
    ),
    on_time_payments=(
        "payment_delay_days",
        lambda x: (x == 0).sum()
    ),
    early_payments=(
        "payment_delay_days",
        lambda x: (x < 0).sum()
    )
).reset_index()

# Calculate late payment percentage
monthly_delay["late_percentage"] = (
    monthly_delay["late_payments"]
    / monthly_delay["total_paid_invoices"]
) * 100

monthly_delay["posting_month"] = (
    monthly_delay["posting_month"].astype(str)
)

print(monthly_delay.to_string(index=False))

# Save report
monthly_delay.to_csv(
    "data/reports/monthly_payment_delay.csv",
    index=False
)

print("\nMonthly payment delay report saved successfully!")
# STEP 4: YEAR-WISE PAYMENT BEHAVIOUR

print("\nYEAR-WISE PAYMENT BEHAVIOUR")
print("---------------------------")

paid_df["posting_year"] = (
    paid_df["posting_date"].dt.year
)

yearly_analysis = paid_df.groupby("posting_year").agg(
    paid_invoices=("doc_id", "count"),
    average_delay=("payment_delay_days", "mean"),
    late_payments=(
        "payment_delay_days",
        lambda x: (x > 0).sum()
    ),
    on_time_payments=(
        "payment_delay_days",
        lambda x: (x == 0).sum()
    ),
    early_payments=(
        "payment_delay_days",
        lambda x: (x < 0).sum()
    )
).reset_index()

yearly_analysis["late_percentage"] = (
    yearly_analysis["late_payments"]
    / yearly_analysis["paid_invoices"]
) * 100

print(yearly_analysis.to_string(index=False))

yearly_analysis.to_csv(
    "data/reports/yearly_payment_analysis.csv",
    index=False
)

print("\nYear-wise payment analysis saved successfully!")
import matplotlib.pyplot as plt

# STEP 5: TIME-BASED VISUALIZATION

# Graph 1: Monthly Invoice Volume
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_trend["posting_month"],
    monthly_trend["total_invoices"],
    marker="o"
)

plt.title("Monthly Invoice Volume Trend")
plt.xlabel("Posting Month")
plt.ylabel("Number of Invoices")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig("data/reports/monthly_invoice_volume.png")
plt.show()

# Graph 2: Monthly Late Payment Percentage
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_delay["posting_month"],
    monthly_delay["late_percentage"],
    marker="o"
)

plt.title("Monthly Late Payment Percentage")
plt.xlabel("Posting Month")
plt.ylabel("Late Payment Percentage (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig("data/reports/monthly_late_payment_percentage.png")
plt.show()

print("\nTime-based visualizations saved successfully!")