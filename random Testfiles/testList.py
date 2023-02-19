liste = []
caller_list = []

class test():
    def __init__(self, name, serial):
        self.name = str(name)
        self.serial = int(serial)
        self.func()

    def func(self):
        newtuple = (self.name, self.serial)
        liste.append(newtuple)


newobject = test("testobjekt", 12341234)
newobject1 = test("testobjekt", 12341234)
newobject2 = test("testobjekt", 12341234)
newobject3 = test("testobjekt", 12341234)

print(liste)

