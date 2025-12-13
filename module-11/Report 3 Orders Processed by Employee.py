import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Noor1998$$$$",
    database="team3_bacchus"
)

cursor = db.cursor()

query = """
SELECT CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
       COUNT(o.order_id) AS orders_processed
FROM Employee e
LEFT JOIN Orders o ON e.employee_id = o.employee_id
GROUP BY employee_name
ORDER BY orders_processed DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nORDERS PROCESSED BY EMPLOYEE")
print("------------------------------")
for row in results:
    print(row)

db.close()
