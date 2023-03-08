from sqlite3 import Connection
from devices import Device
from smarthouse import Room, SmartHouse
from typing import Optional, List, Dict, Tuple
from datetime import date, datetime


class SmartHousePersistence:

    def __init__(self, db_file: str):
        self.db_file = db_file
        self.connection = Connection(db_file)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.rollback()
        self.connection.close()

    def save(self):
        self.connection.commit()

    def reconnect(self):
        self.connection.close()
        self.connection = Connection(self.db_file)
        self.cursor = self.connection.cursor()

    def check_tables(self) -> bool:
        self.cursor.execute("SELECT name FROM sqlite_schema WHERE type = 'table';")
        result = set()
        for row in self.cursor.fetchall():
            result.add(row[0])
        return 'rooms' in result and 'devices' in result and 'measurements' in result


class SmartHouseAnalytics:

    def __init__(self, persistence: SmartHousePersistence):
        self.persistence = persistence


    def get_most_recent_sensor_reading(self, sensor: Device) -> Optional[float]:
        if sensor.hovedType == "Sensor":
            self.persistence.cursor.execute("SELECT value FROM measurements WHERE device ="+ str(sensor.device_id) +" ORDER BY time_stamp DESC LIMIT 1;")
            results = self.persistence.cursor.fetchone()
            for result in results:
                value = result
            return value 
        else:
            return None
        
    def get_coldest_room(self) -> Room:
        self.persistence.cursor.execute("SELECT device, AVG(value) AS avg_temp FROM measurements WHERE device IN (8, 12 ,28) GROUP BY device ORDER BY avg_temp ASC LIMIT 1;")
        results = self.persistence.cursor.fetchall()
        for result in results:
            sensor_id = result
        self.persistence.cursor.execute("SELECT name FROM rooms WHERE id = (SELECT room FROM devices WHERE id ="+ str(sensor_id[0])+");")
        results = self.persistence.cursor.fetchall()
        for result in results:
            room_name = result
        return room_name[0]
        
    def get_sensor_readings_in_timespan(self, sensor: Device, from_ts: datetime, to_ts: datetime) -> List[float]:
        sen_id = sensor.device_id
        From = from_ts.isoformat()
        To = to_ts.isoformat()
        self.persistence.cursor.execute(
            "SELECT value FROM measurements WHERE device = "+str(sen_id)+" AND time_stamp BETWEEN '" + str(From) + "' AND '" + str(To) + "';")

        results = self.persistence.cursor.fetchall()
        resultlist = []
        for value in results:
            resultlist.append(value[0])
        return resultlist

    def describe_temperature_in_rooms(self) -> Dict[str, Tuple[float, float, float]]:
        list_with_values = []
        self.persistence.cursor.execute("SELECT MIN(Value), MAX(Value), AVG(Value) from measurements "
                                        "WHERE device = 8 OR device = 12 OR device = 28 "
                                        "GROUP by device")
        results = self.persistence.cursor.fetchall()
        for result in results:
            for value in results:
                list_with_values.append(value)
        dictionary_with_room_temp = {
            "Living Room / Kitchen": (list_with_values[1]),
            "Entrance": (list_with_values[0]),
            "Master Bedroom": (list_with_values[2])
        }
        return dictionary_with_room_temp


    def get_hours_when_humidity_above_average(self, room: str, day: date) -> List[int]:    
        bathroom1 = "Bathroom 1"
        bathroom2 = "Bathroom 2"
        if room == bathroom1:
            device_id = 3
        elif room == bathroom2:
            device_id = 21
                      
        newdate = day
        timedate = newdate.strftime("%Y-%m-%d")
        self.persistence.cursor.execute("Select avg(value) "
                                        "FROM measurements "
                                        "WHERE device =" + str(device_id) + " "
                                        "AND time_stamp LIKE '" + timedate + "%';")
        avgpre = self.persistence.cursor.fetchone()
        avghum = avgpre[0]

        listofhours = []
        hours = ['T00', 'T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09', 'T10', 'T11', 'T12', 'T13',
                 'T14', 'T15', 'T16', 'T18', 'T19', 'T20', 'T21', 'T22', 'T23']
        i = 0
        for hour in hours:
            self.persistence.cursor.execute("SELECT * "
                                            "FROM measurements "
                                            "WHERE time_stamp "
                                            "LIKE '%" + hour + "%' "
                                            "AND time_stamp LIKE '" + timedate + "%' " 
                                            "AND device = " + str(device_id) + " "
                                            "AND value > " + str(avghum) + ";")
            measurelist = self.persistence.cursor.fetchall()
            if len(measurelist) > 3:
                listofhours.append(i)
            i = i+1
        return listofhours
