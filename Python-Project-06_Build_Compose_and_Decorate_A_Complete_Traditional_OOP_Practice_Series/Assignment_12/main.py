'''12. Static Methods
Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.'''

# Make TemperatureConverter class
class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32  # convert Celsius to Fahrenheit
    

print(f"F: {TemperatureConverter.celsius_to_fahrenheit(47)}")
