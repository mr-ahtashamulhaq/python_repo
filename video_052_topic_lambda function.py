#  Create a lambda function to add two numbers and print the result for 5 and 7.

add = lambda x, y: x + y
print("Sum of 5 and 7 is:", add(5, 7))



# Create a lambda function to calculate the square of a number, and print the square of 6.

square = lambda x: x * x
print("Square of 6 is:", square(6))



# Create a lambda function to find the maximum of two numbers, test it with 10 and 15, and print the maximum.

maximum = lambda a, b: a if a > b else b
print("Maximum of 10 and 15 is:", maximum(10, 15))



#  Create a lambda function to check if a number is even, test it with 9, and print True or False.

is_even = lambda x: x % 2 == 0
print("Is 9 even?:", is_even(9))



#  Create a lambda function to get the last character of a string, test it with "Python", and print the last character.

last_char = lambda s: s[-1]
print("Last character of 'Python' is:", last_char("Python"))