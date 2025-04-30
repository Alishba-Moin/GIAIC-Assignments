'''
3. Public Variables and Methods
Assignment:
Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.'''

# Make Car class
class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):
        print(f"The {self.brand} car has started!")  # public method


car = Car("Toyotta")  # create object

car.start()  # call method

print(car.brand)  # access variable

