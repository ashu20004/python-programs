# Write a program that extends the class Shape to calculate the area of a circle
# and a cone .(use super to inherit base class methods)

import math

class Shape:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Shape:", self.name)

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius * self.radius
        print("Area of the Circle:", area)

class Cone(Shape):
    def __init__(self, name, radius, height):
        super().__init__(name)
        self.radius = radius
        self.height = height

    def calculate_area(self):
        base_area = math.pi * self.radius * self.radius
        lateral_area = math.pi * self.radius * math.sqrt(self.radius*self.radius + self.height*self.height)
        area = base_area + lateral_area
        print("Area of the Cone:", area)



circle = Circle("Circle", 5)

circle.display()

circle.calculate_area()

print()


cone = Cone("Cone", 3, 4)

cone.display()
cone.calculate_area()
