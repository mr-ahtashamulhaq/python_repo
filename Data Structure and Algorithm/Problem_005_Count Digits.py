"""Count number of digits of a given number n"""
n = 38279
num = n
count = 0
while (num>0):
    count +=1
    num = num//10

print(count)

# method 2
from math import log10

digits  = int(log10(n) + 1)
print(digits)

# Output: 5