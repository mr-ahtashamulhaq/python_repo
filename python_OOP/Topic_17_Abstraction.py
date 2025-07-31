from abc import ABC, abstractclassmethod
# Create an abstract class Animal with an abstract method sound().
# Then create Dog and Cat classes that implement sound().
class Animal(ABC):
  @abstractclassmethod
  def sound(self):
    pass

class Dog(Animal):
  def sound(self):
    print( "barking" )
class Cat(Animal):
  def sound(self):
    print( "Meow" )

obj1 = Dog()
obj2 = Cat()
obj1.sound()
obj2.sound()


# Create an abstract class Vehicle with abstract method max_speed().
# Implement it in Bike and Car classes.
class Vehicle(ABC):
  @abstractclassmethod
  def max_speed(self):
    pass

class Bike(Vehicle):
  def max_speed(self):
    print( "max speed is 80" )
class Car(Vehicle):
  def max_speed(self):
    print( "max speed is 180" )

obj1 = Bike()
obj2 = Car()
obj1.max_speed()
obj2.max_speed()


# Create an abstract class called PaymentMethod with an abstract method pay(amount).
# Then create two classes: CreditCard and PayPal that implement the pay method.
# Create objects of both classes and call pay() for each.
class PaymentMethod(ABC):
    @abstractclassmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using CreditCard")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

cc = CreditCard()
pp = PayPal()

cc.pay(500)
pp.pay(300)
