# 1. Student Class ( __str__ and __repr__ ) Create a class Student with attributes: name, roll_no
# Define __str__() → return: "Student Name: Ahtasham, Roll No: 21"
# Define __repr__() → return: "Student('Ahtasham', 21)"
class student:
  def __init__(self, name, rollno):
    self.name = name
    self.rollno = rollno

  def __str__(self):
    return f"student name: {self.name}, Roll no: {self.rollno}"

  def __repr__(self):
    return f"student '{self.name}', {self.rollno}"

s1 = student("ahtasham", 18)
print(s1)
print(repr(s1))

# Create a class Book with attribute: pages and return no of pages

class book:
  def __init__(self, pages):
    self.pages = pages

  def __len__(self):
    return self.pages

b = book(350)
print(len(b)) 
