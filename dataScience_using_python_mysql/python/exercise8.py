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



print("===== EXERCISE 21: ORDERS ABOVE THE AVERAGE =====")

query1 = """
SELECT order_id, customer_id, total_amount
FROM orders
WHERE status='completed'
  AND total_amount > (
      SELECT AVG(total_amount)
      FROM orders
      WHERE status='completed'
  )
ORDER BY total_amount DESC;
"""

cur.execute(query1)

rows = cur.fetchall()

for row in rows:
    print(row)



print("\n===== EXERCISE 22: CUSTOMERS ABOVE AVERAGE LIFETIME REVENUE =====")

query2 = """
WITH customer_revenue AS (
    SELECT customer_id, SUM(total_amount) AS revenue
    FROM orders
    WHERE status='completed'
    GROUP BY customer_id
)
SELECT c.customer_id, c.name, cr.revenue
FROM customer_revenue cr
JOIN customers c ON c.customer_id=cr.customer_id
WHERE cr.revenue > (SELECT AVG(revenue) FROM customer_revenue)
ORDER BY cr.revenue DESC;
"""

cur.execute(query2)

rows = cur.fetchall()

for row in rows:
    print(row)



cur.close()
conn.close()

print("\nDatabase connection closed.")