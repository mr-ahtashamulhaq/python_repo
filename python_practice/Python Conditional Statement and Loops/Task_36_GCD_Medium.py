"""Given two numbers a and b. The task is to find the GCD of  a and b.
The GCD of two numbers is the largest number that can divide both a and b perfectly."""

a = int(input("Enter a  : "))
b = int(input("Enter b  : "))
i = 2
gcd=1
condition = a if a<b else b
while(i<condition):
    if (a%i==0) and (b%i==0):
        gcd = i
    i+=1
print(gcd)