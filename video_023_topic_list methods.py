# Start with nums = [1, 2, 3] Add 4 to the end using a method.
nums=[1,2,3]
nums.append(4)
print(nums)

 # Insert "blue" at index 1 in colors = ["red", "green","indigo"].
colors = ["red", "green","indigo"]
colors.insert(1,"blue")
print("\n",colors)

# Count how many times 5 appears in nums = [5, 1, 5, 3, 5, 8, 2, 5].
nums = [5, 1, 5, 3, 5, 8, 2, 5]
print("\n",nums.count(5))

# Sort marks = [88, 75, 92, 60, 44, 78, 56] in ascending and then descending order.
print("\n")
marks = [88, 75, 92, 60, 44, 78, 56]
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)

# Reverse letters = ['a', 'b', 'c', 'd'] using a method.
letters = ['a', 'b', 'c', 'd']
letters.reverse()
print(letters)

# Find the index of "pen" in items = ["book", "pen", "notebook","ink"].
items = ["book", "pen", "notebook","ink"]
index=items.index("pen")
print("pen is at",index,"index")