# Create a class Car with a class variable wheels = 4 and an instance variable color.
# Create two objects with different colors and print color and wheels from both objects.

class Car:
    wheels = 4  # class variable

    def _init_(self, color):
        self.color = color  # instance variable

c1 = Car("Red")
c2 = Car("Blue")

print(c1.color)
print(c1.wheels)
print(c2.color)
print(c2.wheels)

# Create a class School with a class variable school_name = "ABC School".
# Create an instance variable student_name in the constructor and print both using an object.

class School:
    school_name = "ABC School"  # class variable

    def _init_(self, student_name):
        self.student_name = student_name  # instance variable

s = School("Ali")
print(s.student_name)
print(s.school_name)

# Create a class Circle with a class variable pi = 3.14 and an instance variable radius.
# Create an object with radius 5 and print the area of the circle using the object.

class Circle:
    pi = 3.14  # class variable

    def _init_(self, radius):
        self.radius = radius  # instance variable

c = Circle(5)
area = Circle.pi * c.radius * c.radius
print(area)

# Create a class Employee with a class variable company = "Google" and an instance variable name.
# Create two objects and change the class variable using the class, then print company from both objects.

class Employee:
    company = "Google"  # class variable

    def _init_(self, name):
        self.name = name  # instance variable

e1 = Employee("Ali")
e2 = Employee("Ayesha")

print(e1.company)
print(e2.company)

Employee.company = "Amazon"

print(e1.company)
print(e2.company)

# Create a class Library with a class variable library_name = "City Library".
# Add an instance variable book_name and create two objects with different book names.
# Print the book names and library name using both objects.

class Library:
    library_name = "City Library"  # class variable

    def _init_(self, book_name):
        self.book_name = book_name  # instance variable

b1 = Library("Python Programming")
b2 = Library("Data Science")

print(b1.book_name)
print(b1.library_name)
print(b2.book_name)
print(b2.library_name)