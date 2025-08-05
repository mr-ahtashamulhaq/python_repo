"""Given a string s, you need to slice it so that the output is a substring that contains all the characters except the first and last"""
def sliceString(s):
    return s[1:-1]
print(sliceString("hello"))