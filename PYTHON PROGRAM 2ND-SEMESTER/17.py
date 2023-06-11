# WAP that extends the class Employee. Derive two classes Manager and Team
# Leader from Employee class. Display all the details of the employee working
# under a particular Manager and Team Leader.

class Employee:
    def __init__(self, emp_id, name, age, address):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.address = address

    def display_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)


class Manager(Employee):
    def __init__(self, emp_id, name, age, address, employees):
        super().__init__(emp_id, name, age, address)
        self.employees = employees

    def display_managed_employees(self):
        print("Employees managed by", self.name, ":")
        for employee in self.employees:
            employee.display_details()
            print()


class TeamLeader(Employee):
    def __init__(self, emp_id, name, age, address, team):
        super().__init__(emp_id, name, age, address)
        self.team = team

    def display_team_members(self):
        print("Team members under", self.name, ":")
        for employee in self.team:
            employee.display_details()
            print()



employee1 = Employee(1, "John Doe", 30, "123 Main St")
employee2 = Employee(2, "Jane Smith", 35, "456 Elm St")
employee3 = Employee(3, "Mike Johnson", 25, "789 Oak St")
employee4 = Employee(4, "Emily Davis", 40, "321 Pine St")
employee5 = Employee(5, "Alex Brown", 28, "654 Maple St")


manager = Manager(100, "John Manager", 45, "789 Broadway St", [employee1, employee2])


team_leader = TeamLeader(200, "Jane Team Leader", 32, "987 Park St", [employee3, employee4, employee5])


manager.display_managed_employees()


team_leader.display_team_members()
