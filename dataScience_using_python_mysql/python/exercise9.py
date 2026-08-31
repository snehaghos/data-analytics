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



print("===== EXERCISE 23: MONTHLY REVENUE TREND =====")

query1 = """
WITH monthly_sales AS (
    SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
           SUM(total_amount) AS revenue
    FROM orders
    WHERE status='completed'
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT month, ROUND(revenue,2) AS revenue
FROM monthly_sales
ORDER BY revenue DESC;
"""

cur.execute(query1)

rows = cur.fetchall()

for row in rows:
    print(row)


print("\n===== EXERCISE 24: TOP 5 CUSTOMERS BY REVENUE =====")

query2 = """
WITH customer_revenue AS (
    SELECT customer_id, SUM(total_amount) AS revenue
    FROM orders
    WHERE status='completed'
    GROUP BY customer_id
)
SELECT c.name, ROUND(cr.revenue,2) AS revenue
FROM customer_revenue cr
JOIN customers c ON c.customer_id=cr.customer_id
ORDER BY cr.revenue DESC
LIMIT 5;
"""

cur.execute(query2)

rows = cur.fetchall()

for row in rows:
    print(row)



cur.close()
conn.close()

print("\nDatabase connection closed.")