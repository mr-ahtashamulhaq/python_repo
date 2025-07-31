# Create a class Student with a public attribute name and a method show_name() to print the name.

class Student:
    def _init_(self):
        self.name = "Ali"

    def show_name(self):
        print("Name:", self.name)

s = Student()
print(s.name)
s.show_name()

# Create a class BankAccount with a protected attribute _balance and a method show_balance() to print it.

class BankAccount:
    def _init_(self):
        self._balance = 1000

    def show_balance(self):
        print("Balance:", self._balance)

b = BankAccount()
print(b._balance)
b.show_balance()

# Create a class Employee with a private attribute __salary and a method show_salary() to print it using name mangling.

class Employee:
    def _init_(self):
        self.__salary = 50000

    def show_salary(self):
        print("Salary:", self.__salary)

e = Employee()
print(e.Employee_salary)
e.show_salary()