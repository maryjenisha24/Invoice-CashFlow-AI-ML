
import pandas as pd
import os

# Load cleaned dataset
file_path = "data/cleaned/cleaned_dataset.csv"
df = pd.read_csv(file_path)

print("\n===== FINAL DATASET VERIFICATION =====")

# Dataset shape
print("\nDataset Shape:", df.shape)

# Duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Empty columns
print("\nEmpty Columns:",
      df.columns[df.isnull().all()].tolist())

# Missing values
print("\nTotal Missing Values:", df.isnull().sum().sum())

# Column names
print("\nTotal Columns:", len(df.columns))

# Record count
print("\nTotal Records:", len(df))

# Final confirmation
if df.shape == (48839, 18) and df.duplicated().sum() == 0:
    print("\nFINAL VERIFICATION SUCCESSFUL!")
else:
    print("\nPLEASE INVESTIGATE DATASET!")
