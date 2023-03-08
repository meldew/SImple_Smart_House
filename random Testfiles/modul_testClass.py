
list_with_devices = []
list_with_sensors = []
list_with_aktuators = []

class Room:
    """Representerer et rom i en etasje i ett hus.
        Et rom har et areal og det kan gis et kort navn.
        På et romm kan også registreres smarte enheter."""

    def __init__(self, area: float, name: str = None):
        self.area = area
        self.name = name

    def __repr__(self):
        return f"{self.name} ({self.area} m^2)"



class Device:
    def add_to_list(self, obj):
        list_with_devices.append(obj)

    def Create_actuator(self):
        Sensorer() 
    def Create_(self):
        Sensorer()            


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
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Fuktighetssensor")
        momGay = None
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi 
        self.produsent = produsent
        list_with_sensors.append(self)

    def __repr__(self):
        return f'Sensor ({self.__serienummerInternal}) Type: Fuktighetssensor STATUS: {self.verdi} % PRODUCT DETAILS: {self.produsent} {self.produktnavn}'    


class TemperaturSensor(Sensorer):
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Temperatursensor")
        self.__serienummerInternal = serienummer
        self.hovedType = "Sensor"
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_sensors.append(self)

    def __repr__(self):
        return f'Sensor ({self.__serienummerInternal}) Type: Temperatursensor STATUS: {self.verdi} °C PRODUCT DETAILS: {self.produsent} {self.produktnavn}'


class Strømmåler(Sensorer):
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Strømmåler")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_sensors.append(self)

    def __repr__(self):
        return f'Sensor ({self.__serienummerInternal}) Type: Strømmåler STATUS: {self.verdi} mA PRODUCT DETAILS: {self.produsent} {self.produktnavn}'


class Luftkvalitet(Sensorer):
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Luftkvalitetssensor")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_sensors.append(self)

    def __repr__(self):
        return f'Sensor ({self.__serienummerInternal}) Type: Luftkvalitetssensor STATUS: {self.verdi} g/m^2 PRODUCT DETAILS: {self.produsent} {self.produktnavn}'


class Varmepumpe(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Varmepumpe")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        self.state = Varmepumpe.On_OFF_state(self)
        list_with_aktuators.append(self)

    def On_OFF_state(self) -> str:
        if self.verdi  == True:
            return 'ON'
        else : 
            return 'OFF'
    
    def __repr__(self):
        return f'Aktuator ({self.__serienummerInternal}) Type: Varmepumpe STATUS: {self.state} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'


class Smartlys(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Smart Lys")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_aktuators.append(self)

    def __repr__(self):
        return f'Aktuator ({self.__serienummerInternal}) Type: Smart Lys STATUS: {"OFF" if self.verdi == False else "ON"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'


class Paneloven(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Paneloven")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        self.state = Paneloven.On_OFF_state(self)
        list_with_aktuators.append(self)

    def On_OFF_state(self) -> str:
        if self.verdi  == True:
            return 'ON'
        else : 
            return 'OFF'
    
    def __repr__(self):
        return f'Aktuator ({self.__serienummerInternal}) Type: Paneloven STATUS: {self.state} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'


class Gulvvarmepanel(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Gulvvarmepanel")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        self.state = Gulvvarmepanel.On_OFF_state(self)
        list_with_aktuators.append(self)

    def On_OFF_state(self) -> str:
        if self.verdi  == True:
            return 'ON'
        else : 
            return 'OFF'
    
    def __repr__(self):
        return f'Aktuator ({self.__serienummerInternal}) Type: Gulvvarmepanel STATUS: {self.state} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'


class Smart_Stikkontakt(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Smart Stikkontakt")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        self.state = Smart_Stikkontakt.On_OFF_state(self)
        list_with_aktuators.append(self)

    def On_OFF_state(self) -> str:
        if self.verdi  == True:
            return 'ON'
        else : 
            return 'OFF'
    
    def __repr__(self):
        return f'Aktuator ({self.__serienummerInternal}) Type: Smart Stikkontakt STATUS: {self.state} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Billader(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Billader")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        self.state = Billader.On_OFF_state(self)
        list_with_aktuators.append(self)

    def On_OFF_state(self) -> str:
        if self.verdi  == True:
            return 'ON'
        else : 
            return 'OFF'
    
    def __repr__(self):
        return f'Aktuator ({self.__serienummerInternal}) Type: Billader STATUS: {self.state} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'


test = TemperaturSensor(1.3,"Moen Inc","Prodder Ute 1.2","e237beec-2675-4cb0")




def bla (sensor: Device):
    me = sensor.hovedType
    return me

print(bla(test))


