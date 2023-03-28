# Install FastAPI framework
# pip3 install "fastapi[all]"
# https://fastapi.tiangolo.com/tutorial/

# uvicorn main:app --reload

import uvicorn
import random

from fastapi import FastAPI, Response, status
from fastapi.staticfiles import StaticFiles
from typing import Union

from demohouse import build_demo_house
from device import Device
from sensors import *
from actuators import *


app = FastAPI()

smart_house = build_demo_house()

# http://localhost:8000/welcome/index.html
app.mount("/welcome", StaticFiles(directory="static"), name="static")


# http://localhost:8000/
@app.get("/")
async def root():
    return {"message": "Welcome to SmartHouse Cloud REST API - Powered by FastAPI"}

@app.get("/smarthouse/")
async def GetSmarthouse():
    # Informasjon om smarthuset
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/floor")
async def GetSmarthousefloor():
    # Informasjon om alle etasjer
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/floor/{fid}")
async def GetSmarthousefloorid():
    # Informasjon om spesifikk etasje
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/floor/{fid}/room")
async def GetSmarthouserooms():
    # Informasjon om alle rom i en etasje
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/floor/{fid}/room/{rid}")
async def GetSmarthouseroom():
    # Informasjon om ett rom i en etasje
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/device")
async def Get_all_devices():
    list_with_all_devices = []
    for floor in smart_house.floors:
        for room in floor.rooms:
            list_with_all_devices.append(room.devices) 
    return json.dumps(str(list_with_all_devices))


@app.get("/smarthouse/device/{did}")
async def GetSmarthouseDeviceID(did : int, response: Response):
    for floor in smart_house.floors:
        for room in floor.rooms:
            for device in room.devices:
                if device.did == did:
                    return json.dumps(str(device))


@app.get("/smarthouse/sensor/{did}/current")
async def GetSmarthouseDeviceStatus(did : int, response: Response):
    for floor in smart_house.floors:
        for room in floor.rooms:
            for device in room.devices:
                if device.did == did and device.is_sensor():
                    return json.dumps(str(device.get_current_value())) 


@app.post("/smarthouse/sensor/{did}/current")
async def PostSmartHouseSensorCurrent(did : int):
    value = random.randint(0, 50)
    for floor in smart_house.floors:
        for room in floor.rooms:
            for device in room.devices:
                if device.did == did and device.is_sensor():
                    return json.dumps(str(device.set_current_value(value)))   


@app.get("/smarthouse/sensor/{did}/values")
async def Getlatestmeasurements(did : int, limit: int):
    # Siste måling(er) for spesifikk sensor - antall målinger returnert gitt av "n"
    # TODO Sjekk om endringer er nødvendig
    if 1 <= did <= 31:
        for floor in smart_house.floors:
            for room in floor.rooms:
                for device in room.devices:
                    if device.did == did and device.is_sensor():
                        if type(device) == TemperatureSensor:
                            result = device.temperature[-limit:]
                            return json.dumps(result)
                        elif type(device) == HumiditySensor:
                            result = device.humidity[-limit:]
                            return json.dumps(result)
                        elif type(device) == SmartMeter:
                            result = device.energy_consumption[-limit:]
                            return json.dumps(result)
                        elif type(device) == AirQualitySensor:
                            result = device.air_quality[-limit:]
                            return json.dumps(result)
                        else:
                            return json.dumps("Invalid sensor type")
                    elif device.did == did and device.is_actuator():
                        return json.dumps("Device is not a sensor.")
    else:
        return json.dumps("Invalid device ID")



@app.delete("/smarthouse/sensor/{did}/oldest")
async def Deleteoldestmeasurement(did : int):
    # Slett eldste måling fra gitt sensor
    # TODO sjekk om endringer er nødvendig
    if 1 <= did <= 31:
        for floor in smart_house.floors:
            for room in floor.rooms:
                for device in room.devices:
                    if device.did == did and device.is_sensor():
                        device.delete_oldest_value()
                        return json.dumps("Oldest measurement deleted for device " + str(device.did))
                    elif device.did == did and device.is_actuator():
                        return json.dumps("Device is not a sensor.")
    else:
        return json.dumps("Invalid device ID")



@app.get("/smarthouse/actuator/{did}/current")
async def Getactuatorstatus(did : int):
    # TODO sjekk om endringer er nødvendig
    # Hent status på aktuator
    if 1 <= did <= 31:
        for floor in smart_house.floors:
            for room in floor.rooms:
                for device in room.devices:
                    if device.did == did and device.is_actuator():
                        return json.dumps(str(device.get_current_state()))
                    elif device.did == did and device.is_sensor():
                        return json.dumps("Device is not an actuator.")
    else:
        return json.dumps("Invalid device ID")


@app.put("/smarthouse/device/{did}")
async def Updateactuator(did : int):
    # Oppdater status på aktuator
    # TODO sjekk om endringer er nødvendig
    if 1 <= did <= 31:
        for floor in smart_house.floors:
            for room in floor.rooms:
                for device in room.devices:
                    if device.did == did and device.is_actuator():
                        if type(device.get_current_state()) == bool:
                            if device.get_current_state() == True:
                                device.set_current_state(False)
                                return json.dumps("New state: " + str(device.get_current_state()))
                            elif device.get_current_state() == False:
                                device.set_current_state(True)
                                return json.dumps("New state: " + str(device.get_current_state()))
                        elif type(device.get_current_state()) == float:
                            device.set_current_state("20")
                            return json.dumps("Actuator updated. New value: " + str(device.get_current_state()))
                    elif device.did == did and device.is_sensor():
                        return json.dumps("Device is not an actuator.")
    else:
        return json.dumps("Invalid device ID")


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
