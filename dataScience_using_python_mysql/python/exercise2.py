import mysql.connector

# Connect to MariaDB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="ds_sql_practice",
    port=3307
)

print("Database connected successfully!")

# Create cursor
cur = conn.cursor(dictionary=True)

query = """
SELECT product_id, product_name, unit_price
FROM products
WHERE unit_price BETWEEN 700 AND 2000
ORDER BY unit_price;
"""


cur.execute(query)

rows = cur.fetchall()


for row in rows:
    print(row)


cur.close()
conn.close()