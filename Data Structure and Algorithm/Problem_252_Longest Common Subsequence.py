"""Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings."""

class Solution:
    #USING RECURSION
    def recursion(self, ind1, ind2, text1, text2):
        if ind1 < 0 or ind2 < 0:
            return 0

        if text1[ind1] == text2[ind2]:
            return 1 + self.recursion(ind1 - 1, ind2 - 1, text1, text2)

        else:
            return 0 + max(
                self.recursion(ind1 - 1, ind2, text1, text2),
                self.recursion(ind1, ind2 - 1, text1, text2),
            )

    def LCS(self, text1: str, text2: str):
        n1 = len(text1)
        n2 = len(text2)

        return self.recursion(n1 - 1, n2 - 1, text1, text2)






    #USING MEMOIZATION
    def memoization(self, ind1, ind2, text1, text2, dp):
        if ind1 < 0 or ind2 < 0:
            return 0

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        if text1[ind1] == text2[ind2]:
            dp[ind1][ind2] = 1 + self.memoization(ind1 - 1, ind2 - 1, text1, text2, dp)
            return dp[ind1][ind2]
        else:
            dp[ind1][ind2] = 0 + max(
                self.memoization(ind1 - 1, ind2, text1, text2, dp),
                self.memoization(ind1, ind2 - 1, text1, text2, dp),
            )
            return dp[ind1][ind2]

    def LCS_memo(self, text1: str, text2: str):
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return self.memoization(n1 - 1, n2 - 1, text1, text2, dp)







    #USING TABULATION
    def LCS_tabu(self, text1: str, text2: str):
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for ind1 in range(n1 + 1):
            dp[ind1][0] = 0
        for ind2 in range(n2 + 1):
            dp[0][ind2] = 0

        for ind1 in range(1, n1 + 1):
            for ind2 in range(1, n2 + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = 0 + max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        return dp[n1][n2]







    #USING TABULATION WITH SPACE OPTIMIZATION
    def LCS_tabuSpaceOpt(self, text1: str, text2: str):
        n1 = len(text1)
        n2 = len(text2)
        prev = [-1 for _ in range(n2 + 1)]

        for ind2 in range(n2 + 1):
            prev[ind2] = 0

        for ind1 in range(1, n1 + 1):
            curr = [-1 for _ in range(n2 + 1)]
            curr[0] = 0                  # everytime make new row its first will be zero
            for ind2 in range(1, n2 + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    curr[ind2] = 1 + prev[ind2 - 1]
                else:
                    curr[ind2] = 0 + max(prev[ind2], curr[ind2 - 1])

            prev = curr.copy()
        return prev[n2]



obj = Solution()
text1 = "abce"
text2 = "ace"
print(obj.LCS(text1, text2))
print(obj.LCS_memo(text1, text2))
print(obj.LCS_tabu(text1, text2))
print(obj.LCS_tabuSpaceOpt(text1, text2))