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



print("===== EXERCISE 9: OVERALL BUSINESS SUMMARY =====")

query1 = """
SELECT COUNT(*) AS order_count,
       ROUND(SUM(total_amount),2) AS revenue,
       ROUND(AVG(total_amount),2) AS avg_order_value,
       ROUND(MIN(total_amount),2) AS min_order,
       ROUND(MAX(total_amount),2) AS max_order
FROM orders
WHERE status='completed';
"""

cur.execute(query1)

summary = cur.fetchone()
print(summary)


print("\n===== EXERCISE 10: COUNT BY STATUS =====")

query2 = """
SELECT status,
       COUNT(*) AS order_count,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM orders), 2) AS pct_of_orders
FROM orders
GROUP BY status
ORDER BY order_count DESC;
"""

cur.execute(query2)

rows = cur.fetchall()

for row in rows:
    print(row)




print("\n===== EXERCISE 11: DAILY REVENUE =====")

query3 = """
SELECT order_date,
       COUNT(*) AS orders,
       ROUND(SUM(total_amount),2) AS revenue
FROM orders
WHERE status='completed'
GROUP BY order_date
ORDER BY order_date;
"""

cur.execute(query3)

rows = cur.fetchall()

for row in rows:
    print(row)




cur.close()
conn.close()

print("\nDatabase connection closed.")