"""Given an integer n, write a program to return the factorial of n. The Factorial of a number is the product of all the numbers from 1 to n."""
#User function Template for python3
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

print(factorial(5))