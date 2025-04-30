'''10. Instance Methods
Assignment:
Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.
'''

# Make Dog class
class Dog:
    def __init__(self, name, breed):
        self.name = name  # set dog's name
        self.breed = breed  # set dog's breed

    def bark(self):
        print(f"{self.name}, the {self.breed}, is barking!")  # instance method to bark


# create two dog objects and make them bark
dog1 = Dog("Rocky", "German Shepherd")
dog1.bark()

dog2 = Dog("Max", "Golden Retriever")
dog2.bark()
