'''17. Class Decorators
Assignment:
Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.'''

# Create class decorator to add greet method
def add_greeting(cls):
    def greet(self):
        return f"Decorator: Hello from {self.__class__.__name__} | {self.name}"  # method added by decorator
    cls.greet = greet  # add greet method to the class
    return cls  # return the modified class


# Apply decorator to Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name  # store the name of the person


# Create an object of Person class
person = Person("Alishba")

# Call the greet method added by the decorator
print(person.greet())
