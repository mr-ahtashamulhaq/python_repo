# Add a docstring: "Greets the user with their name."
def greet(name):
  """Greet the user with their name"""
  print(f"hello {name}".upper())

name=input("enter your name : ")
greet(name)
print(greet.__doc__)

# Add a docstring: "Takes in a number n, returns the square of n"
def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
  
square(5)
print(square.__doc__)

