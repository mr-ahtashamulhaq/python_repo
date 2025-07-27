  # names = ["Ali", "Hamza", "Sara"] Use enumerate() to print:
names = ["Ali", "Hamza", "Sara"]
for index, name in enumerate(names):
  print(f"{index} : {name}")


# words = ["sun", "moon", "star", "sky"] Print the index of the word "star" using enumerate
words = ["sun", "moon", "star", "sky"]
for index,i in enumerate(words):
  if i == "star":
    print(f"index is {index}")


# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango','orange','strawberry']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
  


