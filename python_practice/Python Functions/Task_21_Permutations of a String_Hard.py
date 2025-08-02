"""Given a string s, which may contain duplicate characters, your task is to generate and return an array of all unique permutations of the string. You can return your answer in any order."""

from itertools import permutations

def uniquepermutation(s):
    perm = permutations(s)
    unique = set(perm)
    result = [''.join(p) for p in unique]
    return result

print(uniquepermutation("ABC"))