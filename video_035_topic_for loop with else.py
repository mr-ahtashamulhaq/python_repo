# Write a program to search in a list, print "Found" If not found, use else to print "Not Found"

list1=[4,2,6,8,3]
for i in list1:
  if i==7:
    print("found")
    break

else:
  print("not found")

# Use for...else to check if number is prime.
num=int(input("enter any integer "))
for i in range(2,num-1):
  if (num%i==0):
    print("number is not prime")
    break

else:
  print("number is prime")
  

#  Ask the user to input a name. Use for...else to: Print "Welcome" if name found Print "Username not found" if not found
name=["ahtasham","osama","talha","hamza","arslan"]
found=input("enter name to find :")

for i in name:
  if i==found:
    print(f"Welcome {i}".title())
    break

else:
  print("username not found".title())

# Given a list [1, 2, 3, 4, 2] Check if any number is repeated

list=[1, 2, 3, 4, 2]
iteration=len(list)
for i in range(iteration):
  if (list.count(i)>1):
    print(f"{i} is repeated")
    break

else:
  print("Duplicate not found")




















