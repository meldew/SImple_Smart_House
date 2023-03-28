# Install FastAPI framework
# pip3 install "fastapi[all]"
# https://fastapi.tiangolo.com/tutorial/

# uvicorn main:app --reload

import uvicorn

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
    for floor in smart_house.floors:
        for room in floor.rooms:
            for device in room.devices:
                if device.did == did and device.is_sensor():
                    return json.dumps(str(device.set_current_value(device.get_current_value())))   


@app.get("/smarthouse/sensor/{did}/values?limit=n")
async def Getlatestmeasurement():
    # Siste måling(er) for spesifikk sensor - antall målinger returnert gitt av "n"
    # TODO Legg inn funksjon
    return NotImplemented


@app.delete("/smarthouse/sensor/{did}/oldest")
async def Deleteoldestmeasurement():
    # Slett eldste måling fra gitt sensor
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/actuator/{did}/current")
async def Getactuatorstatus():
    # Hent status på aktuator
    # TODO Legg inn funksjon
    return NotImplemented


@app.put("/smarthouse/device/{did}")
async def Updateactuator():
    # Oppdater status på aktuator
    # TODO Legg inn funksjon
    return NotImplemented



if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
