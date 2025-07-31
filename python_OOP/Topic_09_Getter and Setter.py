# Create a class Student with a private attribute __marks.
# Use @property and @marks.setter to get and set the marks safely with validation (0-100).

class Student:
    def _init_(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Marks must be between 0 and 100.")

s = Student()
s.marks = 85
print(s.marks)
s.marks = 150

# Create a class Circle with a private attribute __radius.
# Use @property and @radius.setter to get and set radius, ensuring radius cannot be negative.

class Circle:
    def _init_(self):
        self.__radius = 0

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self.__radius = value
        else:
            print("Radius cannot be negative.")

c = Circle()
c.radius = 5
print(c.radius)
c.radius = -3

# Create a class Employee with a private attribute __salary.
# Use @property and @salary.setter to ensure salary is set only if it is above 15000.

class Employee:
    def _init_(self):
        self.__salary = 0

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 15000:
            self.__salary = value
        else:
            print("Salary must be at least 15000.")

e = Employee()
e.salary = 20000
print(e.salary)
e.salary = 12000

# Create a class Account with a private attribute __balance.
# Use @property and @balance.setter to get and set balance, ensuring it is not negative.

class Account:
    def _init_(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative.")

a = Account()
a.balance = 5000
print(a.balance)
a.balance = -1000

# Create a class Product with a private attribute __price.
# Use @property and @price.setter to get and set the price with validation that price must be greater than 0.

class Product:
    def _init_(self):
        self.__price = 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Price must be greater than 0.")

p = Product()
p.price = 350
print(p.price)
p.price = 0