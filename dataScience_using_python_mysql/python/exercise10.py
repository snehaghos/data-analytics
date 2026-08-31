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



print("===== EXERCISE 25: RANK CUSTOMERS BY REVENUE =====")

query1 = """
WITH customer_revenue AS (
    SELECT customer_id, SUM(total_amount) AS revenue
    FROM orders
    WHERE status='completed'
    GROUP BY customer_id
)
SELECT c.name, ROUND(cr.revenue,2) AS revenue,
       DENSE_RANK() OVER (ORDER BY cr.revenue DESC) AS revenue_rank
FROM customer_revenue cr
JOIN customers c ON c.customer_id=cr.customer_id
ORDER BY revenue_rank;
"""

cur.execute(query1)

rows = cur.fetchall()

for row in rows:
    print(row)



print("\n===== EXERCISE 26: RUNNING MONTHLY REVENUE =====")

query2 = """
WITH monthly_sales AS (
    SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
           SUM(total_amount) AS revenue
    FROM orders
    WHERE status='completed'
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT month, ROUND(revenue,2) AS revenue,
       ROUND(SUM(revenue) OVER (ORDER BY month),2) AS cumulative_revenue
FROM monthly_sales
ORDER BY month;
"""

cur.execute(query2)

rows = cur.fetchall()

for row in rows:
    print(row)


print("\n===== EXERCISE 27: TOP PRODUCT PER CATEGORY =====")

query3 = """
WITH product_sales AS (
    SELECT p.product_id, p.product_name, p.category_id,
           SUM(oi.line_total) AS revenue
    FROM order_items oi
    JOIN orders o ON o.order_id=oi.order_id
    JOIN products p ON p.product_id=oi.product_id
    WHERE o.status='completed'
    GROUP BY p.product_id, p.product_name, p.category_id
), ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY category_id ORDER BY revenue DESC) AS rn
    FROM product_sales
)
SELECT c.category_name, r.product_name, ROUND(r.revenue,2) AS revenue
FROM ranked r
JOIN categories c ON c.category_id=r.category_id
WHERE r.rn=1
ORDER BY c.category_name;
"""

cur.execute(query3)

rows = cur.fetchall()

for row in rows:
    print(row)



cur.close()
conn.close()

print("\nDatabase connection closed.")