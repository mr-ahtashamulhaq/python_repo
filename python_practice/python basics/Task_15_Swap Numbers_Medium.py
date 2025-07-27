"""Given two numbers a and b, you need to swap their values so a holds the value of b and b holds the value of a. Just write the code to swap values of a and b at the specified place."""
a = int(input("Enter a vlaue"))
b = int(input("Enter b value"))

a , b = b , a

print(a, b)