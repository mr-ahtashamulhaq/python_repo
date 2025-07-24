# Create a global variable language = "Python" Then define a function that prints "I love Python" using the global variable.
language = "Python"

def show():
    print("I love", language)

show()


# Create a global counter like this:  count = 0
# Then write a function increment() that increases the count by 1 using the global keyword. Call the function 3 times and print the final count.
count = 0
def increment():
    global count 
    count += 1

increment()
increment()
increment()

print("Final Count:", count)


# Create a function calculate_area() Inside it, define: length = 5 width = 3 Then calculate and print the area. Make sure these variables are local, not global.
def calculate_area():
  length = 5
  width = 3
  area = length * width
  print("Area:", area)

calculate_area()




