
import pandas as pd

df = pd.read_csv("data/raw/dataset.csv")

print("\n===== DUPLICATE RECORD COMPARISON =====")

duplicates = df[
    df.duplicated(subset=["doc_id"], keep=False)
]

comparison = duplicates.groupby("doc_id").nunique()

print("Groups with different clear dates:",
      (comparison["clear_date"] > 1).sum())

print("Groups with different payment terms:",
      (comparison["cust_payment_terms"] > 1).sum())

print("Groups with different open status:",
      (comparison["isOpen"] > 1).sum())

print("Groups with different currencies:",
      (comparison["invoice_currency"] > 1).sum())

print("\n===== FINAL CHECK COMPLETED =====")
