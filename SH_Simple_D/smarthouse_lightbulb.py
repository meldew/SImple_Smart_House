import logging
import threading
import time
import requests

from messaging import ActuatorState
import common


class Actuator:

    def __init__(self, did):
        self.did = did
        self.state = ActuatorState('False')

    def simulator(self):

        logging.info(f"Actuator {self.did} starting")

        while True:

            logging.info(f"Actuator {self.did}: {self.state.state}")

            time.sleep(common.LIGHTBULB_SIMULATOR_SLEEP_TIME)

    def client(self):

        logging.info(f"Actuator Client {self.did} starting")

        loop = True
        while loop:
            request = requests.get("http://localhost:8000/smarthouse/actuator/1/current")
            value = request.json()
            self.state = ActuatorState(value)
            time.sleep(1)
        # send request to cloud service with regular intervals and
        # set state of actuator according to the received response

        logging.info(f"Client {self.did} finishing")

    def run(self):

        simulatorthread = threading.Thread(target=self.simulator)
        simulatorthread.start()

        clientThread = threading.Thread(target=self.client)
        clientThread.start()

        return simulatorthread, clientThread

