# Write a program to create class Employee. Display the personal information
# and salary details of 5 employees using single inheritance.

class Employee:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_personal_info(self):
        print("Personal Information:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)


class Salary(Employee):
    def __init__(self, name, age, address, salary):
        super().__init__(name, age, address)
        self.salary = salary

    def display_salary_details(self):
        print("Salary Details:")
        print("Name:", self.name)
        print("Salary:", self.salary)



employee1 = Salary("John Doe", 30, "123 Main St", 50000)
employee2 = Salary("Jane Smith", 35, "456 Elm St", 60000)
employee3 = Salary("Mike Johnson", 25, "789 Oak St", 45000)
employee4 = Salary("Emily Davis", 40, "321 Pine St", 70000)
employee5 = Salary("Alex Brown", 28, "654 Maple St", 55000)


employee1.display_personal_info()
employee1.display_salary_details()
print()

employee2.display_personal_info()
employee2.display_salary_details()
print()

employee3.display_personal_info()
employee3.display_salary_details()
print()

employee4.display_personal_info()
employee4.display_salary_details()
print()

employee5.display_personal_info()
employee5.display_salary_details()
