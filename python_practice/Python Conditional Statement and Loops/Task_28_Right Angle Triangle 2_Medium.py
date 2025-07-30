"""Given an integer n. Write a program to print the Right angle triangle. The length of the perpendicular and base is n. """
"""
*
*  *
*    *
*      *
*        *
*          *
*            *
*              *
* * * * * * * * * 

"""
n = int(input("Enter n : "))
for i in range (1,n):
    if i ==1:
        print("*" *i)
    # elif i==2:
    #     print("*"+" "*(i) + "*")
    elif i>1:
        print("*"+"  "*(i-1) + "*")
print("* "*n)