# # Create a class Car with a class variable wheels = 4. Write a class method to change the number of wheels.
class car:
  wheels =4
  
  @classmethod
  def changewheel(cls,newwheel):
    cls.wheels = newwheel

a=car()
print(a.wheels)
#accessing with instance
a.changewheel(7)
print(a.wheels)
#accessing with class
car.changewheel(10)
print(a.wheels)

# Make a class Student that increases a class variable total_students every time an object is created. Use a class method to get the total count.
class student:
  total_students = 0
  def __init__(self):
    student.total_students +=1

  @classmethod
  def getcount(cls):
    return cls.total_students


obj1= student()
obj2=student()
print(f"total no of studnets are {student.getcount()}")
  

# Create a class Animal with a class variable kingdom = "Animalia". Access it and change it using both class name and object.
class animal:
  kingdom="Animalia"
  @classmethod
  def changename(cls, newname):
    cls.kingdom = newname

ani = animal()
print(ani.kingdom)

ani.changename("kingdom1")
print(ani.kingdom)

animal.changename("kingdom2")
print(ani.kingdom)


# Make a class Student where every student belongs to the same school (default). Write a class method to update the school for all students.
class student:
  school = "school of CS"
  def __init__(self, name):
    self.name = name
  @classmethod
  def changename(cls,name):
    cls.school = name
    


stu1 = student("ahtasham")
print(f"student name is {stu1.name} and school is {stu1.school}")

stu1.changename("school of IT")
print(f"student name is {stu1.name} and school is {stu1.school}")