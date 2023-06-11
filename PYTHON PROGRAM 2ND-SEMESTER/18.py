# Write a program that has a class Point. Define another class Location which
# has two objects (Location and destination) of class Point. Also, define a function
# in Location that prints the reflection on the y-axis.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Location:
    def __init__(self, location_x, location_y, destination_x, destination_y):
        self.location = Point(location_x, location_y)
        self.destination = Point(destination_x, destination_y)

    def print_reflection(self):
        reflected_location_x = -self.location.x
        reflected_location_y = self.location.y
        reflected_destination_x = -self.destination.x
        reflected_destination_y = self.destination.y

        reflected_location = Point(reflected_location_x, reflected_location_y)
        reflected_destination = Point(reflected_destination_x, reflected_destination_y)

        print("Original Location: ({}, {})".format(self.location.x, self.location.y))
        print("Original Destination: ({}, {})".format(self.destination.x, self.destination.y))
        print("Reflected Location: ({}, {})".format(reflected_location.x, reflected_location.y))
        print("Reflected Destination: ({}, {})".format(reflected_destination.x, reflected_destination.y))



location = Location(2, 3, 4, 5)


location.print_reflection()
