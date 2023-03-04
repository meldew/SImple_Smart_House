from sqlite3 import Connection
conn = Connection("db.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT * FROM devices where id < 2")
results = cursor.fetchall()
for result in results:
    print(result)
cursor.close()