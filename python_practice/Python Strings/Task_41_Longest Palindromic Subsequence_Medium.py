"""Given a string s, return the length of the longest palindromic subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements."""
class Solution:
    def longestPalinSubseq(self, s):
        n = len(s)
        rev = s[::-1] 

        table = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])
        
        return table[n][n]
obj = Solution()
print(obj.longestPalinSubseq("bbabcbcab"))