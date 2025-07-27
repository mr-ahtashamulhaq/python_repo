# # Create a class Book with title and author. Use a classmethod to create a book from "Python Basics-John Doe".
class book:
  def __init__(self,name,author):
    self.name = name
    self.author = author
    
  @classmethod
  def fromstr(cls,string):
    name = string.split("-")[0]
    author = string.split("-")[1]
    return cls(name, author)

b1 = book.fromstr("Python basics-John Doe")
print(b1.name)
print(b1.author)


# Build a class MyDate(day, month, year) and an alternative constructor to accept "18-07-2025" and convert it.
class myDate:
  def __init__(self, day , month , year):
    self.day = day
    self.month = month
    self.year = year

  @classmethod
  def acceptdate(cls,string):
    day , month , year = string.split("-")
    return cls(int(day), int(month), int(year))

d1 = myDate.acceptdate("18-07-2025")
print("date : ", d1.day)
print("month : ", d1.month)
print("year : ", d1.year)


# Create a class Employee with name and salary, and make a class method that creates an object from a string like "john,50000".
class Employee:
  def __init__(self, name, salary):
      self.name = name
      self.salary = salary

  @classmethod
  def from_csv(cls, data_str):
      name, salary = data_str.split(",")
      return cls(name, int(salary))

emp1 = Employee.from_csv("john,50000")

print("Name:", emp1.name)
print("Salary:", emp1.salary)


