from load_data import load_csv_to_sqlite
from agents.recommender_agent import recommend_products_for_customer

def main():
    print("📥 Loading data into SQLite...")
    load_csv_to_sqlite()

    print("🤖 Running recommender agent for customer ID = 1")
    recommendations = recommend_products_for_customer(1)
    for rec in recommendations:
        print(f"Recommended: {rec[1]} - ₹{rec[3]}")

if __name__ == "__main__":
    main()
