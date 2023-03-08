from sqlite3 import Connection
from devices import Device
from smarthouse import Room
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
        """
        Returns a list of sensor measurements (float values) for the given device in the given timespan.
        """
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


    def get_hours_when_humidity_above_average(self, room: Room, day: date) -> List[int]:
        """
        This function determines during which hours of the given day
        there were more than three measurements in that hour having a humidity measurement that is above
        the average recorded humidity in that room at that particular time.
        The result is a (possibly empty) list of number respresenting hours [0-23].
        """

        self.persistence.cursor.execute("Select avg(value) from measurements where device = 3 OR device = 21;")
        Avghum = int(self.persistence.cursor.fetchone()[0])
        listofhours = []
        hours = ['T00', 'T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09', 'T10', 'T11', 'T12', 'T13',
                 'T14', 'T15', 'T16', 'T18', 'T19', 'T20', 'T21', 'T22', 'T23']
        i = 0
        for hour in hours:
            self.persistence.cursor.execute("SELECT * "
                                            "FROM measurements "
                                            "WHERE time_stamp "
                                            "LIKE '%" + hour +
                                            "%' AND device = 21 "
                                            "AND value > " + str(58.55) + ";")
            measurelist = self.persistence.cursor.fetchall()
            if len(measurelist) >= 3:
                newhour = i
                listofhours.append(newhour)
            i = i+1
        return listofhours
