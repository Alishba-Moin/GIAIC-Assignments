'''16. Function Decorators
Assignment:
Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().'''


# Create decorator function to log function call
def log_function_call(func):
    def wrapper(name):
        print("Decorator: Function is being called!")  # log before function execution
        func(name)  # call the original function
    return wrapper  # return the wrapper function


# Apply decorator to sayhello function
@log_function_call
def sayhello(name):
    print(f'Hello {name}')  # original function behavior

# Call the decorated function
sayhello('Alishba')
sayhello('Mishal')
