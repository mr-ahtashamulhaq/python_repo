"""Given a positive integer, n. Find the factorial of n."""
#User function Template for python3
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

print(factorial(5))