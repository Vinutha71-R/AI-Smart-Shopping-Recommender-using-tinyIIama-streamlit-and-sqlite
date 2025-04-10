"""from database import connect_db

def recommend_products_for_customer(customer_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products LIMIT 5")  # Dummy logic
    return cursor.fetchall()
"""
# agents/recommender_agent.py
import ollama

def format_customer_info(row):
    return f"""
    Location: {row['location']}
    Age: {row['age']}
    Gender: {row['gender']}
    Segment: {row['customer_segment']}
    Avg Order Value: ₹{row['avg_order_value']}
    Season: {row['season']}
    Holiday: {row['holiday']}
    Browsing History: {row['browsing_history']}
    Purchase History: {row['purchase_history']}
    """

def recommend_products_for_customer(row):
    customer_info = format_customer_info(row)

    prompt = f"""
    Based on the customer profile below, recommend 3 product categories they are likely to purchase. 
    Be specific and keep the response short, mentioning category and a rough amount.

    Customer Info:
    {customer_info}
    """

    response = ollama.chat(
        model='tinyllama',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']
