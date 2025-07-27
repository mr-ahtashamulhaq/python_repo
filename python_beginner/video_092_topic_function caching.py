# Task 1: Create a cached function power(a, b) that returns a^b (a raised to the power b)
from functools import lru_cache

@lru_cache(maxsize=None)
def power(a, b):
    return a ** b

# Task 2: Create a cached function factorial(n) that returns the factorial of n

@lru_cache(maxsize=None)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Task 3: Create a cached function is_palindrome(s) that checks if a string s is a palindrome(same when reverse)

@lru_cache(maxsize=None)
def is_palindrome(s):
    return s == s[::-1]
