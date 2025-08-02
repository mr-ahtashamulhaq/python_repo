"""A lucky number is defined using a special elimination process:
   1. Start with natural numbers: 1, 2, 3, 4, 5, 6, ...
   2. In the 1st step, remove every 2nd number.
   3. In the 2nd step, remove every 3rd remaining number.
   4. In the 3rd step, remove every 4th remaining number, and so on...
This continues indefinitely. Given an integer n, determine if it remains after all steps.
Return 1 if n is a lucky number, otherwise return 0."""

def isLucky(n):
    counter = 2
    while counter <= n:
        if n % counter == 0:
            return 0
        n -= n // counter
        counter += 1
    return 1

print(isLucky(7))
