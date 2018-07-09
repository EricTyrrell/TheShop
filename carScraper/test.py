import sqlite3

connection = sqlite3.connect("cars.db")
#
# connection.execute('''CREATE TABLE CARS
#                         (ID INTEGER PRIMARY KEY,
#                         NAME                TEXT,
#                         POWER               TEXT,
#                         MAX_POWER_RPM       TEXT,
#                         TORQUE              TEXT,
#                         MAX_TORQUE_RPM    TEXT);''')
# connection.execute("DROP TABLE CARS;")
cursor = connection.execute("SELECT NAME,POWER,MAX_POWER_RPM,TORQUE,MAX_TORQUE_RPM from CARS")
for row in cursor:
    print(row)
# connection.execute("DELETE from CARS")
connection.commit()
connection.close()