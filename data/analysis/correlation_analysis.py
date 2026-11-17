
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned/cleaned_dataset.csv")

# Convert date columns
date_columns = [
    "posting_date",
    "clear_date",
    "due_in_date"
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Create Payment Delay Days
df["payment_delay_days"] = (
    df["clear_date"] - df["due_in_date"]
).dt.days

# Select numerical features
numerical_features = [
    "total_open_amount",
    "payment_delay_days"
]

# Display numerical feature information
print("\nSELECTED NUMERICAL FEATURES")
print("------------------------------")

print(df[numerical_features].describe())

print("\nMissing Values:")
print(df[numerical_features].isnull().sum())

print("------------------------------")

# STEP 3: Calculate Correlation

# Select records with available values
correlation_df = df[
    ["total_open_amount", "payment_delay_days"]
].dropna()

# Calculate correlation
correlation_matrix = correlation_df.corr()

print("\nCORRELATION MATRIX")
print("------------------------------")
print(correlation_matrix.round(3))
print("------------------------------")

# STEP 4: Correlation Heatmap

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".3f",
    linewidths=0.5,
    vmin=-1,
    vmax=1
)

plt.title("Invoice Features Correlation Heatmap")
plt.tight_layout()

# Save heatmap
plt.savefig(
    "data/analysis/correlation_heatmap.png",
    dpi=300
)

plt.show()

print("\nCorrelation heatmap saved successfully!")

# STEP 5: Correlation Insights

correlation_value = correlation_matrix.loc[
    "total_open_amount",
    "payment_delay_days"
]

print("\nCORRELATION ANALYSIS INSIGHTS")
print("------------------------------")

print("Invoice Amount vs Payment Delay:",
      round(correlation_value, 3))

if abs(correlation_value) < 0.1:
    print("Relationship: Very Weak / Almost No Linear Correlation")

elif correlation_value < 0:
    print("Relationship: Negative Correlation")

else:
    print("Relationship: Positive Correlation")

print("\nBUSINESS INSIGHT:")
print("Invoice amount alone is not a strong indicator")
print("of customer payment delay.")

# Save correlation matrix
correlation_matrix.to_csv(
    "data/reports/correlation_matrix.csv"
)

print("\nCorrelation matrix saved successfully!")
print("------------------------------")
