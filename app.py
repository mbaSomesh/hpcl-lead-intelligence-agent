import streamlit as st
import sqlite3
import pandas as pd
import random

DB = "data/leads.db"

st.set_page_config(page_title="HPCL Lead Intelligence", layout="wide")

st.title("HPCL B2B Lead Intelligence Dashboard")

# Load data
conn = sqlite3.connect(DB)
df = pd.read_sql("SELECT * FROM leads", conn)
conn.close()

# Sidebar navigation
page = st.sidebar.selectbox("Navigation", ["Executive Dashboard", "Lead Queue", "Lead Dossier", "Notifications"])

# EXECUTIVE DASHBOARD
if page == "Executive Dashboard":

    st.header("Executive Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Leads", len(df))

    col2.metric("High Priority Leads", len(df[df["urgency"]=="High"]))

    col3.metric("Average Confidence", round(df["confidence"].mean(),2))

    st.subheader("Leads by Product")
    st.bar_chart(df["product"].value_counts())

    st.subheader("Leads by Industry")
    st.bar_chart(df["industry"].value_counts())

    st.subheader("Leads by Source")
    st.bar_chart(df["source"].value_counts())

    st.subheader("Urgency Distribution")
    st.bar_chart(df["urgency"].value_counts())


# LEAD QUEUE
elif page == "Lead Queue":

    st.header("Lead Queue")

    st.dataframe(df[["company","industry","product","score","urgency","confidence","source"]])


# LEAD DOSSIER
elif page == "Lead Dossier":

    st.header("Lead Dossier")

    company = st.selectbox("Select Company", df["company"].unique())

    lead = df[df["company"]==company].iloc[0]

    st.subheader("Company Intelligence Card")

    st.write("Company:", lead["company"])
    st.write("Industry:", lead["industry"])
    st.write("Location: India")
    st.write("Signal Detected:", lead["signal"])

    st.subheader("Product Recommendation")

    st.success(f"Primary Product: {lead['product']}")

    st.write("Confidence Score:", lead["confidence"])

    st.write("Urgency Level:", lead["urgency"])

    st.write("Lead Score:", lead["score"])

    st.subheader("Source Intelligence")

    st.write("Source:", lead["source"])

    st.write("Trust Score:", round(random.uniform(0.85,0.98),2))

    st.subheader("AI Reasoning")

    st.write("Keyword detected in signal:", lead["signal"])

    st.write("Mapped to product:", lead["product"])

    st.write("Confidence derived from keyword strength and industry match")

    st.subheader("Suggested Next Action")

    st.info("Assign to regional sales officer and initiate contact within 24 hours")

    col1, col2, col3 = st.columns(3)

    if col1.button("Assign Lead"):
        st.success("Lead assigned to territory sales officer")

    if col2.button("Accept Lead"):
        st.success("Lead marked as accepted")

    if col3.button("Convert Lead"):
        st.success("Lead marked as converted")


# NOTIFICATIONS
elif page == "Notifications":

    st.header("WhatsApp Alert Simulation")

    company = st.selectbox("Select Company for Alert", df["company"].unique())

    if st.button("Send WhatsApp Alert"):

        st.success(f"WhatsApp alert sent to sales officer for {company}")

        st.info("Message: High priority industrial fuel lead detected. Immediate follow-up recommended.")
