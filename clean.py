import pandas as pd
import numpy as np

df = pd.read_csv("pandas_data_cleaning_practice.csv")   # apni raw file ka naam likho
df = df.copy()

# 1. Text columns: spaces + case
for col in ["Name", "City", "Department", "Gender", "Status", "Remote_Work", "Email"]:
    df[col] = df[col].str.strip()

df["Name"] = df["Name"].str.title()
df["Email"] = df["Email"].str.lower()
df["Department"] = df["Department"].str.upper()
df["Status"] = df["Status"].str.title()
df["Remote_Work"] = df["Remote_Work"].str.title()

# 2. City standardize
city_map = {"lhr": "Lahore", "lahore": "Lahore",
            "khi": "Karachi", "karachi": "Karachi",
            "isb": "Islamabad", "islamabad": "Islamabad",
            "rawalpindi": "Rawalpindi", "rwp": "Rawalpindi"}
df["City"] = df["City"].str.lower().map(city_map).fillna(df["City"].str.title())

# 3. Gender standardize
gender_map = {"m": "Male", "male": "Male", "f": "Female", "female": "Female"}
df["Gender"] = df["Gender"].str.lower().map(gender_map)

# 4. Age / Salary -> numbers
for col in ["Age", "Salary"]:
    df[col] = df[col].astype(str).str.replace(r"[^\d.]", "", regex=True)
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.loc[(df["Age"] < 18) | (df["Age"] > 70), "Age"] = np.nan   # outliers

# 5. Join_Date: 3 formats
def parse_date(s):
    if pd.isna(s):
        return pd.NaT
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"):
        try:
            return pd.to_datetime(str(s).strip(), format=fmt)
        except ValueError:
            pass
    return pd.NaT          # invalid-date yahan NaT ban jayegi

df["Join_Date"] = df["Join_Date"].apply(parse_date)
df.loc[df["Join_Date"] > pd.Timestamp.today(), "Join_Date"] = pd.NaT

# 6. Duplicates
df = df.drop_duplicates()
df = df.drop_duplicates(subset="Employee_ID", keep="first")

# 7. Missing values
df["Age_Missing"] = df["Age"].isna()
df["Salary_Missing"] = df["Salary"].isna()
for col in ["City", "Department", "Gender", "Status", "Remote_Work"]:
    df[col] = df[col].fillna("Unknown")

# 8. Check + save
print(df.isna().sum())
print(df["City"].value_counts())
df.to_csv("clean_employees.csv", index=False)