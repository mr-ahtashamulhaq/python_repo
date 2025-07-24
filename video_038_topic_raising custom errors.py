# Raise a ValueError with a custom message
raise ValueError("This is a custom ValueError")

# Ask user for age, raise an error if it's negative
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative")

# Create a function that raises a TypeError if input is not a string
def check_name(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
check_name("Ahtasham")

# Raise a custom error inside a division function if denominator is zero
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
print(divide(10, 2))

# Create a custom exception class and raise it
class CustomError(Exception):
    pass
raise CustomError("This is a custom-defined error")
