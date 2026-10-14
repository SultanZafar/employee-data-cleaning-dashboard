import pandas as pd

raw = pd.read_csv("pandas_data_cleaning_practice.csv")

age = pd.to_numeric(raw["Age"], errors="coerce")
print("Age ganda text:", raw.loc[age.isna() & raw["Age"].notna(), "Age"].unique())
print("Age out of range:", sorted(age[(age < 18) | (age > 70)].unique()))
print("Age out of range count:", ((age < 18) | (age > 70)).sum())

print("\ninvalid-date count:", (raw["Join_Date"] == "invalid-date").sum())

d = raw["Join_Date"].dropna()
d = d[d != "invalid-date"]
parsed = pd.to_datetime(d, format="%Y-%m-%d", errors="coerce")
parsed = parsed.fillna(pd.to_datetime(d, format="%d/%m/%Y", errors="coerce"))
parsed = parsed.fillna(pd.to_datetime(d, format="%m-%d-%Y", errors="coerce"))
print("Parse fail (invalid-date ke ilawa):", parsed.isna().sum())
print("Future dates:", (parsed > pd.Timestamp.today()).sum())