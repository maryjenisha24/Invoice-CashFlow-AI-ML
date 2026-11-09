
import pandas as pd

df = pd.read_csv("data/raw/dataset.csv")

print("\n===== DOC ID VALIDATION =====")

doc_check = df.groupby("doc_id").agg(
    record_count=("doc_id", "size"),
    customer_count=("cust_number", "nunique"),
    amount_count=("total_open_amount", "nunique"),
    date_count=("posting_date", "nunique")
)

print("Repeated doc_id groups:", (doc_check["record_count"] > 1).sum())
print("Groups with different customers:", (doc_check["customer_count"] > 1).sum())
print("Groups with different amounts:", (doc_check["amount_count"] > 1).sum())
print("Groups with different posting dates:", (doc_check["date_count"] > 1).sum())

print("\n===== INVOICE ID VALIDATION =====")

invoice_check = df.dropna(subset=["invoice_id"]).groupby("invoice_id").agg(
    record_count=("invoice_id", "size"),
    customer_count=("cust_number", "nunique"),
    amount_count=("total_open_amount", "nunique"),
    date_count=("posting_date", "nunique")
)

print("Repeated invoice groups:", (invoice_check["record_count"] > 1).sum())
print("Groups with different customers:", (invoice_check["customer_count"] > 1).sum())
print("Groups with different amounts:", (invoice_check["amount_count"] > 1).sum())
print("Groups with different posting dates:", (invoice_check["date_count"] > 1).sum())

print("\n===== VALIDATION COMPLETED =====")
