import pandas as pd

df = pd.read_csv("data/raw/dataset.csv")

print("===== FULL DUPLICATE CHECK =====")

duplicates = df[
    df.duplicated(subset=["doc_id"], keep=False)
]

comparison = duplicates.groupby("doc_id").nunique()

different_columns = comparison.columns[
    (comparison > 1).any()
].tolist()

print("Columns with differences:", different_columns)

if different_columns:
    print("\nDifferences found. We need to investigate.")
else:
    print("\nNo differences found in repeated doc_id groups.")

print("\n===== CHECK COMPLETED =====")
