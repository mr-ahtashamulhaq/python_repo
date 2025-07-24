# Create a Vector class with x and y components.Overload the + operator using __add__.
class vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self,other):
    return self.x + other.x , self.y + other.y

v1 = vector(5,4)
v2 = vector (5,4)
print(v1 + v2)

# Make a Time class with hours and minutes.Overload the - operator to subtract two time objects correctly
class time:
  def __init__(self, hour, minute):
    self.hour = hour
    self.minute = minute

  def __sub__(self,other):
    self.hour *= 3600
    other.hour *= 3600
    self.minute *= 60
    other.minute *= 60
    
    self.hour -= other.hour
    self.minute -= other.minute

    self.hour //= 3600
    self.minute //= 60

    return time(self.hour , self.minute)

  def __str__(self):
    return f"{self.hour}hr , {self.minute}min"
    

t1 = time(2 , 30)
t2 = time(00 , 30)
print(t1 - t2)


# Create a Box class with length, width, and height Overload the + operator using __add__ to return a new box with added dimensions. Also define __str__ for pretty printing.

class Box:
  def __init__(self, length, width, height):
      self.length = length
      self.width = width
      self.height = height

  def __add__(self, other):
      return Box(
          self.length + other.length,
          self.width + other.width,
          self.height + other.height
      )

  def __str__(self):
      return f"Box({self.length}, {self.width}, {self.height})"

b1 = Box(2, 3, 4)
b2 = Box(1, 1, 1)
b3 = b1 + b2 
print(b3)





    


    

    

