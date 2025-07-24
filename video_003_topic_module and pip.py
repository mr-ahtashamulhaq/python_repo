# Import the math module and print the square root of 64
import math
print(math.sqrt(64))

# Import the random module and print a random number between 1 and 10
import random
print(random.randint(1, 10))

# Import the datetime module and print the current date and time
import datetime
print(datetime.datetime.now())

# Use pip to install the 'pyfiglet' module and print a banner text using it
# (You must run: pip install pyfiglet)
import pyfiglet
print(pyfiglet.figlet_format("Hello"))

# Create your own module named "greet.py" with a function hello(), then import and use it
# greet.py content:
# def hello():
#     print("Hello from custom module!")
import greet
greet.hello()
