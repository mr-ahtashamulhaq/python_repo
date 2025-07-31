# Write four functions: add, sub, mul, and div to perform basic arithmetic operations.Then create a higher-order function calculator(func, x, y) that takes one of these functions and two numbers
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x//y if x>y else y//x

def calculator(otherfunc, x, y):
    return otherfunc(x,y)

print(calculator(add,7,5))


# Create a list of numbers. Use map() with a lambda to square all numbers in the list.
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, nums))
print(squared)


# Write a function square(x) that returns x*x.
# Then write a higher-order function apply(func, value) that applies the passed function to the value.
def square(x):
    return x * x

def apply(func, value):
    return func(value)

print(apply(square, 5))