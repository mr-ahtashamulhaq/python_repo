"""Given a positive integer n, find the sum of the first n natural numbers."""
def sum(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum

# print(sum(4))