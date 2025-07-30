"""Given an integer n,  write a program to print the square wall of size n using nested loops. Try not to use String multiplication."""
n = int(input("Enter n : "))

for i in range (n):
    for j in range(n):
        print("*", end=" ")
    print()