# Create a class Vehicle with a method move() that prints "Vehicle is moving".
# Create a class Car that inherits from Vehicle and has a method horn() that prints "Car horn sounds".

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def horn(self):
        print("Car horn sounds")

c = Car()
c.move()
c.horn()

# Create a class Animal with a method eat() that prints "Animal is eating".
# Create a class Dog that inherits from Animal and has a method bark() that prints "Dog is barking".

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()
d.bark()

# Create a class Teacher with a method teach() that prints "Teacher is teaching".
# Create a class MathTeacher that inherits from Teacher and has a method explain_math() that prints "Explaining math concepts".

class Teacher:
    def teach(self):
        print("Teacher is teaching")

class MathTeacher(Teacher):
    def explain_math(self):
        print("Explaining math concepts")

m = MathTeacher()
m.teach()
m.explain_math()