import sqlite3

conn = sqlite3.connect("smart_shopping.db")  # Make sure the name matches
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)

if ('customers',) not in tables:
    print("❌ 'customers' table NOT found!")
else:
    print("✅ 'customers' table exists.")

conn.close()
