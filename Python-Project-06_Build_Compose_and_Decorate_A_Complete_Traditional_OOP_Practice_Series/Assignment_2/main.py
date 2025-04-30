'''
2. Using cls
Assignment:
Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.
'''

# Make Counter class
class Counter:
    counter = 0  # class variable to count objects

    def __init__(self):
        Counter.counter += 1  # increase count when object is made

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.counter}")  # show total count


# create 4 objects
object1 = Counter()
object2 = Counter()
object3 = Counter()
object4 = Counter()

Counter.display_count()  # call method to show count
