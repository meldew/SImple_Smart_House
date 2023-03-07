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
        list_device8 = []
        self.persistence.cursor.execute("SELECT value FROM measurements m WHERE device = 8")
        results = self.persistence.cursor.fetchall()
        for result in results:
            list_device8.append(result[0])
        s8 = pd.Series(list_device8)
        s8.describe()

        list_device12 = []
        self.persistence.cursor.execute("SELECT value FROM measurements m WHERE device = 12")
        results = self.persistence.cursor.fetchall()
        for result in results:
            list_device12.append(result[0])
        s12 = pd.Series(list_device12)
        s12.describe()

        list_device28 = []
        self.persistence.cursor.execute("SELECT value FROM measurements m WHERE device = 28")
        results = self.persistence.cursor.fetchall()
        for result in results:
            list_device28.append(result[0])
        s28 = pd.Series(list_device28)
        s28.describe()

        dict_devices = {
            "Room 8": [s8.describe()[3], s8.describe()[7], s8.describe()[1]],
            "Room 12": [s12.describe()[3], s12.describe()[7], s12.describe()[1]],
            "Room 24": [s28.describe()[3], s28.describe()[7], s28.describe()[1]]
        }

        return dict_devices


    def get_hours_when_humidity_above_average(self, room: Room, day: date) -> List[int]:
        """
        This function determines during which hours of the given day
        there were more than three measurements in that hour having a humidity measurement that is above
        the average recorded humidity in that room at that particular time.
        The result is a (possibly empty) list of number respresenting hours [0-23].
        """


        return NotImplemented()