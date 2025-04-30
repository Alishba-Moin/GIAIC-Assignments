'''9. Abstract Classes and Methods
Assignment:
Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().'''

# Import ABC and abstractmethod from abc module
from abc import ABC, abstractmethod

# Create abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):  # abstract method to calculate area
        pass

# Create Rectangle class that inherits Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  # set length
        self.width = width    # set width

    def area(self):
        return self.length * self.width  # calculate area of rectangle

# create rectangle object and calculate area
rectangle = Rectangle(6, 3)
print(f"Area of a Rectangle: {rectangle.area()}")
