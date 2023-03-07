import pandas as pd
from sqlite3 import Connection
conn = Connection("db.sqlite")
cursor = conn.cursor()
# cursor.execute("SELECT device, AVG(value) AS avg_temp FROM measurements WHERE device IN (8, 12 ,28) GROUP BY device ORDER BY avg_temp ASC LIMIT 1;")
# results = cursor.fetchall()
# for result in results:
#     sensor_id = result
# cursor.execute("SELECT name FROM rooms WHERE id = (SELECT room FROM devices WHERE id ="+ str(sensor_id[0])+");")
# results = cursor.fetchall()
# for result in results:
#     room_name = result

list_with_values = []
cursor.execute("SELECT value from measurements WHERE device = 8")
results = cursor.fetchall()
for result in results:
    list_with_values.append(result[0])

s = pd.Series(list_with_values)
print(s.describe())
