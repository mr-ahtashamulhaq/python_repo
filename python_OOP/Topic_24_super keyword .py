# Create Animal class with __init__(name) and speak() method. Create Dog class that extends it and uses super().
class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    return f"{self.name} making sound"

class dog(Animal):
  def __init__(self,name,breed):
    super().__init__(name)
    self.breed = breed

ob1 = dog("shepherd", "black")
print(ob1.name)
print(ob1.breed)
print(ob1.speak())


# Create a Vehicle class with __init__(brand). Create Car class with model and use super() to set the brand.
class vehicle:
  def __init__(self,brand):
    self.brand = brand

class car (vehicle):
  def __init__(self,brand, model):
    super().__init__(brand)
    super().__init__ (brand)
    self.model = model
  

v1 = car("toyota", 2025)
print(v1.brand, v1.model)


# In Parent class, create a method say(). In Child, override say() but also call the parent’s version using super().
class Parent:
  def say(self):
      print("I am the Parent")

class Child(Parent):
  def say(self):
      super().say()
      print("I am the Child")

c = Child()
c.say()

