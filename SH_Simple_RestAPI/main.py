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
def root():
    return {"message": "Welcome to SmartHouse Cloud REST API - Powered by FastAPI"}

@app.get("/smarthouse/")
def GetSmarthouse():
    # Informasjon om smarthuset
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/floor")
def GetSmarthousefloor():
    # Informasjon om alle etasjer
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/floor/{fid}")
def GetSmarthousefloorid():
    # Informasjon om spesifikk etasje
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/floor/{fid}/room")
def GetSmarthouserooms():
    # Informasjon om alle rom i en etasje
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/floor/{fid}/room/{rid}")
def GetSmarthouseroom():
    # Informasjon om ett rom i en etasje
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/device")
def GetSmarthouseDevices():
    # Informasjon om alle enheter
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/device/{did}")
def GetSmarthouseDeviceID():
    # Informasjon om spesifikk enhet
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/sensor/{did}/current")
def GetSmarthouseDeviceStatus():
    # Status på sensor (avgitt måleverdi)
    # TODO Legg inn funksjon
    return NotImplemented


@app.post("/smarthouse/sensor/{did}/current")
def PostSmartHouseSensorCurrent():
    # Legg til måling for spesifisert enhet
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/sensor/{did}/values?limit=n")
def Getlatestmeasurement():
    # Siste måling(er) for spesifikk sensor - antall målinger returnert gitt av "n"
    # TODO Legg inn funksjon
    return NotImplemented


@app.delete("/smarthouse/sensor/{did}/oldest")
def Deleteoldestmeasurement():
    # Slett eldste måling fra gitt sensor
    # TODO Legg inn funksjon
    return NotImplemented


@app.get("/smarthouse/actuator/{did}/current")
def Getactuatorstatus():
    # Hent status på aktuator
    # TODO Legg inn funksjon
    return NotImplemented


@app.put("/smarthouse/device/{did}")
def Updateactuator():
    # Oppdater status på aktuator
    # TODO Legg inn funksjon
    return NotImplemented



if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)