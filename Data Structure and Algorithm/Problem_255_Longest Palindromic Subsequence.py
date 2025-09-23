"""Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""
class Solution:
    # USING RECURSION
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

    def LPS(self, s: str):
        # Longest Palindromic Subsequence is Longest Common Subsequence of string and its reverse
        text1 = s
        text2 = s[::-1]
        n = len(s)

        return self.recursion(n - 1, n - 1, text1, text2)








    # USING MEMOIZATION
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

    def LPS_memo(self, s):
        text1 = s
        text2 = s[::-1]
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.memoization(n - 1, n - 1, text1, text2, dp)








    # USING TABULATION
    def LPS_tabu(self, s):
        text1 = s
        text2 = s[::-1]
        n = len(s)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        for ind1 in range(n + 1):
            dp[ind1][0] = 0
        for ind2 in range(n + 1):
            dp[0][ind2] = 0

        for ind1 in range(1, n + 1):
            for ind2 in range(1, n + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = 0 + max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        return dp[n][n]





    # USING TABULATION WITH SPACE OPTIMIZATION
    def LPS_tabuSpaceOpt(self, s):
        text1 = s
        text2 = s[::-1]
        n = len(s)
        prev = [-1 for _ in range(n + 1)]

        for ind2 in range(n + 1):
            prev[ind2] = 0

        for ind1 in range(1, n + 1):
            curr = [-1 for _ in range(n + 1)]
            curr[0] = 0  # everytime make new row its first will be zero
            for ind2 in range(1, n + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    curr[ind2] = 1 + prev[ind2 - 1]
                else:
                    curr[ind2] = 0 + max(prev[ind2], curr[ind2 - 1])

            prev = curr.copy()
        return prev[n]


obj = Solution()
print(obj.LPS("bbbab"))
print(obj.LPS_memo("bbbab"))
print(obj.LPS_tabu("bbbab"))
print(obj.LPS_tabuSpaceOpt("bbbab"))

# Output : 4