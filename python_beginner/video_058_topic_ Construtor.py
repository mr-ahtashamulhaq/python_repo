# Create a class Book with a default constructor that initializes title as "Unknown" and author as "Anonymous".
# Add a method show() to display them.

class Book:
    def _init_(self):
        self.title = "Unknown"
        self.author = "Anonymous"

    def show(self):
        print(f"Title: {self.title}, Author: {self.author}")

b = Book()
b.show()

# Create a class Laptop with a parameterized constructor to initialize brand and price.
# Add a method display() to show brand and price.

class Laptop:
    def _init_(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}, Price: {self.price}")

l = Laptop("Dell", 85000)
l.display()

# Create a class Employee with a default constructor to initialize name as "No Name" and salary as 0.
# Add a method show() to display these details.

class Employee:
    def _init_(self):
        self.name = "No Name"
        self.salary = 0

    def show(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

e = Employee()
e.show()

# Create a class Circle with a parameterized constructor to initialize radius.
# Add a method area() to calculate and print the area.

class Circle:
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        print("Area:", 3.14 * self.radius * self.radius)

c = Circle(5)
c.area()

# Create a class Mobile with a default constructor that initializes brand as "Nokia" and price as 1500.
# Add a method info() to display them.

class Mobile:
    def _init_(self):
        self.brand = "Nokia"
        self.price = 1500

    def info(self):
        print(f"Brand: {self.brand}, Price: {self.price}")

m = Mobile()
m.info()