"""Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2 and print in a single line.
Note: Don't add a new line in the end."""
#User function Template for python3
n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
table = n1 - n2
for i in range(1,11):
    print(table * i , end=" ")
