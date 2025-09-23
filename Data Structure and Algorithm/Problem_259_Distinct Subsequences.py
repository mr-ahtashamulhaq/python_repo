"""Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer."""
class Solution:
    
    # USING RECURSION
    def recursion(self, i, j, text1, text2):
        # base cases
        if j < 0:  # matched all of text2
            return 1
        if i < 0:  # text1 exhausted but text2 not matched
            return 0

        if text1[i] == text2[j]:
            # pick or skip
            return self.recursion(i - 1, j - 1, text1, text2) + self.recursion(
                i - 1, j, text1, text2
            )
        else:
            # must skip
            return self.recursion(i - 1, j, text1, text2)

    def numDistinct(self, text1: str, text2: str):
        n1 = len(text1)
        n2 = len(text2)
        return self.recursion(n1 - 1, n2 - 1, text1, text2)








    # USING MEMOIZATION
    def memoization(self, i, j, text1, text2, dp):
        # base cases
        if j < 0:
            return 1
        if i < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if text1[i] == text2[j]:
            dp[i][j] = self.memoization(
                i - 1, j - 1, text1, text2, dp
            ) + self.memoization(i - 1, j, text1, text2, dp)
        else:
            dp[i][j] = self.memoization(i - 1, j, text1, text2, dp)

        return dp[i][j]

    def numDistinct_memo(self, text1: str, text2: str):
        n1, n2 = len(text1), len(text2)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return self.memoization(n1 - 1, n2 - 1, text1, text2, dp)







    # USING TABULATION
    def numDistinct_tabu(self, text1: str, text2: str):
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        # base case: empty text2
        for i in range(n1 + 1):
            dp[i][0] = 1

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n1][n2]







    # USING TABULATION WITH SPACE OPTIMIZATION
    def numDistinct_tabuSpaceOpt(self, text1: str, text2: str):
        n1, n2 = len(text1), len(text2)
        dp = [0] * (n2 + 1)
        dp[0] = 1 

        for i in range(1, n1 + 1):
            # must go backwards
            for j in range(n2, 0, -1):
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = dp[j - 1] + dp[j]
                # else dp[j] stays same

        return dp[n2]


obj = Solution()
s = "rabbbit"
t = "rabbit"
print(obj.numDistinct(s, t))
print(obj.numDistinct_memo(s, t))
print(obj.numDistinct_tabu(s, t))
print(obj.numDistinct_tabuSpaceOpt(s, t))

#Output : 3 