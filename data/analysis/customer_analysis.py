
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned/cleaned_dataset.csv")

# Convert date columns
df["clear_date"] = pd.to_datetime(df["clear_date"], errors="coerce")
df["due_in_date"] = pd.to_datetime(df["due_in_date"], errors="coerce")

# Customer-wise invoice overview
customer_summary = df.groupby("cust_number").agg(
    total_invoices=("doc_id", "count"),
    paid_invoices=("clear_date", "count"),
    open_invoices=("isOpen", "sum")
)

# Sort customers by total invoice count
customer_summary = customer_summary.sort_values(
    by="total_invoices",
    ascending=False
)

print("\nCUSTOMER INVOICE OVERVIEW")
print(customer_summary.head(10))

print("\nTOTAL UNIQUE CUSTOMERS:", df["cust_number"].nunique())

# Save report
customer_summary.to_csv(
    "data/reports/customer_invoice_summary.csv"
)

print("\nCustomer invoice summary saved successfully!")

# STEP 2: Customer-wise payment behaviour

# Consider only paid invoices
paid_df = df[df["clear_date"].notna()].copy()

# Calculate payment delay
paid_df["payment_delay_days"] = (
    paid_df["clear_date"] - paid_df["due_in_date"]
).dt.days

# Group payment behaviour by customer
customer_payment = paid_df.groupby("cust_number").agg(
    paid_invoices=("payment_delay_days", "count"),
    average_delay=("payment_delay_days", "mean"),
    late_invoices=("payment_delay_days", lambda x: (x > 0).sum()),
    on_time_invoices=("payment_delay_days", lambda x: (x == 0).sum()),
    early_invoices=("payment_delay_days", lambda x: (x < 0).sum())
)

# Calculate late payment percentage
customer_payment["late_percentage"] = (
    customer_payment["late_invoices"]
    / customer_payment["paid_invoices"]
) * 100

# Sort by late payment percentage
customer_payment = customer_payment.sort_values(
    by="late_percentage",
    ascending=False
)

print("\nCUSTOMER PAYMENT BEHAVIOUR")
print(customer_payment.head(10).to_string())

# Save report
customer_payment.to_csv(
    "data/reports/customer_payment_behaviour.csv"
)

print("\nCustomer payment behaviour report saved successfully!")
# STEP 3: Repeat Customer Behaviour

# Count invoices for each customer
customer_invoice_count = df.groupby("cust_number").size().reset_index(name="total_invoices")

# Classify customers
customer_invoice_count["customer_type"] = customer_invoice_count["total_invoices"].apply(
    lambda x: "Repeat Customer" if x > 1 else "One-time Customer"
)

# Customer type summary
repeat_summary = customer_invoice_count.groupby("customer_type").agg(
    total_customers=("cust_number", "count"),
    total_invoices=("total_invoices", "sum"),
    average_invoices=("total_invoices", "mean")
)

print("\nREPEAT CUSTOMER ANALYSIS")
print(repeat_summary)

# Save report
repeat_summary.to_csv("data/reports/repeat_customer_analysis.csv")

print("\nRepeat customer analysis report saved successfully!")
# STEP 4: Top Late-Paying Customers

# Consider customers with at least 5 paid invoices
reliable_customers = customer_payment[
    customer_payment["paid_invoices"] >= 5
].copy()

# Sort by number of late invoices
top_late_customers = reliable_customers.sort_values(
    by="late_invoices",
    ascending=False
)

print("\nTOP 10 LATE-PAYING CUSTOMERS")
print(top_late_customers.head(10).to_string())

# Save report
top_late_customers.head(10).to_csv(
    "data/reports/top_late_paying_customers.csv"
)

print("\nTop late-paying customers report saved successfully!")
# STEP 5: Outstanding Amount and Overdue Analysis

# Consider only open invoices
open_df = df[df["isOpen"] == 1].copy()

# Calculate total outstanding amount
total_outstanding = open_df["total_open_amount"].sum()

# Use latest posting date as analysis reference date
reference_date = pd.to_datetime(df["posting_date"]).max()
print("Reference Date:", reference_date)
print("Reference Date Type:", type(reference_date))
# Identify overdue invoices
overdue_df = open_df[
    open_df["due_in_date"] < reference_date
].copy()

# Calculate overdue days
overdue_df["overdue_days"] = (
    reference_date - overdue_df["due_in_date"]
).dt.days

# Customer-wise outstanding analysis
customer_outstanding = open_df.groupby("cust_number").agg(
    open_invoices=("doc_id", "count"),
    outstanding_amount=("total_open_amount", "sum")
)

# Customer-wise overdue analysis
customer_overdue = overdue_df.groupby("cust_number").agg(
    overdue_invoices=("doc_id", "count"),
    overdue_amount=("total_open_amount", "sum"),
    average_overdue_days=("overdue_days", "mean")
)

print("\nOUTSTANDING AMOUNT ANALYSIS")
print("Total Outstanding Amount:", total_outstanding)

print("\nOVERDUE INVOICE ANALYSIS")
print("Total Open Invoices:", len(open_df))
print("Total Overdue Invoices:", len(overdue_df))

# Top customers by outstanding amount
print("\nTOP 10 CUSTOMERS BY OUTSTANDING AMOUNT")
print(
    customer_outstanding.sort_values(
        by="outstanding_amount",
        ascending=False
    ).head(10).to_string()
)

# Save reports
customer_outstanding.to_csv(
    "data/reports/customer_outstanding_analysis.csv"
)

customer_overdue.to_csv(
    "data/reports/customer_overdue_analysis.csv"
)

print("\nOutstanding and overdue reports saved successfully!")
# STEP 6: Customer Analysis Summary

total_customers = df["cust_number"].nunique()

repeat_customers = (
    customer_invoice_count["customer_type"] == "Repeat Customer"
).sum()

one_time_customers = (
    customer_invoice_count["customer_type"] == "One-time Customer"
).sum()

total_paid_invoices = paid_df.shape[0]

total_late_invoices = (paid_df["payment_delay_days"] > 0).sum()

total_early_invoices = (paid_df["payment_delay_days"] < 0).sum()

total_on_time_invoices = (paid_df["payment_delay_days"] == 0).sum()

average_payment_delay = paid_df["payment_delay_days"].mean()

print("\nCUSTOMER ANALYSIS SUMMARY")
print("--------------------------------")
print("Total Customers:", total_customers)
print("Repeat Customers:", repeat_customers)
print("One-time Customers:", one_time_customers)
print("Total Paid Invoices:", total_paid_invoices)
print("Late Invoices:", total_late_invoices)
print("On-time Invoices:", total_on_time_invoices)
print("Early Invoices:", total_early_invoices)
print("Average Payment Delay:", round(average_payment_delay, 2), "days")
print("Total Outstanding Amount:", round(total_outstanding, 2))

print("--------------------------------")
print("CUSTOMER ANALYSIS COMPLETED!")