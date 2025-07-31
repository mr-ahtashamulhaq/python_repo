# Create a base class with a method, a child class that inherits it and adds another method,
# and a grandchild class that inherits and adds a third method.

class Animal:
    def eat(self):
        print("Animal can eat.")

class Mammal(Animal):
    def walk(self):
        print("Mammal can walk.")

class Dog(Mammal):
    def bark(self):
        print("Dog can bark.")

d = Dog()
d.eat()
d.walk()
d.bark()


# Create a Person class with a method to display the name,
# a Student class that inherits Person and adds roll number,
# and a GraduateStudent class that adds a degree method.

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def show_roll(self):
        print("Roll Number:", self.roll)

class GraduateStudent(Student):
    def __init__(self, name, roll, degree):
        super().__init__(name, roll)
        self.degree = degree

    def show_degree(self):
        print("Degree:", self.degree)

gs = GraduateStudent("Ali", 101, "BSCS")
gs.show_name()
gs.show_roll()
gs.show_degree()


# Create a Vehicle class with a start method,
# a Car class that inherits and adds wheels method,
# and an ElectricCar class that adds battery method.

class Vehicle:
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels.")

class ElectricCar(Car):
    def battery(self):
        print("ElectricCar has a battery.")

ecar = ElectricCar()
ecar.start()
ecar.wheels()
ecar.battery()


# Create a base Shape class with a display method,
# a Rectangle class that inherits Shape and calculates area,
# and a Box class that inherits Rectangle and calculates volume.

class Shape:
    def display(self):
        print("This is a shape.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)

class Box(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        print("Volume:", self.length * self.width * self.height)

b = Box(5, 4, 3)
b.display()
b.area()
b.volume()
