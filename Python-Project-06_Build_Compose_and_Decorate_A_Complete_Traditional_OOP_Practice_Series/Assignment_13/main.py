'''13. Composition
Assignment:
Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.'''

# Make Engine class
class Engine:
    def start_engine(self):
        return "Car engine is starting!"  # method to start the engine


# Make Car class
class Car:
    def __init__(self):
        self.engine = Engine()  # create Engine object within Car class

    def start_engine(self):
        return f"Car starting: {self.engine.start_engine()}"  # call Engine's start method via Car


# create a Car object and start the engine
car = Car()
print(car.start_engine()) 
