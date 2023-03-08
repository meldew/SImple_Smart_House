import devices
from devices import *
from typing import List, Optional


class Room:
    def __init__(self, area: float, name: str = None, room_id: int = None):
        self.room_id = room_id
        self.area = area
        self.name = name
        self.list_of_devices_in_a_room = []
        

    def __repr__(self):
        return f"{self.name} ({self.area} m^2)"


class Floor:
    def __init__(self, floor_no: int):
        self.floor_no = floor_no
        self.rooms = []


class SmartHouse:
    def __init__(self):
        self.floors = []


    def create_floor(self) -> Floor:
        floornum = len(self.floors) + 1
        newfloor = Floor(floornum)
        self.floors.append(newfloor)
        return newfloor


    def create_room(self, room_id: int, floor_no: int, area: float, name: str = None) -> Room:
        newroom = Room(area, name, room_id)
        globals()[f'Rom{room_id}'] = newroom
        if floor_no == 1:
            self.floors[0].rooms.append(newroom)
        elif floor_no == 2:
            self.floors[1].rooms.append(newroom)
        elif floor_no == 3:
            self.floors[2].append(newroom)
        else:
            return NotImplemented

        return newroom


    def get_no_of_rooms(self) -> int:
        no_of_rooms = 0
        for floor in self.floors:
            no_of_rooms = no_of_rooms + len(floor.rooms)
        return no_of_rooms


    def get_all_devices(self) -> List[Device]:
        return devices.list_with_devices
    

    def get_all_rooms(self) -> List[Room]:
        roomlist = []
        for floor in self.floors:
            for room in floor.rooms:
                roomlist.append(room)
        return roomlist


    def get_total_area(self) -> float:
        total_area = 0
        for floor in self.floors:
            for room in floor.rooms:
                total_area = total_area + room.area
        return total_area


    def register_device(self, device: Device, room: Room):

        room.list_of_devices_in_a_room.append(device)


    def get_no_of_devices(self):        
        return len(list_with_devices)


    def get_no_of_sensors(self):  
        return len(list_with_sensors) 
    

    def get_no_of_actuators(self): 
        return len(list_with_aktuators)


    def move_device(self, device: Device, from_room: Room, to_room: Room): 
        from_room.list_of_devices_in_a_room.remove(device)
        to_room.list_of_devices_in_a_room.append(device)


    def find_device_by_serial_no(self, serial_no: str) -> Optional[Device]:
        for device in list_with_devices:
            if device.serienummer == serial_no:
                return device   


    def get_room_with_device(self, device: Device):
        for floor in self.floors:
            for room in floor.rooms:
                for device_obj in room.list_of_devices_in_a_room:
                    if device_obj == device:
                        return room


    def get_all_devices_in_room(self, room: Room) -> List[Device]:
        return room.list_of_devices_in_a_room


    def turn_on_lights_in_room(self, room: Room):
        for device_obj in room.list_of_devices_in_a_room:
            if type(device_obj) == Smartlys:
                device_obj.verdi = True
       

    def turn_off_lights_in_room(self, room: Room):
        for device_obj in room.list_of_devices_in_a_room:
            if type(device_obj) == Smartlys:
                device_obj.verdi = False
        

    def get_temperature_in_room(self, room: Room) -> Optional[float]:
        for device_obj in room.list_of_devices_in_a_room:
            if type(device_obj) == TemperaturSensor:
                return device_obj.verdi
        

    def set_temperature_in_room(self, room: Room, temperature: float):
        for device_obj in room.list_of_devices_in_a_room:
            if type(device_obj) == Varmepumpe:
                device_obj.temp = temperature
            elif type(device_obj) == Paneloven:
                device_obj.temp = temperature
            elif type(device_obj) == Gulvvarmepanel:
                device_obj.temp = temperature

