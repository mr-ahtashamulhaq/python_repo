"""print sum of first 5 natural numbers using functional Recursion"""

def func(n):
    if n==1:
        return 1
    else:
        return n  + func(n-1)
    
x = func(5)
print(x)

# Output : 15