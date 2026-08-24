import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sneha",
    database="ds_sql_practice",
    port=3307
)

print("Database connected successfully!")

cur = conn.cursor(dictionary=True)

query = """
SELECT 'customers' AS table_name, COUNT(*) AS row_count
FROM customers

UNION ALL

SELECT 'products', COUNT(*)
FROM products

UNION ALL

SELECT 'orders', COUNT(*)
FROM orders

UNION ALL

SELECT 'order_items', COUNT(*)
FROM order_items

UNION ALL

SELECT 'payments', COUNT(*)
FROM payments;
"""

cur.execute(query)

rows = cur.fetchall()

for row in rows:
    print(row)


cur.close()
conn.close()