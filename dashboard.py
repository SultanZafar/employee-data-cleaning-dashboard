import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Employee Dashboard", layout="wide")


# ---------- 1. Data load ----------
@st.cache_data
def load_data():
    return pd.read_csv("clean_employees.csv", parse_dates=["Join_Date"])


df = load_data()

st.title("Employee Dashboard")

# ---------- 2. Sidebar filters ----------
st.sidebar.header("Filters")
multi = st.sidebar.toggle("Multi-select mode")


def make_filter(name, column):
    options = sorted(df[column].unique())
    if multi:
        chosen = st.sidebar.multiselect(name, options, placeholder="All")
    else:
        pick = st.sidebar.selectbox(name, ["All"] + options)
        chosen = [] if pick == "All" else [pick]
    values = chosen if chosen else options   # khali = All
    return values, chosen


sel_city, ch_city = make_filter("City", "City")
sel_dept, ch_dept = make_filter("Department", "Department")
sel_status, ch_status = make_filter("Status", "Status")

f = df[
    df["City"].isin(sel_city)
    & df["Department"].isin(sel_dept)
    & df["Status"].isin(sel_status)
]


def show(chosen):
    return ", ".join(chosen) if chosen else "All"


if f.empty:
    st.warning("Filters ke mutabiq koi data nahi mila.")
    st.stop()

# Kaun sa filter laga hai, ye upar dikhao
st.info(
    f"**Showing:** City = {show(ch_city)}  |  "
    f"Department = {show(ch_dept)}  |  "
    f"Status = {show(ch_status)}  |  "
    f"{len(f):,} employees"
)

# ---------- 3. KPI cards ----------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Employees", f"{len(f):,}")
c2.metric("Average Salary", f"{f['Salary'].mean():,.0f}")
c3.metric("Active %", f"{(f['Status'] == 'Active').mean() * 100:.1f}%")
c4.metric("Remote %", f"{(f['Remote_Work'] == 'Yes').mean() * 100:.1f}%")

st.divider()

# ---------- 4. Charts ----------
left, right = st.columns(2)

with left:
    dept_sal = f.groupby("Department", as_index=False)["Salary"].mean()
    fig1 = px.bar(
        dept_sal, x="Department", y="Salary",
        title=f"Average Salary by Department ({show(ch_city)})",
    )
    st.plotly_chart(fig1, use_container_width=True)

    status_cnt = f["Status"].value_counts().reset_index()
    status_cnt.columns = ["Status", "Count"]
    fig3 = px.pie(
        status_cnt, names="Status", values="Count",
        hole=0.4, title="Status Breakdown",
    )
    st.plotly_chart(fig3, use_container_width=True)

with right:
    city_cnt = f["City"].value_counts().reset_index()
    city_cnt.columns = ["City", "Headcount"]
    fig2 = px.bar(
        city_cnt, x="City", y="Headcount",
        title=f"Headcount by City ({show(ch_dept)})",
    )
    st.plotly_chart(fig2, use_container_width=True)

    hires = f.dropna(subset=["Join_Date"]).copy()
    hires["Month"] = hires["Join_Date"].dt.to_period("M").dt.to_timestamp()
    monthly = hires.groupby("Month").size().reset_index(name="Hires")
    fig4 = px.line(monthly, x="Month", y="Hires", title="Monthly Hiring Trend")
    st.plotly_chart(fig4, use_container_width=True)

# ---------- 5. Data quality note ----------
st.caption(
    f"Missing: Age {f['Age'].isna().sum()}, "
    f"Salary {f['Salary'].isna().sum()}, "
    f"Join_Date {f['Join_Date'].isna().sum()} "
    "(averages sirf available values par based hain)"
)