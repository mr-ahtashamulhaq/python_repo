"""Given a string s consisting of lowercase english alphabets, the task is to find the number of distinct subsequences of the string"""
from itertools import combinations

class Solution:
    def distinctSubsequences(self, s):
        subs = set()
        for length in range(len(s) + 1):
            for combo in combinations(s, length):
                subs.add("".join(combo))
        if "" in subs:
            subs.remove("")
        return len(subs)

obj = Solution()
print(obj.distinctSubsequences("gfg"))