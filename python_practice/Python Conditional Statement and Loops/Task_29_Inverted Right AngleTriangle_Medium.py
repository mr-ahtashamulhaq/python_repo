"""Given an integer n. Write a program to print the inverted "Right angle triangle" wall. The length of the perpendicular and base is n."""
#                * * * * * 
#                * * * *
#                * * *
#                * *
#                *


n = int(input("Enter n : "))
for i in range (n,-1,-1):
    print("* " * i)