'''6. Constructors and Destructors
Assignment:
Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).'''

# Make Logger class
class Logger():
    def __init__(self):
        print("Object has been created!")  # constructor message

    def __del__(self):
        print("Object has been destroyed!")  # destructor message


log = Logger()  # create object

del log  # delete object
