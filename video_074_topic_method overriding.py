# Shape and Rectangle Create Shape class with method area() that prints "No area defined" Create Rectangle class that overrides area() and prints area based on length * width
class shape:
  def area(self):
    print("no area defined")

class rectangle(shape):
  def __init__(self, length,width):
    self.length = length
    self.width = width
    
  def area(self):
    return f"area is {self.length * self.width}"

sh1 = rectangle(5,6)
print(sh1.area())


# Vehicle class has a method start() → prints "Starting vehicle" Bike class overrides start() to print "Starting bike with kick
class Vehicle:
  def start(self):
      print("Starting vehicle...")

class Bike(Vehicle):
  def start(self):
      print("Starting bike with kick...") 


v = Vehicle()
b = Bike()

v.start()
b.start()  



# Account class has a method withdraw() → prints "Withdraw successful" SavingsAccount overrides it to check if balance is enough before withdrawing
class Account:
  def __init__(self, balance):
      self.balance = balance

  def withdraw(self, amount):
      print("Withdraw successful")

class SavingsAccount(Account):
  def withdraw(self, amount):
      if amount <= self.balance:
          self.balance -= amount
          print(f"Withdrawn: {amount}. Remaining: {self.balance}")
      else:
          print("Insufficient balance!")

acc = SavingsAccount(500)
acc.withdraw(200)
acc.withdraw(400)


