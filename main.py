from smarthouse import SmartHouse
from devices import *


def build_demo_house() -> SmartHouse:
    house = SmartHouse()
    Floor1 = house.create_floor()
    Floor2 = house.create_floor()
    LivRoom = house.create_room(1, 39.75, "Living Room / Kitchen")
    Bath1 = house.create_room(1, 6.3, "Bathroom 1")
    Guest1 = house.create_room(1, 8.0, "Guest Room 1")
    Entrance = house.create_room(1, 13.5, "Entrance")
    Garage = house.create_room(1, 19, "Garage")
    Outside = house.create_room(1, 0, "Outside")
    Office = house.create_room(2, 11.75, "Office")
    Bath2 = house.create_room(2, 9.25, "Bathroom 2")
    Guest2 = house.create_room(2, 8, "Guest Room 2")
    Gang = house.create_room(2, 10, "Gang")
    Guest3 = house.create_room(2, 10, "Guest Room 3")
    DressRoom = house.create_room(2, 4, "Dressing Room")
    MasterBed = house.create_room(2, 17, "Master Bedroom")
    
    house.register_device(Smartlys(False,"Fritsch Group","Tresom Bright 1.0","f11bb4fc-ba74-49cd"), LivRoom)
    house.register_device(Smartlys(False,"Fritsch Group","Alphazap 2","480dbae8-cce7-46d7"), LivRoom)
    house.register_device(Fuktighetssensor(68,"Bernhard-Roberts","Andalax","4cb686fe-6448-4cf6"), Bath1)
    house.register_device(Smartlys(False,"Fritsch Group","Alphazap 2","6a36c71d-4f48-4eb4"), Guest1)
    house.register_device(Smartlys(False,"Larkin-Nitzsche","Quo Lux","d01130c9-a368-42c6"), Garage)
    house.register_device(Billader(False,"Jast, Hansen and Halvorson","Charge It 9000","0cae4f01-4ad9-47aa"), Garage)
    house.register_device(Paneloven(False,"Hauck-DuBuque","Voyatouch 42","d16d84de-79f1-4f9a"), Guest1)
    house.register_device(TemperaturSensor(1.3,"Moen Inc","Prodder Ute 1.2","e237beec-2675-4cb0"), Outside)
    house.register_device(Smartlys(False,"Fritsch Group","Alphazap 2","f4db4e54-cebe-428d"), Entrance)
    house.register_device(Smartlys(False,"Larkin-Nitzsche","Quo Vadis Lux","8d09aa92-fc58-4c6"), Outside)
    house.register_device(Strømmåler(0,"Kilback LLC","Transcof Current","c8bb5601-e850-4a80"), LivRoom)
    house.register_device(TemperaturSensor(18.1,"Moen Inc","Prodder Inne 2.3","d16d84de-79f1-4f9a"), LivRoom)
    house.register_device(Smartlys(False,"Fritsch Group","Alphazap 2","390ae474-21fb-4e06"), Entrance)
    house.register_device(Strømmåler(1.5,"Ward-Schaefer","Zaam-Dox NetConnect","3b06cf0f-8494-458b"), Entrance)
    house.register_device(Smart_Stikkontakt(False,"Kilback LLC","Konklab 3","c28b6e75-d565-4678"), LivRoom)
    house.register_device(Varmepumpe(False,"Osinski Inc","Fintone XCX4AB","4eca6387-0767-4e4e"), LivRoom)
    house.register_device(Luftkvalitet(0.08,"Hauck-DuBuque","Sonair Pro","c76688cc-3692-4aa3"), LivRoom)
    house.register_device(Smart_Stikkontakt(False,"Kilback LLC","Konklab 3","4b9050f3-0ef0-4914"), LivRoom)
    house.register_device(Paneloven(False,"Hauck-DuBuque","Voyatouch 42","66373954-2ddd-4807"), Office)
    house.register_device(Smart_Stikkontakt(False,"Kilback LLC","Konklab 3","1b34f6ce-94cb-4f7b"), Office)
    house.register_device(Fuktighetssensor(52,"Bernhard-Roberts","Namfix Y","8ceb53b2-e88f-4e8c"), Bath2)
    house.register_device(Luftkvalitet(0.08,"Steuber-Gerlach","Aerified 42","ae902f8f-10b4-4738"), Bath2)
    house.register_device(Gulvvarmepanel(False,"Steuber-Gerlach","Temp Opp Pro 13","42f204bf-9944-47a1"), Bath2)
    house.register_device(Paneloven(False,"Hauck-DuBuque","Otcom 2","73902f8f-10b4-4738"), Guest2)
    house.register_device(Smartlys(False,"Fritsch Group","Alphazap 2","627ff5f3-f4f5-47bd"), MasterBed)
    house.register_device(Smartlys(False,"Fritsch Group","Alphazap 2","ebaaadce-2d6b-4623"), MasterBed)
    house.register_device(Varmepumpe(False,"Osinski Inc","Fintone XCX2FF","eed2cba8-eb13-4023"), MasterBed)
    house.register_device(TemperaturSensor(16.1,"Moen Inc","Prodder Inne 2.3","481e94bd-ff50-40ea"), MasterBed)
    house.register_device(Smartlys(False,"Fritsch Group","Tresom Bright 1.0","233064d7-028a-407f"), MasterBed)
    house.register_device(Smartlys(False,"Fritsch Group","Alphazap 2","89393440-43cb-4cb5"), DressRoom)
    house.register_device(Paneloven(False,"Hauck-DuBuque","Otcom 2","be490f21-b9cf-4413"), Guest3)
    return house


