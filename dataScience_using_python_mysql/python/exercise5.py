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


print("===== EXERCISE 12: REVENUE BY CUSTOMER CITY =====")

query1 = """
SELECT c.city,
       COUNT(o.order_id) AS order_count,
       ROUND(SUM(o.total_amount),2) AS revenue
FROM customers c
JOIN orders o ON o.customer_id=c.customer_id
WHERE o.status='completed'
GROUP BY c.city
ORDER BY revenue DESC;
"""

cur.execute(query1)

rows = cur.fetchall()

for row in rows:
    print(row)



print("\n===== EXERCISE 13: CUSTOMERS WITH MANY COMPLETED ORDERS =====")

query2 = """
SELECT c.customer_id, c.name,
       COUNT(o.order_id) AS completed_orders
FROM customers c
JOIN orders o ON o.customer_id=c.customer_id
WHERE o.status='completed'
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) >= 3
ORDER BY completed_orders DESC;
"""

cur.execute(query2)

rows = cur.fetchall()

for row in rows:
    print(row)



cur.close()
conn.close()

print("\nDatabase connection closed.")