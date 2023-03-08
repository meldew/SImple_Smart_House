from datetime import date

# liste = []
# caller_list = []

# class test():
#     def __init__(self, name, serial):
#         self.name = str(name)
#         self.serial = int(serial)
#         self.func()

#     def func(self):
#         newtuple = (self.name, self.serial)
#         liste.append(newtuple)


# newobject = test("testobjekt", 12341234)
# newobject1 = test("testobjekt", 12341234)
# newobject2 = test("testobjekt", 12341234)
# newobject3 = test("testobjekt", 12341234)

# print(liste)

"""
s = pd.Series([1, 2, 3])
print(s.describe()[1])

dictionary = {
    "Room1": [s.describe()[3], s.describe()[7], s.describe()[1]],
    "Room2": [20.5, 30.5, 25.6],
}

print(dictionary["Room1"][2])
"""
day = date(year=2023, month=2, day=13)
newdate = day.strftime("%Y-%m-%d")
print(newdate)
