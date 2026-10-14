import pandas as pd

raw = pd.read_csv("pandas_data_cleaning_practice.csv")

age = pd.to_numeric(raw["Age"], errors="coerce")
print("Age ganda text:", raw.loc[age.isna() & raw["Age"].notna(), "Age"].unique())
print("Age out of range:", sorted(age[(age < 18) | (age > 70)].unique()))

sal = pd.to_numeric(raw["Salary"], errors="coerce")
print("\nSalary ganda text:", raw.loc[sal.isna() & raw["Salary"].notna(), "Salary"].unique())
print("Salary negative count:", (sal < 0).sum())
print(sal.describe())

pattern = r"^(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4})$"
bad = raw["Join_Date"].notna() & ~raw["Join_Date"].astype(str).str.match(pattern)
print("\nJoin_Date ajeeb format:", raw.loc[bad, "Join_Date"].unique())