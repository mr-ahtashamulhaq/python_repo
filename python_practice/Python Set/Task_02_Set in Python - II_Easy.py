"""This is the last practice question of Python Set. You are familiar with working on the set in Python. Now, let's move on to work on two sets using some inbuilt functions which are used widely. 
They are:
union(): Used to find union() between two sets. It performs this using '|' operator.

intersection(): Used to find intersection() between two sets. It performs this using '&' operator.

difference(): Difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly for B - A holds the same."""
def common_in_set(a, b):
    return a & b 

def diff(a, b):
    return a - b

def all_in_set(a, b):
    return a | b  

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Common elements:", common_in_set(a, b))
print("Elements only in a:", diff(a, b))        
print("All elements (union):", all_in_set(a, b)) 