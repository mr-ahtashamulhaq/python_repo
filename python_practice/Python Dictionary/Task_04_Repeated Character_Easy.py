"""Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

Note - If there are no repeating characters return '#'."""
def first_repeated_char(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch 
        seen.add(ch)
    return '#'


print(first_repeated_char("geeksforgeeks"))