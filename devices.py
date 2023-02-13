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
        return f'Sensor ({self.__serienummerInternal}) Type: Fuktighetssensor STATUS: {self.verdi} % PRODUCT DETAILS: {self.produsent} {self.produktnavn}'    


class TemperaturSensor(Sensorer):
    def __init__(self,verdi:float, produsent:str, produktnavn:str, serienummer:str):
        super().__init__(serienummer, "Temperatursensor")
        self.__serienummerInternal = serienummer
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
        self.state = Smartlys.On_OFF_state(self)
        list_with_aktuators.append(self)

    def On_OFF_state(self) -> str:
        if self.verdi  == True:
            return 'ON'
        else : 
            return 'OFF'
    
    def __repr__(self):
        return f'Aktuator ({self.__serienummerInternal}) Type: Smart Lys STATUS: {self.state} PRODUCT DETAILS: {self.produsent} {self.produktnavn}'


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




strømmåler = Strømmåler(0.5,"Moen Inc Prodder","Ute 1.2","e237beec-2675-4cb0")
pumpe1 = Varmepumpe(True,"Moen Inc Prodder","Ute 1.2","e237beec-2675-4cb0")
temp1 = TemperaturSensor(30.3,"Moen Inc Prodder","Ute 1.2","e237beec-2675-4cb0")
temp2 = TemperaturSensor(35.3,"Moen Inc Prodder","Ute 1.2","e237beec-2675-4cb0")
temp3 = TemperaturSensor(37.3,"Moen Inc Prodder","Ute 1.2","e237beec-2675-4cb0")
lys1 = Smartlys(True,"Moen Inc Prodder","Ute 1.2","e237beec-2675-4cb0")
lys2 = Smartlys(False,"Moen Inc Prodder","Ute 1.2","e237beec-2675-4cb0")
lys3 = Smartlys(True,"Moen Inc Prodder","Ute 1.2","e237beec-2675-4cb0")
fukt1 = Fuktighetssensor(20.3,"Moen Inc Prodder","Ute 1.2","e237beec-2675-4cb0")
fukt2 = Fuktighetssensor(20.5,"Moen Inc Prodder","Ute 1.2","e237beec-2675-4cb0")
fukt3 = Fuktighetssensor(17.4,"Moen Inc Prodder","Ute 1.2","e237beec-2675-4cb0")

print(len(list_with_aktuators))
print(len(list_with_sensors))
print(len(list_with_devices))
print(list_with_sensors[4].verdi)
#print(list_with_sensors[0])
print(repr(list_with_sensors[3]))
# print(list_with_aktuators[0].state)
# print(list_with_aktuators[3].state)
# print(list_with_aktuators[2].state)
