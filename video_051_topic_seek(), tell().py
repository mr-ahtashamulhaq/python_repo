# Open a file, read 5 bytes, print current position using tell().

with open("seek_tell1.txt", "w") as f:
    f.write("Hello, Python file handling!")

with open("seek_tell1.txt", "r") as f:
    data = f.read(5)
    print("Data read:", data)
    print("Current position using tell():", f.tell())



# Use seek() to move to the 7th byte and read the next 5 bytes.

with open("seek_tell2.txt", "w") as f:
    f.write("Learning Python file seek and tell functions.")

with open("seek_tell2.txt", "r") as f:
    f.seek(6)  # Move to the 7th byte
    data = f.read(5)
    print("Data after seek to 7th byte:", data)



# Use seek() with whence=1 to move 3 bytes forward from current position.

with open("seek_tell3.txt", "w") as f:
    f.write("Seek from current position example.")

with open("seek_tell3.txt", "r") as f:
    f.read(5)                # Move to 5
    f.seek(3, 1)             # Move 3 bytes ahead from current (5+3=8)
    data = f.read(5)         # Read 5 bytes from position 8
    print("Data after seek(3,1):", data)



#  Create a file and truncate it to 10 bytes, then print the content to see the effect.

with open("truncate4.txt", "w") as f:
    f.write("Python truncate example test data.")

with open("truncate4.txt", "r+") as f:
    f.truncate(10)           # Cut the file size to 10 bytes

with open("truncate4.txt", "r") as f:
    content = f.read()
    print("Content after truncate to 10 bytes:", content)



# Write a program that reads a file, prints current position using tell(), moves to the 4th byte using seek(), prints position, then truncates the file at current position.

with open("seek_tell_truncate5.txt", "w") as f:
    f.write("File handling practice with seek, tell, truncate.")

with open("seek_tell_truncate5.txt", "r+") as f:
    print("Initial position:", f.tell())         # Should be 0
    f.seek(4)                                    # Move to 4th byte
    print("Position after seek(4):", f.tell())   # Should be 4
    f.truncate()                                 # Truncate at current position (4)

with open("seek_tell_truncate5.txt", "r") as f:
    content = f.read()
    print("Content after truncating at position 4:", content)