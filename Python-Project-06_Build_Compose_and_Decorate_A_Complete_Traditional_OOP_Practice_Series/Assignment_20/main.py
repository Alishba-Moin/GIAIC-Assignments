'''20. Creating a Custom Exception
Assignment:
Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.'''

# Define a custom exception class InvalidAgeError
class InvalidAgeError(Exception):
    pass

# Define a function to check if age is valid
def check_age(age):
    try:
        # If the age is less than 18, raise InvalidAgeError
        if age < 18:
            raise InvalidAgeError("You're not eligible")
    except InvalidAgeError as e:
        # Handle the exception and print the error message
        print(e)
    else:
        # If no exception, print the eligibility message
        print('You are eligible')


check_age(8)  # This will raise and catch InvalidAgeError
