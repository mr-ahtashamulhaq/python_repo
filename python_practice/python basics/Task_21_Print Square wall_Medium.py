"""Given an integer n,  write a program to print the square wall of size n using nested loops. Try not to use String multiplication."""
#User function Template for python3
n = int(input("Enter n : "))

# Your code here
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()