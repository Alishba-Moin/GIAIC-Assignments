'''19. callable() and __call__()
Assignment:
Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.'''


# Create a Multiplier class
class Multiplier:
    # Initialize the class with a factor
    def __init__(self, factor):
        self.factor = factor  # store the factor

    # Define the __call__ method to make the object callable
    def __call__(self, input):
        return input * self.factor  # multiply input by the factor

# Create a Multiplier object with factor 4
multiplies = Multiplier(4)

# Test if the object is callable using callable()
print(callable(multiplies))  # returns True because the object can be called

# Call the object like a function 
print(multiplies(2)) 
