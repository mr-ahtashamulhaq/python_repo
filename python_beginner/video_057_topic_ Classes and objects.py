# Create a class Car with attributes brand and model, and a method display() to print them using self.

class Car:
    brand = ""
    model = ""

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

car1 = Car()
car1.brand = "Toyota"
car1.model = "Corolla"
car1.display()

# Create a class Rectangle with attributes length and width, and a method area() to print the area.

class Rectangle:
    length = 0
    width = 0

    def area(self):
        print("Area:", self.length * self.width)

rect = Rectangle()
rect.length = 5
rect.width = 3
rect.area()

# Create a class Student with attributes name and marks, and a method show() to display them.

class Student:
    name = ""
    marks = 0

    def show(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

s = Student()
s.name = "Ayesha"
s.marks = 92
s.show()

# Create a class BankAccount with attributes account_holder and balance, and a method deposit() to add amount to balance and show updated balance.

class BankAccount:
    account_holder = ""
    balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder}'s updated balance: {self.balance}")

acc = BankAccount()
acc.account_holder = "Ali"
acc.balance = 1000
acc.deposit(500)

# Create a class Circle with attribute radius and a method circumference() to print the circumference.

class Circle:
    radius = 0

    def circumference(self):
        print("Circumference:", 2 * 3.14 * self.radius)

c = Circle()
c.radius = 7
c.circumference()