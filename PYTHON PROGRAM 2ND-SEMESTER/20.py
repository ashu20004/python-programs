# Write a program that create a class Distance with members km and metres.
# Derive classes School and office which store the distance from your house to
# school and office along with other details.


class Distance:
    def __init__(self, km, meters):
        self.km = km
        self.meters = meters


class School(Distance):
    def __init__(self, km, meters, name, address):
        super().__init__(km, meters)
        self.name = name
        self.address = address

    def display_details(self):
        print("School Name:", self.name)
        print("School Address:", self.address)
        print("Distance from Home to School: {} km {} meters".format(self.km, self.meters))


class Office(Distance):
    def __init__(self, km, meters, name, address):
        super().__init__(km, meters)
        self.name = name
        self.address = address

    def display_details(self):
        print("Office Name:", self.name)
        print("Office Address:", self.address)
        print("Distance from Home to Office: {} km {} meters".format(self.km, self.meters))



school = School(5, 200, "ABC School", "123 Main Street")


office = Office(10, 500, "XYZ Office", "456 Elm Street")


school.display_details()
print()
office.display_details()
