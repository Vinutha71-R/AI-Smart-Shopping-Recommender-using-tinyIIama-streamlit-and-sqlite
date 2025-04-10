from database import connect_db

class CustomerAgent:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.customer_data = self.get_customer_data()

    def get_customer_data(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE id = ?", (self.customer_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                "id": row[0],
                "name": row[1],
                "age": row[2],
                "gender": row[3],
                "location": row[4]
            }
        return None

    def get_customer_profile(self):
        return self.customer_data

    def summarize_profile(self):
        if not self.customer_data:
            return "Unknown Customer"
        return f"{self.customer_data['name']}, {self.customer_data['age']} yrs, {self.customer_data['location']}"
