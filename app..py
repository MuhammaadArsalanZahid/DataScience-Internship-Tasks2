import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("superstore.csv")

# Dashboard title
st.title("Global Superstore Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

region = st.sidebar.selectbox(
    "Select Region",
    df["Region"].unique()
)

category = st.sidebar.selectbox(
    "Select Category",
    df["Category"].unique()
)

# Apply filters
filtered_df = df[
    (df["Region"] == region) &
    (df["Category"] == category)
]

# KPIs
st.subheader("Key Performance Indicators")

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()

st.write("Total Sales:", total_sales)
st.write("Total Profit:", total_profit)
st.write("Total Orders:", total_orders)

# Top 5 customers
st.subheader("Top 5 Customers")

top_customers = (
    filtered_df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

st.bar_chart(top_customers)

# Profit by Sub-Category
st.subheader("Profit by Sub-Category")

profit_subcategory = (
    filtered_df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values()
)

st.bar_chart(profit_subcategory)

# Sales Trend
st.subheader("Sales Trend")

df["Order Date"] = pd.to_datetime(df["Order Date"])
sales_trend = (
    filtered_df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

sales_trend.index = sales_trend.index.astype(str)

st.line_chart(sales_trend)

# Show filtered data
st.subheader("Filtered Data")
st.dataframe(filtered_df)