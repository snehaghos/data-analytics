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


# Example 1: Calculate price with tax

print("===== PRICE WITH TAX =====")

query1 = """
SELECT product_name,
       unit_price,
       ROUND(unit_price * 1.18, 2) AS price_with_tax
FROM products;
"""

cur.execute(query1)

rows = cur.fetchall()

for row in rows:
    print(row)


# Example 2: Categorize orders using CASE


print("\n===== ORDER SEGMENT =====")

query2 = """
SELECT order_id,
       total_amount,
       CASE
           WHEN total_amount >= 3000 THEN 'High Value'
           WHEN total_amount >= 1500 THEN 'Medium Value'
           ELSE 'Low Value'
       END AS order_segment
FROM orders;
"""

cur.execute(query2)

rows = cur.fetchall()

for row in rows:
    print(row)


# Exercise: Create order value bands


print("\n===== ORDER VALUE BANDS =====")

query3 = """
SELECT order_id,
       total_amount,
       CASE
           WHEN total_amount >= 3000 THEN 'High'
           WHEN total_amount >= 1500 THEN 'Medium'
           ELSE 'Low'
       END AS value_band
FROM orders
ORDER BY total_amount DESC;
"""

cur.execute(query3)

rows = cur.fetchall()

for row in rows:
    print(row)


# Exercise: Extract year and month


print("\n===== YEAR AND MONTH =====")

query4 = """
SELECT order_id,
       order_date,
       YEAR(order_date) AS order_year,
       MONTH(order_date) AS month_number,
       DATE_FORMAT(order_date, '%Y-%m') AS order_month
FROM orders
ORDER BY order_date;
"""

cur.execute(query4)

rows = cur.fetchall()

for row in rows:
    print(row)


# Exercise: Clean text


print("\n===== CLEAN TEXT =====")

query5 = """
SELECT customer_id,
       UPPER(name) AS customer_name_upper,
       LOWER(email) AS email_lower
FROM customers;
"""

cur.execute(query5)

rows = cur.fetchall()

for row in rows:
    print(row)


# Close connection

cur.close()
conn.close()

print("\nDatabase connection closed.")