"""
You are given an array of strings. Your task is to find the longest string 
such that **all its prefixes** are also present in the array.

- If there are multiple answers, return the lexicographically smallest one.
- If no such string exists, return "None".
"""
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def check_all_prefix(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            if not node.is_end:  # prefix missing
                return False
        return True

def completeString(n: int, a: List[str]) -> str:
    trie = Trie()
    for word in a:
        trie.insert(word)

    best_word = "" 
    for word in a:
        if trie.check_all_prefix(word):
            if len(word) > len(best_word) or (len(word) == len(best_word) and word < best_word):
                best_word = word

    return best_word if best_word != "" else "None"




words1 = ["n", "ni", "nin", "ninj", "ninja", "ninga"]
words2 = ["ab", "abc", "abcd", "xyz"]

print(completeString(len(words1), words1)) 
print(completeString(len(words2), words2)) 

# Output :
# ninja
# None
