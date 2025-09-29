"""
You are given a string `s`. Your task is to count the number of **distinct substrings** 
that can be formed from it.

Note:
- The empty substring is also counted as one.
- Substring = a contiguous block of characters within the string.
"""

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}

    class Trie:
        def __init__(self):
            self.root = Solution.TrieNode()

        def insert_and_count(self, word: str) -> int:
            node = self.root
            count_new_nodes = 0
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Solution.TrieNode()
                    count_new_nodes += 1
                node = node.children[ch]
            return count_new_nodes

    def countDistinctSubstrings(self, s: str) -> int:
        trie = self.Trie()
        result = 0

        # Insert all suffixes
        for i in range(len(s)):
            suffix = s[i:]
            result += trie.insert_and_count(suffix)

        # +1 for empty substring
        return result + 1



obj = Solution()
print(obj.countDistinctSubstrings("ab"))    
print(obj.countDistinctSubstrings("aaa")) 
print(obj.countDistinctSubstrings("abc"))

# Output :
#         4
#         4
#         7