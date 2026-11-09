import pandas as pd
import os

# Step 1: Load original dataset
input_file = "data/raw/dataset.csv"

df = pd.read_csv(input_file)

print("Original Dataset Loaded Successfully!")
print("Original Shape:", df.shape)

# Step 2: Remove exact duplicate rows
duplicates_before = df.duplicated().sum()

df = df.drop_duplicates()

duplicates_removed = duplicates_before

print("\nExact Duplicate Rows Removed:", duplicates_removed)

# Step 3: Remove completely empty columns
empty_columns = df.columns[df.isnull().all()].tolist()

df = df.dropna(axis=1, how="all")

print("Completely Empty Columns Removed:", empty_columns)

# Step 4: Create output folder
output_folder = "data/cleaned"

os.makedirs(output_folder, exist_ok=True)

# Step 5: Save cleaned dataset
output_file = os.path.join(output_folder, "cleaned_dataset.csv")

df.to_csv(output_file, index=False)

# Step 6: Display final results
print("\n===== CLEANING SUMMARY =====")
print("Final Dataset Shape:", df.shape)
print("Remaining Duplicate Rows:", df.duplicated().sum())
print("Remaining Empty Columns:", df.columns[df.isnull().all()].tolist())
print("Cleaned Dataset Saved Successfully!")
print("Output File:", output_file)