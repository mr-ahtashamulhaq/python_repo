"""Given an integer n. Write a program to find the nth Fibonacci number.
F(0)= 0, F(1)=1"""


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
n = int(input("Enter number  : "))
print(fib(n))