import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="ds_sql_practice",
    port=3307
)

print("Database connected successfully!\n")

cur = conn.cursor(dictionary=True)



print("===== EXERCISE 14: JOIN ORDERS TO CUSTOMERS =====")

query1 = """
SELECT o.order_id, c.name, c.city, o.order_date, o.total_amount
FROM orders o
JOIN customers c ON c.customer_id=o.customer_id
WHERE o.status='completed'
ORDER BY o.order_date;
"""

cur.execute(query1)

rows = cur.fetchall()

for row in rows:
    print(row)


print("\n===== EXERCISE 15: JOIN PRODUCTS TO CATEGORIES =====")

query2 = """
SELECT p.product_id, p.product_name, c.category_name, p.unit_price
FROM products p
JOIN categories c ON c.category_id=p.category_id
ORDER BY c.category_name, p.product_name;
"""

cur.execute(query2)

rows = cur.fetchall()

for row in rows:
    print(row)




print("\n===== EXERCISE 16: JOIN ORDER LINE ITEMS =====")

query3 = """
SELECT o.order_id, c.name AS customer_name, p.product_name,
       oi.quantity, oi.unit_price, oi.line_total
FROM orders o
JOIN customers c ON c.customer_id=o.customer_id
JOIN order_items oi ON oi.order_id=o.order_id
JOIN products p ON p.product_id=oi.product_id
WHERE o.status='completed'
ORDER BY o.order_id, oi.order_item_id;
"""

cur.execute(query3)

rows = cur.fetchall()

for row in rows:
    print(row)



print("\n===== EXERCISE 17: LEFT JOIN - CUSTOMERS WITH NO COMPLETED ORDERS =====")

query4 = """
SELECT c.customer_id, c.name,
       COUNT(o.order_id) AS completed_orders
FROM customers c
LEFT JOIN orders o
  ON o.customer_id=c.customer_id
 AND o.status='completed'
GROUP BY c.customer_id, c.name
ORDER BY completed_orders, c.name;
"""

cur.execute(query4)

rows = cur.fetchall()

for row in rows:
    print(row)



cur.close()
conn.close()

print("\nDatabase connection closed.")