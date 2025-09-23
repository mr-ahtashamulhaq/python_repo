"""Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward."""
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

    def minInsertion(self, s: str):
        # Longest Palindromic Subsequence is Longest Common Subsequence of string and its reverse
        text1 = s
        text2 = s[::-1]
        n = len(s)

        LPS = self.recursion(n - 1, n - 1, text1, text2)
        return n - LPS








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

    def minInsertion_memo(self, s: str):
        text1 = s
        text2 = s[::-1]
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        LPS = self.recursion(n - 1, n - 1, text1, text2)
        return n - LPS








    # USING TABULATION
    def minInsertion_tabu(self, s: str):
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

        LPS = dp[n][n]
        return n - LPS





    # USING TABULATION WITH SPACE OPTIMIZATION
    def minInsertion_tabuSpaceOpt(self, s: str):
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
        LPS = prev[n]
        return n - LPS

obj = Solution()
s = "abcde"
print(obj.minInsertion(s))
print(obj.minInsertion_memo(s))
print(obj.minInsertion_tabu(s))
print(obj.minInsertion_tabuSpaceOpt(s))

# Output : 4