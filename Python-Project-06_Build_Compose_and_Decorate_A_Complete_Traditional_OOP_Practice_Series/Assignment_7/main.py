'''7. Access Modifiers: Public, Private, and Protected
Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.
'''

# Make Employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name           # Public variable
        self._salary = salary      # Protected variable
        self.__ssn = '1234'        # Private variable

    def get_ssn(self):
        return f"SSN: {self.__ssn}"  # Access private variable

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"{self.name}'s Salary: {self._salary}")


employee = Employee("Alishba", 80000)

print(f"Employee Name: {employee.name}")    # Public - works
print(f"Salary: {employee._salary}")        # Protected - works but not recommended
print(employee.get_ssn())                   # Private - accessed using method

print('=' * 30)

employee.display_details()  # show name and salary
