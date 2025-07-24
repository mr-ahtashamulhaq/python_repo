# Write a recursive function factorial(n) that returns the factorial of a number.
def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact(n-1)
    
n=int(input("enter number to calculate factorial: "))
print(f"factorial of {n} is {fact(n)}")

# Write a function sum_n(n) that returns the sum of the first n natural numbers.
def sum(n):
  if n==0:
    return 0
  else:
    return n+sum(n-1)

print(sum(5))

# Write a function power(base, exp) that calculates base ** exp using recursion.
def power(base,expo):
  if expo==0:
    return 1
  else:
    return base*power(base,expo-1)
    
base=5
expo=3
print(power(base,expo))

# Write a function count_digits(n) that returns the number of digits in n using recursion.
def count_digit(n):
  if n<=10:
    return 1
  else:
    return 1+count_digit(n//10)

print(count_digit(34625))

# Write a function fibbonaci(n) that returns the fibbonaci series to n using recursion.
def fib(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fib(n-1)+ fib(n-2)

n=5
for i in range(n):
  print(fib(i),end=" ")







