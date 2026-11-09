
import pandas as pd

df = pd.read_csv("data/raw/dataset.csv")

print("\n===== EXACT DUPLICATE COUNT =====")
print(df.duplicated().sum())

print("\n===== DOC ID DUPLICATE RECORDS =====")
doc_duplicates = df[df.duplicated(subset=["doc_id"], keep=False)]
print("Total records:", len(doc_duplicates))
print(doc_duplicates[["doc_id", "cust_number", "posting_date",
                      "total_open_amount"]].head(15))

print("\n===== INVOICE ID DUPLICATE RECORDS =====")
invoice_duplicates = df[
    df.duplicated(subset=["invoice_id"], keep=False)
]
print("Total records:", len(invoice_duplicates))
print(invoice_duplicates[["invoice_id", "cust_number",
                          "posting_date", "total_open_amount"]].head(15))

print("\n===== DUPLICATE ANALYSIS COMPLETED =====")
