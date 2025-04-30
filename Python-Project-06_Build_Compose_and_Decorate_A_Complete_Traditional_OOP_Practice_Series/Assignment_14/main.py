'''14. Aggregation
Assignment:
Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.'''

# Make Employee class
class Employee:
    def __init__(self, name):
        self.name = name  # set employee name


# Make Department class with aggregation
class Department:
    def __init__(self, name, employee):
        self.name = name  # set department name
        self.employee = employee  # store reference to Employee object

    def show_detail(self):
        print(f"Department: {self.name}")
        print(f"Employee: {self.employee.name}")  # access employee name


# create Employee object
employee = Employee('Alishba')

# create Department object and assign Employee to it
department = Department("Research and Development (R&D)", employee)

department.show_detail()  # show department and employee details
