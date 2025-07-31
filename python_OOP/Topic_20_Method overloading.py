# Create a class Calculator with a method add() that can add either 2 or 3 numbers using default arguments.

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

c = Calculator()
print(c.add(5, 10))
print(c.add(5, 10, 15))

# Create a class Printer with a print_data() method that works for both int and string using type checking.

class Printer:
    def print_data(self, data):
        if isinstance(data, int):
            print(f"Integer: {data}")
        elif isinstance(data, str):
            print(f"String: {data}")
        else:
            print("Unsupported type")

p = Printer()
p.print_data(123)
p.print_data("python")


# Create a class Greet with greet() method using *args to greet one or more people.

class Greet:
    def greet(self, *names):
        for name in names:
            print(f"Hello, {name}!")

g = Greet()
g.greet("Ali")
g.greet("Ali", "Ahmed", "ahtsham")
