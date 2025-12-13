import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Noor1998$$$$",
    database="team3_bacchus"
)

cursor = db.cursor()

query = """
SELECT c.customer_name,
       SUM(oi.line_total) AS total_sales
FROM Customer c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Order_Items oi ON o.order_id = oi.order_id
GROUP BY c.customer_name
ORDER BY total_sales DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nTOTAL SALES BY CUSTOMER")
print("------------------------")
for row in results:
    print(row)

db.close()
