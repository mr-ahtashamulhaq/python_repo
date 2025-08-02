"""Given a string s, remove all its adjacent duplicate characters recursively, until there are no adjacent duplicate characters left.
Note: If the resultant string becomes empty, return an empty string."""
#User function Template for python3
def remove_adjacent_duplicates(s):
    i = 0
    new_str = ""
    
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
            i += 1
        else:
            new_str += s[i]
            i += 1

    if new_str != s:
        return remove_adjacent_duplicates(new_str)
    else:
        return new_str

print(remove_adjacent_duplicates("geeksforgeek"))