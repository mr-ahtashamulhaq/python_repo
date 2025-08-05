"""Given a string s, and a pattern p. You need to find if p exists in s or not and return the starting index of p in s. If p does not exist in s then -1 will be returned.
Here p and s both are case-sensitive."""
def findPattern(s : str,p):
    return s.find(p)

print(findPattern("hello", "llo"))