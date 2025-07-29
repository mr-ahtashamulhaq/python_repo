"""Given an integer year. Print "True" (without quotes) if it can represent a leap year, otherwise print "False" (without quotes)."""
year = int(input("enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("True")
else:
    print("False")

