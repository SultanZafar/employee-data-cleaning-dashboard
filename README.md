# Employee Data Cleaning & Dashboard

Messy HR dataset (1,206 rows) ko clean karke interactive dashboard banaya.

**Live demo:** https://employee-dashboard-sultan.streamlit.app

![Dashboard](screenshots/dashboard.png)

## Problem
Raw data me inconsistent city names (LHR / lahore / Lahore), 3 alag date formats,
hidden missing values ("unknown", "not available", "invalid-date"), duplicates
aur mixed Gender/Status spellings thin.

## What I did
- Text standardization (City, Department, Gender, Status)
- Hidden missing values detect karke NaN me convert kiye
- 3 date formats parse kiye, 4 duplicate rows hataye
- Missing values ka documented strategy (flag columns + "Unknown")
- Streamlit dashboard: KPIs, filters, salary / headcount / hiring trend charts

## Tech
Python, Pandas, Plotly, Streamlit

## Run locally
pip install -r requirements.txt
python clean.py
streamlit run dashboard.py