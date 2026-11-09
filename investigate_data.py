
import pandas as pd

df = pd.read_csv("data/raw/dataset.csv")

print("\n===== PAYMENT STATUS CHECK =====")
print(pd.crosstab(df["isOpen"], df["clear_date"].isnull()))

print("\n===== DUPLICATE DOC IDs =====")
print("Duplicate doc_id:", df["doc_id"].duplicated().sum())

print("\n===== DUPLICATE INVOICE IDs =====")
print("Duplicate invoice_id:", df["invoice_id"].duplicated().sum())

print("\n===== MISSING INVOICE ID RECORDS =====")
print(df[df["invoice_id"].isnull()])

print("\n===== EXACT DUPLICATE SAMPLE =====")
print(df[df.duplicated(keep=False)].head(10))

print("\n===== DATE SAMPLE =====")
print(df[["posting_date", "clear_date", "due_in_date"]].head(10))

print("\n===== INVESTIGATION COMPLETED =====")
