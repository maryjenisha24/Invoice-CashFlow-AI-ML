
import pandas as pd
import numpy as np

file_path = "data/raw/dataset.csv"

df = pd.read_csv(file_path)

print("\n========== DATASET INFORMATION ==========")
print("Shape:", df.shape)

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE RECORDS ==========")
print("Duplicate rows:", df.duplicated().sum())

print("\n========== UNIQUE VALUES ==========")
print("Unique customers:", df["cust_number"].nunique())
print("Unique invoice IDs:", df["invoice_id"].nunique())

print("\n========== NUMERICAL SUMMARY ==========")
print(df.describe())

print("\n========== PROFILING COMPLETED ==========")
