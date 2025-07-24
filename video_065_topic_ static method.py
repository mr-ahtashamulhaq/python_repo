# Create a class Math with a static method add(a, b) that prints the sum of a and b.

class Math:
    @staticmethod
    def add(a, b):
        print("Sum:", a + b)

Math.add(5, 3)
m = Math()
m.add(10, 15)

# Create a class Converter with a static method km_to_miles(km) that prints the miles equivalent of the km passed (1 km = 0.621371 miles).

class Converter:
    @staticmethod
    def km_to_miles(km):
        miles = km * 0.621371
        print(f"{km} km = {miles} miles")

Converter.km_to_miles(10)
c = Converter()
c.km_to_miles(5)

# Create a class Utility with a static method is_even(num) that prints whether the given number is even or not.

class Utility:
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

Utility.is_even(12)
u = Utility()
u.is_even(7)

# Create a class Greeting with a static method say_hello() that prints "Hello, welcome to Python OOP!".

class Greeting:
    @staticmethod
    def say_hello():
        print("Hello, welcome to Python OOP!")

Greeting.say_hello()
g = Greeting()
g.say_hello()