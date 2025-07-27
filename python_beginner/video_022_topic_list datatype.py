# print the first and last item using indexing.
mylist=[67,456,234,"ahtasham",True,87.9,56.7]
print(mylist[0],mylist[len(mylist)-1])

# Change the second item 
print("\norignal list",mylist)
mylist[1]=999
print("modified list",mylist)

# Write a program that prints the sum of all items in numbers
numbers=[2,3,7,8,10,20]
sum=0
for i in numbers:
  sum+=i
print("\nsum is",sum)

# rint each name from names = ["Alice", "Bob", "Charlie"] using a loop.
names = ["\nAlice", "Bob", "Charlie"]
for i in names:
  print(i)

# Given countries check if "pakistan" is in the list. If yes, print "Found".
countries=["australia","america","india","pakistan","nigeria"]
if"pakistan" in countries:
  print("\nfound")
else:
  print("\nnot found")