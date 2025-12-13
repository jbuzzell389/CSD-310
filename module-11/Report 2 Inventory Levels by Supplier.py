import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Noor1998$$$$",
    database="team3_bacchus"
)

cursor = db.cursor()

query = """
SELECT s.supplier_name,
       i.item_name,
       i.quantity,      -- FIXED COLUMN NAME
       i.unit_price
FROM Inventory i
JOIN Supplier s ON i.supplier_id = s.supplier_id
ORDER BY s.supplier_name;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nINVENTORY LEVELS BY SUPPLIER")
print("-----------------------------")
for row in results:
    print(row)

db.close()

