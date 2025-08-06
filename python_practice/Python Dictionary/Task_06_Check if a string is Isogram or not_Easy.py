"""Given a string s of lowercase alphabets, You have to check that  it is isogram or not.
An Isogram is a string in which no letter occurs more than once."""
def is_isogram(s):
    return len(set(s)) == len(s)


print(is_isogram("machine")) 
print(is_isogram("hello"))