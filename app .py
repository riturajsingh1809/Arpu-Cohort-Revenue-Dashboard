
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ARPU & Cohort Revenue Dashboard", layout="wide")

st.title("📊 ARPU & Cohort Revenue Dashboard")
st.write("Task 9 - Failure Handling & Resilience")

df = pd.read_csv("Cleaned_Payment_Data.csv")

total_revenue = df["Amount"].sum()
total_users = df["User_ID"].nunique()
arpu = total_revenue / total_users

success = len(df[df["Payment_Status"]=="Success"])
failed = len(df[df["Payment_Status"]=="Failed"])

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Users", total_users)
col3.metric("ARPU", f"₹{arpu:.2f}")
col4.metric("Failed Payments", failed)

st.subheader("Revenue by Plan")
plan = df.groupby("Plan")["Amount"].sum()
st.bar_chart(plan)

st.subheader("Revenue by Country")
country = df.groupby("Country")["Amount"].sum()
st.bar_chart(country)

st.subheader("Monthly Revenue")
df["Payment_Date"] = pd.to_datetime(df["Payment_Date"])
monthly = df.groupby(df["Payment_Date"].dt.to_period("M"))["Amount"].sum()
monthly.index = monthly.index.astype(str)
st.line_chart(monthly)

st.subheader("Dataset Preview")
st.dataframe(df)

st.success("Dashboard Created Successfully")
