"""You are given two strings s1 and s2. Your task is to print the  longest common subsequences.

Note: A subsequence is derived from another string by deleting some or none of the elements without changing the order of the remaining elements."""
class Solution:
    
    #USING RECURSION
    def recursion(self, ind1, ind2, text1, text2):
        if ind1 < 0 or ind2 < 0:
            return ""

        if text1[ind1] == text2[ind2]:
            return self.recursion(ind1 - 1, ind2 - 1, text1, text2) + text1[ind1]
        else:
            left = self.recursion(ind1 - 1, ind2, text1, text2)
            right = self.recursion(ind1, ind2 - 1, text1, text2)
            return left if len(left) >= len(right) else right

    def LCS(self, text1, text2):
        n1 = len(text1)
        n2 = len(text2)
        return self.recursion(n1 - 1, n2 - 1, text1, text2)







    #USING MEMOIZATION
    def memoization(self, ind1, ind2, text1, text2, dp):
        if ind1 < 0 or ind2 < 0:
            return ""

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        if text1[ind1] == text2[ind2]:
            dp[ind1][ind2] = self.memoization(ind1 - 1, ind2 - 1, text1, text2, dp) + text1[ind1]
        else:
            left = self.memoization(ind1 - 1, ind2, text1, text2, dp)
            right = self.memoization(ind1, ind2 - 1, text1, text2, dp)
            dp[ind1][ind2] = left if len(left) >= len(right) else right

        return dp[ind1][ind2]

    def LCS_memo(self, text1, text2):
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return self.memoization(n1 - 1, n2 - 1, text1, text2, dp)







    #USING TABULATION
    def LCS_tabu(self, text1, text2):
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

        i, j = n1, n2
        result = []
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                result.append(text1[i - 1])
                i -= 1
                j -= 1
            else:
                if dp[i][j - 1] >= dp[i - 1][j]:
                    j -= 1
                else:
                    i -= 1

        result.reverse()
        return "".join(result)







    #USING TABULATION WITH SPACE OPTIMIZATION
    def LCS_tabuSpaceOpt(self, text1, text2):
        n1 = len(text1)
        n2 = len(text2)
        prev = [0 for _ in range(n2 + 1)]
        path = [["" for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for ind1 in range(1, n1 + 1):
            curr = [0 for _ in range(n2 + 1)]
            for ind2 in range(1, n2 + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    curr[ind2] = 1 + prev[ind2 - 1]
                    path[ind1][ind2] = path[ind1 - 1][ind2 - 1] + text1[ind1 - 1]
                else:
                    if prev[ind2] >= curr[ind2 - 1]:
                        curr[ind2] = prev[ind2]
                        path[ind1][ind2] = path[ind1 - 1][ind2]
                    else:
                        curr[ind2] = curr[ind2 - 1]
                        path[ind1][ind2] = path[ind1][ind2 - 1]
            prev = curr.copy()
        return path[n1][n2]



obj = Solution()
text1 = "abcde"
text2 = "ace"
print(obj.LCS(text1, text2))
print(obj.LCS_memo(text1, text2))
print(obj.LCS_tabu(text1, text2))
print(obj.LCS_tabuSpaceOpt(text1, text2))

# Output : ace