'''
1. Using self
Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.
'''

# Make Student class
class Student:
    def __init__(self, name, marks):
        self.name = name  # store name
        self.marks = marks  # store marks

    def display(self):
        print(f"My name is {self.name} and my marks in Math are {self.marks}.")


student = Student("Alishba", 98)  # create object
student.display()  # show info

