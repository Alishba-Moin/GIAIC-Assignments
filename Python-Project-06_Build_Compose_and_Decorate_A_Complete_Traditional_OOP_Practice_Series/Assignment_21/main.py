'''Assignment:
Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.'''

class Countdown:
    def __init__(self, start):
        self.current = start  # Start number for the countdown

    def __iter__(self):
        return self  # Return the object itself to be used as an iterator
    
    def __next__(self):
        if self.current < 0:  # Stop the iteration once we reach below 0
            raise StopIteration
        else:
            number = self.current  # Get the current number
            self.current -= 1  # Decrement the number for the countdown
            return number
        
# Using the Countdown class in a for-loop
for num in Countdown(3):
    print(num)