def do_device_list(smart_house: SmartHouse):
    print("Listing Devices...")
    idx = 0
    for d in smart_house.get_all_devices():
        print(f"{idx}: {d}")
        idx += 1


def do_room_list(smart_house: SmartHouse):
    print("Listing Rooms...")
    idx = 0
    for r in smart_house.get_all_rooms():
        print(f"{idx}: {r}")
        idx += 1


def do_find(smart_house: SmartHouse):
    print("Please enter serial no: ")
    serial_no = input()
    device = smart_house.find_device_by_serial_no(serial_no)
    if device:
        devices = smart_house.get_all_devices()
        rooms = smart_house.get_all_rooms()
        room = smart_house.get_room_with_device(device)
        device_idx = devices.index(device)
        room_idx = rooms.index(room)
        print(f"Device No {device_idx}:")
        print(device)
        print(f"is located in room No {room_idx}:")
        print(room)
    else:
        print(f"Could not locate device with serial no {serial_no}")


def do_move(smart_house):
    devices = smart_house.get_all_devices()
    rooms = smart_house.get_all_rooms()
    print("Please choose device:")
    device_id = input()
    device = None
    if device_id.isdigit():
        device = devices[int(device_id)]
    else:
        device = smart_house.find_device_by_serial_no(device_id)
    if device:
        print("Please choose target room")
        room_id = input()
        if room_id.isdigit() and rooms[int(room_id)]:
            to_room = rooms[int(room_id)]
            from_room = smart_house.get_room_with_device(device)
            smart_house.move_device(device, from_room, to_room)
        else:
            print(f"Room with no {room_id} does not exist!")
    else:
        print(f"Device wit id '{device_id}' does not exist")


def main(smart_house: SmartHouse):
    print("************ Smart House Control *****************")
    print(f"No of Rooms:       {smart_house.get_no_of_rooms()}")
    print(f"Total Area:        {smart_house.get_total_area()}")
    print(f"Connected Devices: {smart_house.get_no_of_devices()} ({smart_house.get_no_of_sensors()} Sensors | {smart_house.get_no_of_actuators()} Actuators)")
    print("**************************************************")
    print()
    print("Management Interface v.0.1")
    while (True):
        print()
        print("Please select one of the following options:")
        print("- List all devices in the house (l)")
        print("- List all rooms in the house (r) ")
        print("- Find a device via its serial number (f)")
        print("- Move a device from one room to another (m)")
        print("- Quit (q)")
        char = input()
        if char == "l":
            do_device_list(smart_house)
        elif char == "r":
            do_room_list(smart_house)
        elif char == "f":
            do_find(smart_house)
        elif char == "m":
            do_move(smart_house)
        elif char == "q":
            break
        else:
            print(f"Error! Could not interpret input '{char}'!")


if __name__ == '__main__':
    house = build_demo_house()
    main(house)
