# Create a Python class named Circle constructed by a radius. Use a class
# variable to define the value of constant PI.
# a.
# Write two methods to be named as area and circum to compute the area
# and the perimeter of a circle respectively by using class variable PI.
# b.
# Write a method called display to print area and perimeter

class circle:
    PI=22/7
    def __init__(self,r):
        self.r=r


    def area(self):
        return circle.PI*self.r*self.r
    def circum(self):
        return 2*circle.PI*self.r
    
    def display(self):
        print(self.area())
        print(self.circum())

circle1=circle(5)
circle1.area()
circle1.circum()
circle1.display()