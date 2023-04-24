import logging
import threading
import time
import math
import requests
import json 

from messaging import SensorMeasurement
import common


class Sensor:

    def __init__(self, did):
        self.did = did
        self.measurement = SensorMeasurement('0.0')

    def simulator(self):

        logging.info(f"Sensor {self.did} starting")

        while True:

            temp = round(math.sin(time.time() / 10) * common.TEMP_RANGE, 1)

            logging.info(f"Sensor {self.did}: {temp}")
            self.measurement.set_temperature(str(temp))

            time.sleep(common.TEMPERATURE_SENSOR_SIMULATOR_SLEEP_TIME)

    def client(self):
        logging.info(f"Sensor Client {self.did} starting")

        converter_str2json = json.dumps(self.measurement)
        http_link = "http://localhost:8000/smarthouse/device/{self.did}"
        
        requests.put(http_link, data=converter_str2json)
        
        logging.info(f"Client {self.did} finishing")

    def run(self):
    
        simulatorthread = threading.Thread(target=self.simulator)
        simulatorthread.start()

        clientThread = threading.Thread(target=self.client)
        clientThread.start()
    
        return simulatorthread, clientThread

