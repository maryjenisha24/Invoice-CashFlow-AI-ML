
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned/cleaned_dataset.csv")

# Convert date columns
df["posting_date"] = pd.to_datetime(df["posting_date"])
df["clear_date"] = pd.to_datetime(df["clear_date"])
df["due_in_date"] = pd.to_datetime(df["due_in_date"])

# STEP 1: Overall Invoice Overview
total_invoices = len(df)

paid_invoices = df[df["clear_date"].notna()]
open_invoices = df[df["clear_date"].isna()]

total_outstanding = open_invoices["total_open_amount"].sum()

print("\nOVERALL INVOICE OVERVIEW")
print("------------------------------")
print("Total Invoices:", total_invoices)
print("Paid Invoices:", len(paid_invoices))
print("Open Invoices:", len(open_invoices))
print("Total Outstanding Amount:", round(total_outstanding, 2))
print("------------------------------")

# STEP 2: Calculate Invoice Aging

# Consider today's date as the analysis date
analysis_date = df["posting_date"].max()
# Filter open invoices
open_df = df[df["clear_date"].isna()].copy()

# Calculate overdue days
open_df["overdue_days"] = (
    analysis_date - open_df["due_in_date"]
).dt.days

print("\nINVOICE AGING CALCULATION")
print("------------------------------")
print("Total Open Invoices:", len(open_df))
print("Average Overdue Days:", round(open_df["overdue_days"].mean(), 2))
print("Maximum Overdue Days:", open_df["overdue_days"].max())
print("Minimum Overdue Days:", open_df["overdue_days"].min())
print("------------------------------")

# STEP 3: Aging Bucket Classification

def classify_aging(days):
    if days < 0:
        return "Not Yet Due"
    elif days <= 30:
        return "0-30 Days"
    elif days <= 60:
        return "31-60 Days"
    elif days <= 90:
        return "61-90 Days"
    else:
        return "90+ Days"


open_df["aging_bucket"] = open_df["overdue_days"].apply(classify_aging)

print("\nAGING BUCKET CLASSIFICATION")
print("------------------------------")
print(open_df["aging_bucket"].value_counts())
print("------------------------------")

# STEP 4: Aging-wise Outstanding Amount

aging_amount = open_df.groupby("aging_bucket")[
    "total_open_amount"
].agg(["count", "sum"])

aging_amount = aging_amount.rename(columns={
    "count": "invoice_count",
    "sum": "outstanding_amount"
})

print("\nAGING-WISE OUTSTANDING AMOUNT")
print("------------------------------")
print(aging_amount.round(2))
print("------------------------------")

# STEP 5: Aging Analysis Insights

total_open_amount = open_df["total_open_amount"].sum()

print("\nAGING ANALYSIS INSIGHTS")
print("------------------------------")

print("Total Open Invoices:", len(open_df))

print("Total Outstanding Amount:",
      round(total_open_amount, 2))

print("\nHighest Invoice Aging Category:",
      aging_amount["outstanding_amount"].idxmax())

print("Highest Outstanding Amount:",
      round(aging_amount["outstanding_amount"].max(), 2))

print("\nOutstanding Percentage by Category:")

aging_amount["percentage"] = (
    aging_amount["outstanding_amount"] / total_open_amount
) * 100

print(aging_amount["percentage"].round(2))

# Save Aging Analysis Report
aging_amount.to_csv(
    "data/reports/aging_analysis_report.csv"
)

print("\nAging analysis report saved successfully!")
print("------------------------------")
