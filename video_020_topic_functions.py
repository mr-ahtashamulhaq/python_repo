# Write a function add(a, b) that returns the sum of a and b.
def sum(a,b):
  return a+b

# Write a function is_even(num) that returns True if the number is even, else False.
def iseven(a):
  if(a%2==0):
     return True
  else:
     return False

# Write a function find_max(x, y, z) that returns the largest of three numbers.
def findmax(a,b,c):
  if a>b and a>c:
    print(a,"is laregst number")
  elif b>a and b>c:
    print(b,"is laregst number")
  else:
    print(c,"is laregst number")

# Write a function reverse_string(s) that returns the reversed string.
def reverse_string(str):
  print(str[::-1])
    
    

a=7
b=45
print ("sum is",sum(a,b))


num=int(input("enter any number : "))
if iseven(num):
  print("number is even")
else:
  print("number is odd")


x=int(input("enter first number : "))
y=int(input("enter second number : "))
z=int(input("enter third number : "))
findmax(x,y,z)


str="ahtasham ul haq"
reverse_string(str)


