"""Given two char c1 and c2.  you need to print all the alphabet starting from c1 to c2 in a single line.
Note: Print all characters with a single space after it and all in a single line. Don't add a new line after printing"""

def alphabets(c1,c2):
    for ch in range(ord(c1) , ord(c2)+1):
        print(chr(ch), end=" ")
alphabets("a","z")