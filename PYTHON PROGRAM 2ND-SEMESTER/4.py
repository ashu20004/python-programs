# Create a class called Numbers, which has a single class attribute called
# MULTIPLIER, and a constructor which takes the parameters x and y (these
# should all be numbers).
# a. Write an instance method called add which returns the sum of the
# attributes x and y.
# b. Write a class method called multiply, which takes a single number
# parameter a and returns the product of a and MULTIPLIER.
# c. Write a static method called subtract, which takes two number objects, b
# and c, and returns b - c.
# d. Write a method called value which returns a tuple containing the values of x
# and y. 

class Numbers:
    def __init__(self,x,y):
        self.multiplier=x*y
        self.x=x
        self.y=y
        return
    
    def add(self):
        return f"sum={self.x+self.y}"
    
    def multiply(self,a):
        return f"{self.multiplier*a}"
    
    @staticmethod
    def subtract(a,b):
        return f"{b-a}"
    
    def value(self):
        return self.x,self.y
    
a1=Numbers(10,5)

print(a1.add())

print(a1.multiply(2))

print(a1.subtract(3,5))

print(a1.value())
