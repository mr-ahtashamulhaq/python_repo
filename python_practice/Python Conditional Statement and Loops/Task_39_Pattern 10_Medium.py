"""Geek is very fond of patterns. Once, his teacher gave him a pattern to solve. He gave Geek an integer n and asked him to build a pattern."""

#                  * 
#                  * *
#                  * * *
#                  * *
#                  *

n = int(input("Enter n : "))


for i in range (1,n+1):
    print("* " * i)

for i in range (n-1,-1,-1):
    print("* " * i)