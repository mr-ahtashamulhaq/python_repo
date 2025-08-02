"""Given a pair of strings s1 and s2 of equal lengths, your task is to find which of the two strings has more distinct subsequences. If both strings have the same number of distinct subsequences, return s1."""
class Solution:
    def getDistinctSubsequences(self, s):
        n = len(s)
        subsequences = set()

        for i in range(2 ** n):
            subseq = ""
            for j in range(n):
                if (i >> j) & 1:
                    subseq += s[j]

            subsequences.add(subseq)
        return subsequences

    def betterString(self, s1, s2):
        set1 = self.getDistinctSubsequences(s1)
        set2 = self.getDistinctSubsequences(s2)

        if len(set1) >= len(set2):
            return s1
        else:
            return s2

obj = Solution()
print(obj.betterString("gfg", "ggg"))
