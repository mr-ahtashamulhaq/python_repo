# Ask the user for two numbers. Try to divide them and print the result. If an error occurs, print "Invalid input" In finally, print "Program ended"
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))

try:
    print(f"\nAnswer is {num1/num2}")

except :
    print ("\nEnter Valid number ")

finally:
  print("program ended!")

# Inside a loop, ask the user for a number. Try dividing 10 by the number.
for i in range(3):
  try:
    a=input("\nenter any number ")
    print(f"{a}/10 = {int(a)/10}")
  except:
    print("\nenter Valid number")
  finally:
    print("Done with this attempt")

  