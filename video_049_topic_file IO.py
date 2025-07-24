# Create a file named hello.txt and write "Hello Python!" in it.
with open("hello.txt","w") as file:
  file.write("Hello python!")

# # Open hello.txt, read the content, and print it.
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

# Append "Welcome to File I/O" to hello.txt (on a new line).
with open("hello.txt", "a") as file : 
  file.write("\nWelcome to file I/O")

# Create a file called user_data.txt.
# Ask the user to input their: 
# Name, Age, City , Write this info in the file in this format:
# Name: Ali, Age: 20, City: Lahore

with open("user_data.txt","w") as file:
  name = input("enter your name : ")
  age = input("enter your age: ")
  city = input("enter your city : ")

  file.write(f"name: {name}, Age: {age}, City: {city}")

# Read a file called story.txt, count how many times the word "Python" appears (case insensitive), and print the count.
with open ("story.txt", "r") as file:
  content = file.read()
  content = content.split(" ")
  count = 0
  for word in content:
    if word == "Python":
      count+=1

  print(f"word python repeats {count} times")