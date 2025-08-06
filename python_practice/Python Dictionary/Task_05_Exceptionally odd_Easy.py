"""Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

Not - If there are no repeating characters return '#'."""
def find_odd_occurrence(arr):
    for num in arr:
        if arr.count(num) % 2 != 0:
            return num
    return None
        

print(find_odd_occurrence([1, 2, 3, 2, 3, 1, 3]))  # 3