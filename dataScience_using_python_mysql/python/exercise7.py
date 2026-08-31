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



print("===== EXERCISE 18: REVENUE BY PRODUCT =====")

query1 = """
SELECT p.product_id, p.product_name,
       SUM(oi.quantity) AS units_sold,
       ROUND(SUM(oi.line_total),2) AS revenue
FROM order_items oi
JOIN orders o ON o.order_id=oi.order_id
JOIN products p ON p.product_id=oi.product_id
WHERE o.status='completed'
GROUP BY p.product_id, p.product_name
ORDER BY revenue DESC;
"""

cur.execute(query1)

rows = cur.fetchall()

for row in rows:
    print(row)



print("\n===== EXERCISE 19: REVENUE BY CATEGORY =====")

query2 = """
SELECT c.category_name,
       SUM(oi.quantity) AS units_sold,
       ROUND(SUM(oi.line_total),2) AS revenue
FROM order_items oi
JOIN orders o ON o.order_id=oi.order_id
JOIN products p ON p.product_id=oi.product_id
JOIN categories c ON c.category_id=p.category_id
WHERE o.status='completed'
GROUP BY c.category_id, c.category_name
ORDER BY revenue DESC;
"""

cur.execute(query2)

rows = cur.fetchall()

for row in rows:
    print(row)



print("\n===== EXERCISE 20: CUSTOMER LIFETIME REVENUE =====")

query3 = """
SELECT c.customer_id, c.name,
       COUNT(o.order_id) AS order_count,
       ROUND(SUM(o.total_amount),2) AS lifetime_revenue,
       ROUND(AVG(o.total_amount),2) AS avg_order_value
FROM customers c
JOIN orders o ON o.customer_id=c.customer_id
WHERE o.status='completed'
GROUP BY c.customer_id, c.name
ORDER BY lifetime_revenue DESC;
"""

cur.execute(query3)

rows = cur.fetchall()

for row in rows:
    print(row)


cur.close()
conn.close()

print("\nDatabase connection closed.")