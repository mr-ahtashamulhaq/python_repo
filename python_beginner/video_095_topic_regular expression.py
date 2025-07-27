# Find all numbers from the string: "There are 2 apples and 10 bananas"
import re

text = "There are 2 apples and 10 bananas"
numbers = re.findall(r'\d+', text)
print(numbers)

# Check if string starts with "Hello"
text = "Hello world"
if re.match(r'^Hello', text):
    print("Yes, it starts with Hello")
else:
    print("No, it doesn't")

# Replace all spaces in "Hi how are you" with "-"
text = "Hi how are you"
new_text = re.sub(r'\s', '-', text)
print(new_text) 
