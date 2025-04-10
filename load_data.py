

import pandas as pd
from database import connect_db

def load_csv_to_sqlite():
    conn = connect_db()
    cursor = conn.cursor()



    # Create tables with correct schema
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            age INTEGER,
            gender TEXT,
            location TEXT,
            browsing_history TEXT,
            purchase_history TEXT,
            customer_segment TEXT,
            avg_order_value REAL,
            holiday TEXT,
            season TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price REAL,
            embedding TEXT
        )
    """)

    # Load customers CSV
    customers = pd.read_csv("datasets/customer_data_collection.csv")

    # Rename columns to match DB schema
    customers = customers.rename(columns={
        "Customer_ID": "id",
        "Age": "age",
        "Gender": "gender",
        "Location": "location",
        "Browsing_History": "browsing_history",
        "Purchase_History": "purchase_history",
        "Customer_Segment": "customer_segment",
        "Avg_Order_Value": "avg_order_value",
        "Holiday": "holiday",
        "Season": "season"
    })

    # Load products CSV
    products = pd.read_csv("datasets/product_recommendation_data.csv")

    # Save data to SQLite
    customers.to_sql("customers", conn, if_exists="replace", index=False)
    products.to_sql("products", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
    print("✅ Data loaded successfully.")

if __name__ == "__main__":
    load_csv_to_sqlite()
   
