'''8. The super() Function
Assignment:
Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.'''

# Make base class Person
class Person:
    def __init__(self, name):
        self.name = name  # set name


# Make child class Teacher
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # call base class constructor
        self.subject = subject  # set subject

    def display(self):
        print(f"Teacher Name: {self.name}\nSubject: {self.subject}")


teacher = Teacher("Alishba", "English")  # create object
teacher.display()  # show teacher info
