# Hierarchical Inheritance:
# Create a base class Vehicle with a method,
# create Car and Bike classes inheriting Vehicle,
# each having their own method.

class Vehicle:
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding.")

c = Car()
c.start()
c.drive()

b = Bike()
b.start()
b.ride()


# Hierarchical Inheritance:
# Create a base class Person with a method,
# create Teacher and Student classes inheriting Person,
# each with their own method.

class Person:
    def show_person(self):
        print("This is a person.")

class Teacher(Person):
    def teach(self):
        print("Teaching students.")

class Student(Person):
    def study(self):
        print("Studying subjects.")

t = Teacher()
t.show_person()
t.teach()

s = Student()
s.show_person()
s.study()


# Hybrid Inheritance:
# Create a base class Electronics, inherit Mobile and Laptop from it,
# then create a SmartPhone class that inherits from Mobile,
# showing combination of hierarchical + multilevel.

class Electronics:
    def power_on(self):
        print("Electronics powered on.")

class Mobile(Electronics):
    def call(self):
        print("Calling from mobile.")

class Laptop(Electronics):
    def code(self):
        print("Coding on laptop.")

class SmartPhone(Mobile):
    def browse(self):
        print("Browsing on smartphone.")

sp = SmartPhone()
sp.power_on()
sp.call()
sp.browse()

l = Laptop()
l.power_on()
l.code()