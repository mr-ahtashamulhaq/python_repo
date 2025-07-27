# Ask for name and print Good Morning, [name]! from command line
import sys
name = sys.argv[1]
print ("good morning", name)


#check if user give arguments then print
if len(sys.argv) > 1:
  name = sys.argv[1]
  print(f"hello {name}")
else:
  print("no name provided")



# Create a script that takes two numbers from the command line and adds them. Run it from command line like: python add.py 5 8
# And it should print:
# Sum is: 13

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print(f"sum is {num1 + num2}")
  
  