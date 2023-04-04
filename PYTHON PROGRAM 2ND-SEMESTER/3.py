#Create a Python class named Rectangle constructed by a length and width.
#a. Create a method called area which will compute the area of a rectangle. 

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        return 
    
    def area(self):
        return f"area= {self.length*self.width} "

box1=Rectangle(12,15)

box2=Rectangle(10,5)

print(box1.area())
print(box2.area())