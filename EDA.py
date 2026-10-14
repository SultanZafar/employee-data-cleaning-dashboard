import pandas as pd
import shutil
import os

# load raw dataset
# ==============================
raw_file = "pandas_data_cleaning_practice.csv"

df = pd.read_csv(raw_file)

print("First 5 rows:")
print(df.head())

# ==============================
# 2. CREATE BACKUP
# ==============================
os.makedirs("backup", exist_ok=True)

backup_file = "backup/raw_backup.csv"

if not os.path.exists(backup_file):
    shutil.copy2(
        raw_file,
        backup_file
    )
    print("original backup created successfully.")
else:
    print("backup already exists. No new backup created.")
# Load dataset
df = pd.read_csv("pandas_data_cleaning_practice.csv")

# 1. Number of rows and columns
print("\nDATA SHAPE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns)

print("\nDATA INFORMATION:")
df.info()

print("\nSTATISTICS:")
print(df.describe())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# STEP 2A: ANALYZE MISSING VALUES
missing_count = df.isna().sum()

missing_percent = (
    df.isna().sum() / len(df) * 100
).round(2)

missing_report = pd.DataFrame({
    "Missing_count":missing_count,
    "Missing_Percent": missing_percent
})
print("\nMISSING VALUES ANALYSIS:")
print(missing_report)

# STEP 2B: INSPECT MISSING AGE RECORDS

missing_age_rows = df[df["Age"].isna()]

print("\nROWS WITH MISSING AGE:")
print(missing_age_rows.head(10))

print("\nTOTAL ROWS WITH MISSING AGE:")
print(len(missing_age_rows))

# STEP 2C: PRESERVE RECORDS WITH MISSING AGE

missing_age_rows = df[df["Age"].isna()].copy()
os.makedirs("rejected", exist_ok=True)

missing_age_rows.to_csv("rejected/missing_age_records.csv", index=False)
print("\nMissing Age records saved safely.")
print("Records saved:", len(missing_age_rows))
print("Original dataset rows:", len(df))

missing_salary_column = df[df["Salary"].isna()]
print("\nROWS WITH MISSING SALARY:")
print(missing_salary_column.head(10))
print('\nTOTAL ROWS WITH MISSING SALARY:')
print(len(missing_salary_column))

print('\nPERCENTAGE OF ROWS WITH MISSING SALARY:')
print((df["Salary"].isna().sum() / len(df)) * 100)

# ==============================
# STEP 3: PRESERVE REMAINING MISSING RECORDS
# ==============================

os.makedirs("rejected", exist_ok=True)

# Missing Salary records save
missing_salary_rows = df[df["Salary"].isna()].copy()
missing_salary_rows.to_csv("rejected/missing_salary_records.csv", index=False)
print("\nMissing Salary records saved safely.")
print("Records saved:", len(missing_salary_rows))

# Missing City records save
missing_city_rows = df[df["City"].isna()].copy()
missing_city_rows.to_csv("rejected/missing_city_records.csv", index=False)
print("\nMissing City records saved safely.")
print("Records saved:", len(missing_city_rows))

# Missing Department records save
missing_dept_rows = df[df["Department"].isna()].copy()
missing_dept_rows.to_csv("rejected/missing_department_records.csv", index=False)
print("\nMissing Department records saved safely.")
print("Records saved:", len(missing_dept_rows))

# Missing Gender records save
missing_gender_rows = df[df["Gender"].isna()].copy()
missing_gender_rows.to_csv("rejected/missing_gender_records.csv", index=False)
print("\nMissing Gender records saved safely.")
print("Records saved:", len(missing_gender_rows))

# Missing Email records save
missing_email_rows = df[df["Email"].isna()].copy()
missing_email_rows.to_csv("rejected/missing_email_records.csv", index=False)
print("\nMissing Email records saved safely.")
print("Records saved:", len(missing_email_rows))

# Missing Join_Date records save
missing_date_rows = df[df["Join_Date"].isna()].copy()
missing_date_rows.to_csv("rejected/missing_join_date_records.csv", index=False)
print("\nMissing Join_Date records saved safely.")
print("Records saved:", len(missing_date_rows))

# Missing Status records save
missing_status_rows = df[df["Status"].isna()].copy()
missing_status_rows.to_csv("rejected/missing_status_records.csv", index=False)
print("\nMissing Status records saved safely.")
print("Records saved:", len(missing_status_rows))

# Missing Remote_Work records save
missing_remote_rows = df[df["Remote_Work"].isna()].copy()
missing_remote_rows.to_csv("rejected/missing_remote_work_records.csv", index=False)
print("\nMissing Remote_Work records saved safely.")
print("Records saved:", len(missing_remote_rows))

print("Original rows:", len(df))
print("Missing values:", df.isna().sum().sum())

missing_percent = (df["Age"].isna().sum() / len(df)) * 100
print("\nPercentage of rows with missing Age:", missing_percent)

# STEP 3: CREATE WORKING COPY

clean_df = df.copy()

print("Original rows:", len(df))
print("Working copy rows:", len(clean_df))
print("Original columns:", len(df.columns))
print("Working copy columns:", len(clean_df.columns))

# STEP 4: CHECK MISSING VALUES

print("\nMissing values in working copy:")
print(clean_df.isnull().sum())