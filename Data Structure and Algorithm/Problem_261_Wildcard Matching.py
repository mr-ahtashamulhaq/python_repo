"""Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial)."""
class Solution:
    # USING RECURSION
    def recursion(self, i, j, text1, text2):
        if i < 0 and j < 0:   # both exhausted
            return True
        if i >= 0 and j < 0:  # pattern exhausted but string not
            return False
        if i < 0 and j >= 0:  # string exhausted, pattern left
            for k in range(j + 1):
                if text2[k] != "*":
                    return False
            return True

        if text2[j] == text1[i] or text2[j] == "?":
            return self.recursion(i-1, j-1, text1, text2)
        elif text2[j] == "*":
            return self.recursion(i-1, j, text1, text2) or self.recursion(i, j-1, text1, text2)
        else:
            return False

    def isMatch(self, s: str, p: str) -> bool:
        return self.recursion(len(s)-1, len(p)-1, s, p)






    # USING MEMOIZATION
    def memoization(self, i, j, text1, text2, dp):
        if i < 0 and j < 0:
            return True
        if i >= 0 and j < 0:
            return False
        if i < 0 and j >= 0:
            for k in range(j + 1):
                if text2[k] != "*":
                    return False
            return True

        if dp[i][j] != -1:
            return dp[i][j]

        if text2[j] == text1[i] or text2[j] == "?":
            dp[i][j] = self.memoization(i-1, j-1, text1, text2, dp)
        elif text2[j] == "*":
            dp[i][j] = self.memoization(i-1, j, text1, text2, dp) or self.memoization(i, j-1, text1, text2, dp)
        else:
            dp[i][j] = False

        return dp[i][j]

    def isMatch_memo(self, s: str, p: str) -> bool:
        n1, n2 = len(s), len(p)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return self.memoization(n1-1, n2-1, s, p, dp)






    # USING TABULATION
    def isMatch_tabu(self, s: str, p: str) -> bool:
        n1, n2 = len(s), len(p)
        dp = [[False] * (n1 + 1) for _ in range(n2 + 1)]

        # Base cases
        dp[0][0] = True
        for j in range(1, n1 + 1):
            dp[0][j] = False
        for i in range(1, n2 + 1):
            dp[i][0] = all(p[k] == "*" for k in range(i))

        # Fill dp
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if p[i-1] == s[j-1] or p[i-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False

        return dp[n2][n1]






    # USING TABULATION WITH SPACE OPTIMIZATION
    def isMatch_tabuSpaceOpt(self, s: str, p: str) -> bool:
        n1, n2 = len(s), len(p)
        prev = [False] * (n1 + 1)
        prev[0] = True

        for i in range(1, n2 + 1):
            cur = [False] * (n1 + 1)
            cur[0] = all(p[k] == "*" for k in range(i))

            for j in range(1, n1 + 1):
                if p[i-1] == s[j-1] or p[i-1] == "?":
                    cur[j] = prev[j-1]
                elif p[i-1] == "*":
                    cur[j] = prev[j] or cur[j-1]
                else:
                    cur[j] = False

            prev = cur

        return prev[n1]



obj = Solution()
s = "aa"
p = "*"
print(obj.isMatch(s, p))             
print(obj.isMatch_memo(s, p))        
print(obj.isMatch_tabu(s, p))        
print(obj.isMatch_tabuSpaceOpt(s, p))
