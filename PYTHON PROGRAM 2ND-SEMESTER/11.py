# Write a program that has a class Point with attributes x and y.
# a.
# Write a method called midpoint that returns a midpoint of a line joining two
# points.
# b.
# Write a method called length that returns the length of a line joining two
# points.

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other_point):
        mid_x = (self.x + other_point.x) / 2
        mid_y = (self.y + other_point.y) / 2
        return Point(mid_x, mid_y)

    def length(self, other_point):
        dx = other_point.x - self.x
        dy = other_point.y - self.y
        return math.sqrt(dx**2 + dy**2)



point1 = Point(2, 3)
point2 = Point(5, 8)


midpoint = point1.midpoint(point2)
print("Midpoint:", midpoint.x, midpoint.y)


length = point1.length(point2)
print("Length:", length)
