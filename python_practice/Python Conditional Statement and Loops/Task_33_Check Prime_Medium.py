"""Given an integer n check if n is prime or not.
A prime number is a number that is divisible by 1 and itself only.

Note: Print "True" if n is prime, otherwise print "False"."""

n = int(input("Enter number  : "))
isprime = True
for i in range(2,n):
    if n%i == 0:
        isprime = False
        break
if isprime:
    print(True)
else:
    print(False)