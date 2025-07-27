# Write a function area(length, width) that returns the area.
def area(length,width):
  area = length * width
  return area

len=int(input("enter length :"))
wid=int(input("enter width :"))
print("area is",area(len,wid))


# Write a function greet(name="Guest") that prints "Welcome, <name>!"
def greet(name="guest"):
  print("hello",name)

greet()
name="ahtasham"
greet(name)


# Write a function student(name, age, grade) and call it using keyword arguments.
def student(name,age,grade):
  print(name,"is",age,"years old and got",grade,"grade")

student(age=18,grade="A+",name="ahtasham")


# Write a function power(base, exponent=2) that returns base raised to exponent.(Default exponent should be 2)
def power(base,expo=2):
  i=1
  result=1
  while(i<=expo):
    result*=base
    i+=1
  return result

base=5
print("power with default argument :",power(base))
expo=4
print("power with given arguments : ",power(base,expo))





  