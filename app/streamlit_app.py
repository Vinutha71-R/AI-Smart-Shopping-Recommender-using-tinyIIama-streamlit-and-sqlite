import streamlit as st
import sys
import os
import pandas as pd
import sqlite3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.recommender import recommend_products_for_customer

# Load data
conn = sqlite3.connect("smart_shopping.db")
df = pd.read_sql_query("SELECT * FROM customers", conn)
# Drop unnamed columns (those without headers)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]


# 🧽 Clean column names
df.columns = df.columns.str.strip()

# 🔍 Show available columns for debugging
st.markdown(f"**Available columns:** {', '.join(df.columns)}")


st.title("🛍️ Smart Shopping AI Recommender")

# Now this should work if those columns exist
if 'id' in df.columns and 'location' in df.columns:
    customer_options = df[['id', 'location']].drop_duplicates()
    customer_display = customer_options.apply(lambda x: f"{x['id']} - {x['location']}", axis=1)

    selected_display = st.selectbox("Select a Customer", customer_display)
    selected_id = selected_display.split(' - ')[0]
    selected_row = df[df["id"] == selected_id].iloc[0]

    if st.button("Recommend Products"):
        with st.spinner("Generating AI-powered recommendations..."):
            recommendation = recommend_products_for_customer(selected_row)

        st.success("Here are your personalized recommendations:")
        st.markdown(recommendation)
else:
    st.error("The required columns 'id' and 'location' are not found in the database.")
