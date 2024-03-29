list_with_devices = []
list_with_sensors = []
list_with_aktuators = []
class Device:
    def add_to_list(self, obj):
        list_with_devices.append(obj)

class Sensorer(object):
    def __init__(self, serienummer, enhetstype):
        self.serienummer = serienummer
        self.enhetstype = enhetstype
        Device().add_to_list(self)

class Aktuatorer(object):
    def __init__(self, serienummer, enhetstype):
        self.serienummer = serienummer
        self.enhetstype = enhetstype
        Device().add_to_list(self)

class Fuktighetssensor(Sensorer):
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str,device_id:int):
        super().__init__(serienummer, "Fuktighetssensor")
        momGay = None
        self.device_id = device_id
        self.hovedType = "Sensor"
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_sensors.append(self)

    def __repr__(self):
        return f'Sensor({self.__serienummerInternal}) TYPE: Fuktighetssensor STATUS: {self.verdi} % PRODUCT DETAILS: {self.produsent} {self.produktnavn}'    

class TemperaturSensor(Sensorer):
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str,device_id:int):
        super().__init__(serienummer, "Temperatursensor")
        self.device_id = device_id
        self.hovedType = "Sensor"
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_sensors.append(self)

    def __repr__(self):
        return f'Sensor({self.__serienummerInternal}) TYPE: Temperatursensor STATUS: {self.verdi} °C PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Strømmåler(Sensorer):
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str,device_id:int):
        super().__init__(serienummer, "Strømmåler")
        self.device_id = device_id
        self.hovedType = "Sensor"
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_sensors.append(self)

    def __repr__(self):
        return f'Sensor({self.__serienummerInternal}) TYPE: Strømmåler STATUS: {self.verdi} kWh PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Luftkvalitet(Sensorer):
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str,device_id:int):
        super().__init__(serienummer, "Luftkvalitetssensor")
        self.device_id = device_id
        self.hovedType = "Sensor"
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_sensors.append(self)

    def __repr__(self):
        return f'Sensor({self.__serienummerInternal}) TYPE: Luftkvalitetssensor STATUS: {self.verdi} g/m^2 PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Varmepumpe(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str,device_id:int):
        super().__init__(serienummer, "Varmepumpe")
        self.device_id = device_id
        self.hovedType = "Aktuator"
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        self.temp = 0
        list_with_aktuators.append(self)
    
    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Varmepumpe STATUS: {("OFF" if self.verdi == False else "ON") if self.temp == 0 else str(self.temp) + " °C"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Smartlys(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str,device_id:int):
        super().__init__(serienummer, "Smart Lys")
        self.device_id = device_id
        self.hovedType = "Aktuator"
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_aktuators.append(self)

    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Smart Lys STATUS: {"OFF" if self.verdi == False else "ON"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Paneloven(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str,device_id:int):
        super().__init__(serienummer, "Paneloven")
        self.device_id = device_id
        self.hovedType = "Aktuator"
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        self.temp = 0
        list_with_aktuators.append(self)

    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Paneloven STATUS: {"OFF" if self.verdi == False else "ON"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Gulvvarmepanel(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str,device_id:int):
        super().__init__(serienummer, "Gulvvarmepanel")
        self.device_id = device_id
        self.hovedType = "Aktuator"
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        self.temp = 0
        list_with_aktuators.append(self)

    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Gulvvarmepanel STATUS: {"OFF" if self.verdi == False else "ON"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Smart_Stikkontakt(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str,device_id:int):
        super().__init__(serienummer, "Smart Stikkontakt")
        self.device_id = device_id
        self.hovedType = "Aktuator"
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_aktuators.append(self)

    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Smart Stikkontakt STATUS: {"OFF" if self.verdi == False else "ON"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Billader(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str,device_id:int):
        super().__init__(serienummer, "Billader")
        self.device_id = device_id
        self.hovedType = "Aktuator"
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_aktuators.append(self)

    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Billader STATUS: {"OFF" if self.verdi == False else "ON"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Luftavfukter(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str,device_id:int):
        super().__init__(serienummer, "Smart Stikkontakt")
        self.device_id = device_id
        self.hovedType = "Aktuator"
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_aktuators.append(self)

    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Luftavfukter STATUS: {"OFF" if self.verdi == False else "ON"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'
