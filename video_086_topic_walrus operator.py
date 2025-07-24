# Use the walrus operator to get the length of a string "Python" and check if it's greater than 4.
if (length := len("Python")) > 4:
    print(f"Length is {length}")  # Output: Length is 6

# Ask the user to enter a number. If it’s greater than 10, print "Big number".
if (num := int(input("Enter a number: "))) > 10:
    print("Big number")

# Keep asking for input until the user types "exit", print each input using walrus operator.
while (text := input("Type something (or 'exit' to quit): ")) != "exit":
    print(f"You typed: {text}")

# Use the walrus operator to assign and immediately print the square of 7.
print(sq := 7 ** 2)  # Output: 49

# Check if the number of vowels in "programming" is more than 3 using walrus.
vowels = "aeiou"
if (count := sum(1 for c in "programming" if c in vowels)) > 3:
    print(f"Vowels found: {count}")
