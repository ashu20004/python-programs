# Create a class Employee that keeps a track of the number of employees in an
# organization and also stores their name, designation and salary details.
# a.
# Write a method called getdata to take input (name, designation, salary)
# from user.
# b.
# Write a method called average to find average salary of all the employees
# in the organization.
# c.
# Write a method called display to print all the information of an employee.

class Employee:
    employee=0
    t_salary=0
    def __init__(self):
        Employee.employee+=1
    def getdata(self):
        self.name,self.designation,self.salary=input("Enter name,designation,salary:").split(',')
        Employee.t_salary+=int(self.salary)

    def average(self):
        avg=Employee.t_salary/Employee.employee
        return avg 
    def display(self):
        return print(f"{self.name} has {self.salary} and designations {self.designation}")

a=Employee()

a.getdata()

a.display()
