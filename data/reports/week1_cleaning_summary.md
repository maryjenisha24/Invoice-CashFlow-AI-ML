# WEEK 1 – DATA CLEANING AND PREPROCESSING

## Project Title
Invoice Payment Delay & Cash-Flow Intelligence Platform

## Internship Organization
Orvians Technologies

## 1. Project Objective

The objective is to clean and preprocess historical invoice payment data for developing an AI/ML platform that predicts payment delays, customer payment risks, and future cash collections.

## 2. Dataset Information

- Dataset: Customer Invoices Dataset
- Original Records: 50,000
- Original Columns: 19

## 3. Data Cleaning Activities

The following activities were performed:

1. Dataset loading and initial inspection.
2. Missing value analysis.
3. Duplicate record identification and removal.
4. Column quality inspection.
5. Date format conversion.
6. Text data cleaning and whitespace removal.
7. Invoice status validation.
8. Date anomaly investigation.
9. Final dataset verification.

## 4. Duplicate Removal

- Duplicate rows identified and removed: 1,161
- Remaining duplicate rows: 0
- Unique document IDs: 48,839

## 5. Missing Value Analysis

- Missing clear dates for open invoices were preserved.
- Missing invoice IDs were identified.
- No completely empty columns remain.

## 6. Date Quality Investigation

Date-related anomalies were investigated.

- Baseline after posting: Preserved.
- Due before posting: Preserved.
- Baseline after due: No records found.
- Clear before posting: No records found.
- Clear before due: Preserved.
- Missing clear dates for open invoices: Preserved.
- Invoice status mismatches: None.

A separate Date Quality Report was generated.

## 7. Final Dataset Results

- Total Records: 48,839
- Total Columns: 18
- Duplicate Rows: 0
- Empty Columns: 0
- Missing Values: 9,687

## 8. Output Files

- data/cleaned/cleaned_dataset.csv
- data/reports/date_quality_report.csv
- data/reports/date_quality_summary.md

## 9. Conclusion

Week 1 data cleaning and preprocessing activities have been completed.

The final cleaned dataset was successfully verified. Duplicate rows were removed, date fields were investigated, and legitimate missing values were preserved.

The cleaned dataset is ready for the next stages of the Invoice Payment Delay & Cash-Flow Intelligence Platform project.