# Use dir() on a list Create a list and print all the available methods using dir().
# Make a Person class with some instance variables. Create an object and print __dict__.
# Try help(len) and read what it shows.
x = [1, 2, 3, 4, 5]
print(dir(x))


class person:
  def __init__(self,name, age):
    self.name = name
    self.age = age
p1 = person("ahtasham", 18)
print("\n\n",p1.__dict__)

help(len)


# Define a class Calculator with add() and subtract() methods. Then use dir() to list all available methods and attributes.
class Calculator:
  def add(self, x, y):
      return x + y

  def subtract(self, x, y):
      return x - y

calc = Calculator()

print(dir(calc))

