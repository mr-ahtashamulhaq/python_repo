# Person has name, age Student adds roll_no, and method show_info() 
class person:
  def __init__ (self,n,a):
    self.name = n
    self.age = a


class Student(person):
  def __init__ (self,n,a,r):
    super().__init__(n,a)
    self.rollno = r

  def showinfo(self):
    print(f"{self.name} , {self.age} , {self.rollno}")

p1 = Student("ahtasham", 19 , 6660)
p1.showinfo()


# Vehicle has method start() Car inherits from it and adds drive() method
class Vehicle:
  def start(self):
      print("Vehicle has started.")

class Car(Vehicle):
  def drive(self):
      print("Car is now driving.")


c = Car()
c.start() 
c.drive()


# Employee stores name, salary Manager adds department and method show()
class Employee:
  def __init__(self, name, salary):
      self.name = name
      self.salary = salary

class Manager(Employee):
  def __init__(self, name, salary, department):
      super().__init__(name, salary)
      self.department = department

  def show(self):
      print(f"Name: {self.name}")
      print(f"Salary: {self.salary}")
      print(f"Department: {self.department}")

m = Manager("Ahtasham", 50000, "IT")
m.show()


  