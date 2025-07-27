# Create a function that takes any number of arguments using *args and prints their sum.

def sum_all(*args):
    total = sum(args)
    print("Sum:", total)

sum_all(1, 2, 3, 4, 5)

# Create a function that takes any number of keyword arguments using **kwargs and prints each key with its value.

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Ali", age=21, subject="Python")

# Create a decorator that prints "Function is starting" before a function runs and "Function has ended" after it runs, then apply it to a greet() function that prints "Hello, World!"

def notify(func):
    def wrapper():
        print("Function is starting")
        func()
        print("Function has ended")
    return wrapper

@notify
def greet():
    print("Hello, World!")

greet()

# Create a decorator that works with any number of arguments (*args, **kwargs) and prints "Running function..." before execution and "Done." after execution. Apply it to a function that prints the product of two numbers.

def notifier(func):
    def wrapper(*args, **kwargs):
        print("Running function...")
        func(*args, **kwargs)
        print("Done.")
    return wrapper

@notifier
def multiply(a, b):
    print("Product:", a * b)

multiply(4, 5)

# Create a function using *args to find the maximum value from all the numbers passed and print it.

def find_max(*args):
    print("Maximum:", max(args))

find_max(10, 25, 5, 40, 32)