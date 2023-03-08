from sqlite3 import Connection
conn = Connection("db.sqlite")
cursor = conn.cursor()

list_with_values = []
cursor.execute("""SELECT MAX(value), AVG(value), MIN(value) from measurements 
WHERE device = 8 OR device = 12 OR device = 28
GROUP by device
""")
results = cursor.fetchall()
for result in results:
  for x in result: 
    list_with_values.append(x)
print(list_with_values)
dictionary = {
    "Living Room / Kitchen": [list_with_values[5],list_with_values[3], list_with_values[4]],
    "Entrance": [list_with_values[2],list_with_values[0], list_with_values[1]],
    "Master Bedroom": [list_with_values[8],list_with_values[6], list_with_values[7]]
}
