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
def test():
    device_8 = []
    cursor.execute("SELECT value from measurements WHERE device = 8")
    results = cursor.fetchall()
    for result in results:
        device_8.append(result[0])
    s1 = pd.Series(device_8)
    print(s1.describe())

    device_12 = []
    cursor.execute("SELECT value from measurements WHERE device = 12")
    results = cursor.fetchall()
    for result in results:
        device_12.append(result[0])
    s2 = pd.Series(device_8)
    print(s2.describe())

    device_28 = []
    cursor.execute("SELECT value from measurements WHERE device = 28")
    results = cursor.fetchall()
    for result in results:
        device_28.append(result[0])
    s3 = pd.Series(device_8)
    print(s3.describe())

    dictionary = {
        "Room1": [s1.describe()[3], s1.describe()[7], s1.describe()[1]],
        "Room1": [s2.describe()[3], s2.describe()[7], s2.describe()[1]],
        "Room1": [s3.describe()[3], s3.describe()[7], s3.describe()[1]]
    }
    return dictionary