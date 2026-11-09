
import pandas as pd
import os

# Step 1: Create date quality report data
report_data = [
    {
        "Date Condition": "Baseline after posting",
        "Records": 3198,
        "Decision": "Preserve",
        "Remarks": "Investigated and retained"
    },
    {
        "Date Condition": "Due before posting",
        "Records": 137,
        "Decision": "Preserve",
        "Remarks": "Investigated and retained"
    },
    {
        "Date Condition": "Baseline after due",
        "Records": 0,
        "Decision": "No records found",
        "Remarks": "No anomaly detected"
    },
    {
        "Date Condition": "Clear before posting",
        "Records": 0,
        "Decision": "No records found",
        "Remarks": "No anomaly detected"
    },
    {
        "Date Condition": "Clear before due",
        "Records": 14469,
        "Decision": "Preserve",
        "Remarks": "Investigated and retained"
    },
    {
        "Date Condition": "Missing clear date for open invoices",
        "Records": 9681,
        "Decision": "Preserve",
        "Remarks": "Legitimate missing values"
    },
    {
        "Date Condition": "Invoice status mismatch",
        "Records": 0,
        "Decision": "None",
        "Remarks": "No mismatches detected"
    }
]

# Step 2: Convert into DataFrame
report_df = pd.DataFrame(report_data)

# Step 3: Create reports folder
output_folder = "data/reports"
os.makedirs(output_folder, exist_ok=True)

# Step 4: Save report
output_file = os.path.join(
    output_folder,
    "date_quality_report.csv"
)

report_df.to_csv(output_file, index=False)

# Step 5: Display report
print("\n===== DATE QUALITY REPORT =====")
print(report_df.to_string(index=False))

print("\nReport saved successfully!")
print("Output file:", output_file)
