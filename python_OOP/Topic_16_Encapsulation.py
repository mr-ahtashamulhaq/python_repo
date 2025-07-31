# Create a BankAccount class with a private balance variable.
# Add get_balance() and deposit(amount) methods.
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    
    def get_balance(self):
        print(f"balance is {self.__balance}")
    def deposit(self, amount):
        self.__balance += amount

obj = BankAccount(70000)
obj.get_balance()

obj.deposit(30000)
obj.get_balance()


# Create a Student class with private name and grade.
# Use getters and setters to safely access and change values.
class Student:
    def __init__(self,name, grade):
        self.__name = name
        self.__grade = grade
    
    def get_fun(self):
        print(f"name : {self.__name} \n grade:{self.__grade}")
    def set_fun(self, name, grade):
        self.__name = name
        self.__grade = grade

obj = Student("ahtasham", "A+")
obj.get_fun()

obj.set_fun("Ali", "B")
obj.get_fun()


# Create a class Student with private variables __name and __marks.
# Add set_data(name, marks) and get_data() methods to safely set and get the values.
class Student:
    def __init__(self):
        self.__name = ""
        self.__marks = 0

    def set_data(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_data(self):
        return f"Name: {self.__name}, Marks: {self.__marks}"

s = Student()
s.set_data("Ahtasham", 92)
print(s.get_data())
