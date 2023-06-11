# Write a program to compare two-person object based on their age by
# overloading > operator.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
if person1 > person2:
    print("Person 1 is older")
else:
    print("Person 2 is older")
