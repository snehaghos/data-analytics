import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sneha",
    database="ds_sql_practice",
    port=3307
)

print("Database connected successfully!")

cur = conn.cursor()

cur.execute("SHOW TABLES")

for table in cur:
    print(table)

cur.close()
conn.close()