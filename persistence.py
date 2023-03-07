from sqlite3 import Connection
from devices import Device
from smarthouse import Room
from typing import Optional, List, Dict, Tuple
from datetime import date, datetime
import pandas as pd


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
            self.persistence.cursor.execute("SELECT value FROM measurements WHERE device ="+ str(sensor.device_id) +"ORDER BY time_stamp DESC LIMIT 1;")
            results = self.persistence.cursor.fetchall()
            for result in results:
                value = result
            return value 
        else : 
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
        return NotImplemented()

    def describe_temperature_in_rooms(self) -> Dict[str, Tuple[float, float, float]]:
        list_with_values = []
        self.persistence.cursor.execute("MIN(Value), MAX(Value), AVG(Value) from measurements "
                                        "WHERE device = 8 OR device = 12 OR device = 28"
                                        "GROUP by device")
        results = self.persistence.cursor.fetchall()
        for result in results:
            for value in results:
                list_with_values.append(value)
        dictionary_with_room_temp = {
            "Living Room / Kitchen": (list_with_values[3], list_with_values[4], list_with_values[5]),
            "Entrance": (list_with_values[0], list_with_values[1], list_with_values[2]),
            "Master Bedroom": (list_with_values[6], list_with_values[7], list_with_values[8])
        }
        return dictionary_with_room_temp


    def get_hours_when_humidity_above_average(self, room: Room, day: date) -> List[int]:
        """
        This function determines during which hours of the given day
        there were more than three measurements in that hour having a humidity measurement that is above
        the average recorded humidity in that room at that particular time.
        The result is a (possibly empty) list of number respresenting hours [0-23].
        """


        return NotImplemented()