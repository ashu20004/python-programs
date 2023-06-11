# WAP that create a class Student having attribute as name and age and Marks
# class inheriting Students class with its own attributes marks1, marks2 and
# marks3 as marks in 3 subjects. Also, define the class Result that inherits the
# Marks class with its own attribute total. Every class has its own display()
# method to display the corresponding details. Use __init__() and super() to
# implement the above classes.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Marks(Student):
    def __init__(self, name, age, marks1, marks2, marks3):
        super().__init__(name, age)
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def display(self):
        super().display()
        print("Marks in Subject 1:", self.marks1)
        print("Marks in Subject 2:", self.marks2)
        print("Marks in Subject 3:", self.marks3)


class Result(Marks):
    def __init__(self, name, age, marks1, marks2, marks3):
        super().__init__(name, age, marks1, marks2, marks3)
        self.total = self.marks1 + self.marks2 + self.marks3

    def display(self):
        super().display()
        print("Total Marks:", self.total)



student_result = Result("John Doe", 18, 80, 75, 90)


student_result.display()
