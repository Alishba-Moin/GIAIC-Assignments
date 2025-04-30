'''5. Static Variables and Static Methods
Assignment:
Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.'''

# Make MathUtils class
class MathUtils:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b  # return sum


result = MathUtils.add(4, 6)  # call static method
print(result)  # print result
