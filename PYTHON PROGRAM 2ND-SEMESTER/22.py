# Write a program that has a class Polygon. Derive two classes Rectangle and
# triangle from polygon and write methods to get the details of their dimensions
# and hence calculate the area.

class polygen:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class rectangle(polygen):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width
    
class triangle(polygen):
    def __init__(self, height, base):
        super().__init__(height, base)

    def area(self):
        return self.length * self.width / 2
    

r1 = rectangle(3, 4)
t1 = triangle(3, 4)
print(r1.area())
print(t1.area())
