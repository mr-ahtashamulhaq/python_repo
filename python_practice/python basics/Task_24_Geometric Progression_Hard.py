"""Given three integers, a, r and n. Where a is the first term, r is the common ratio of a G.P. and r is equal to 2.  Calculate the nth term of GP(Geometric Progression).

The nth term is given by an = a * r(n-1), where r = 2."""
#User function Template for python3
a = int(input("Enter a "))
n = int(input("Enter n "))
r = 2

########### Write your code below ###############
# Compute the GP Term
ans = a * (r**(n-1))
########### Write your code above ###############

print(ans)