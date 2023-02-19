#<Sensor eller Aktuator>(<serienummer) TYPE: <enhetstype> STATUS: <enhetsstatus> PRODUCT DETAILS: <produsent> <produktnavn>
#-------------------------------------------------------------------------------------------------------------------------
#Sensor(e237beec-2675-4cb0) TYPE: Temperatursensor STATUS: 3.2 °C PRODUCT DETAILS: Moen Inc Prodder Ute 1.2
#Aktuator(f11bb4fc-ba74-49cd) TYPE: Smart Lys STATUS: OFF PRODUCT DETAILS: Fritsch Group Tresom Bright 1.0
#Aktuator(eed2cba8-eb13-4023) TYPE: Varmepumpe STATUS: OFF PRODUCT DETAILS: Osinski Inc Fintone XCX2FF
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
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Fuktighetssensor")
        momGay = None
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_sensors.append(self)

    def __repr__(self):
        return f'Sensor({self.__serienummerInternal}) TYPE: Fuktighetssensor STATUS: {self.verdi} % PRODUCT DETAILS: {self.produsent} {self.produktnavn}'    

class TemperaturSensor(Sensorer):
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Temperatursensor")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_sensors.append(self)

    def __repr__(self):
        return f'Sensor({self.__serienummerInternal}) TYPE: Temperatursensor STATUS: {self.verdi} °C PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Strømmåler(Sensorer):
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Strømmåler")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_sensors.append(self)

    def __repr__(self):
        return f'Sensor({self.__serienummerInternal}) TYPE: Strømmåler STATUS: {self.verdi} kWh PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Luftkvalitet(Sensorer):
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Luftkvalitetssensor")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_sensors.append(self)

    def __repr__(self):
        return f'Sensor({self.__serienummerInternal}) TYPE: Luftkvalitetssensor STATUS: {self.verdi} g/m^2 PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Varmepumpe(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Varmepumpe")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        self.temp = 0
        list_with_aktuators.append(self)
    
    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Varmepumpe STATUS: {("OFF" if self.verdi == False else "ON") if self.temp == 0 else str(self.temp) + " °C"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Smartlys(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Smart Lys")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_aktuators.append(self)

    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Smart Lys STATUS: {"OFF" if self.verdi == False else "ON"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Paneloven(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Paneloven")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        self.temp = 0
        list_with_aktuators.append(self)

    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Paneloven STATUS: {"OFF" if self.verdi == False else "ON"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Gulvvarmepanel(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Gulvvarmepanel")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        self.temp = 0
        list_with_aktuators.append(self)

    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Gulvvarmepanel STATUS: {"OFF" if self.verdi == False else "ON"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Smart_Stikkontakt(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Smart Stikkontakt")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_aktuators.append(self)

    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Smart Stikkontakt STATUS: {"OFF" if self.verdi == False else "ON"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'

class Billader(Aktuatorer):
    def __init__(self,verdi:bool, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Billader")
        self.__serienummerInternal = serienummer
        self.produktnavn = produktnavn
        self.verdi = verdi
        self.produsent = produsent
        list_with_aktuators.append(self)

    def __repr__(self):
        return f'Aktuator({self.__serienummerInternal}) TYPE: Billader STATUS: {"OFF" if self.verdi == False else "ON"} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'
