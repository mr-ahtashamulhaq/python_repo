# Create a set named colors that contains "red", "green", "blue" Print the set.
colors={"red","green","blue"}
print(colors)
print(type(colors))

# Create a list with some duplicates: convert it to set and check type
s1=[12,19,"ahtasham","a",12,25,19,27,25]
print("\n",set(s1))
print(type(set(s1)))

# Create an empty set, then add "Python" and "Java" to it.Print the set after each addition.

set2=set()
set2.add("pyhton")
print(set2)
set2.add("java")
print(set2)


# Check if "banana" is present in this set:
fruits = {"apple", "banana", "cherry"}
if "banana" in fruits:
  print("\nyes its present")
else:
  print("\nnot present")

fruits = {"apple", "orange", "cherry"}
if "banana" in fruits:
  print("\nyes its present")
else:
  print("\nnot present")


