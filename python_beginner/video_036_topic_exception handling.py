# Ask the user to enter two numbers. Try to divide the first by the second.

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))

try:
    print(f"\nAnswer is {num1/num2}")

except :
    print ("\nEnter Valid number ")

# Ask the user to enter their age.Use try-except to Convert input to intege
try:
    num = int(input("\nEnter your age: "))
    int(num)
except:
    print("Invalid age!")


# Create a list Ask the user for an index and print that item.
items = ["apple", "banana", "mango"] 
ind=input("\nenter the index: ")
try:
    print(f"item is{items[int(ind)]}")

except:
    print("Enter a valid index")
