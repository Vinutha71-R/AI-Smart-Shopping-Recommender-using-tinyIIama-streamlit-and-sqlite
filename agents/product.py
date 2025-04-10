from database import connect_db

class ProductAgent:
    def __init__(self):
        self.conn = connect_db()

    def get_all_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()

    def get_products_by_category(self, category):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products WHERE category = ?", (category,))
        return cursor.fetchall()

    def get_product_embedding(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT embedding FROM products WHERE id = ?", (product_id,))
        result = cursor.fetchone()
        return result[0] if result else None

    def close(self):
        self.conn.close()
