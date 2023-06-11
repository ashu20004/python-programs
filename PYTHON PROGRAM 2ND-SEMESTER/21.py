# Write a program to create an abstract class Vehicle. Derive three classes Car,
# Motorcycle and Truck from it. Define appropriate methods and print the details
# of vehicle.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def display_details(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    def display_details(self):
        print("Car Details:")
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Color:", self.color)

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

    def display_details(self):
        print("Motorcycle Details:")
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Type:", self.type)

class Truck(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    def display_details(self):
        print("Truck Details:")
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Capacity:", self.capacity)


car = Car("Toyota", "Camry", 2022, "Red")
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, "Cruiser")
truck = Truck("Ford", "F-150", 2020, "2 tons")


car.display_details()
print()
motorcycle.display_details()
print()
truck.display_details()
