"""You are given two strings s1 and s2. Your task is to find the length of the longest common substring among the given strings."""
class Solution:
    
    
    #USING RECURSION
    def recursion(self, ind1, ind2, text1, text2, count):
        if ind1 < 0 or ind2 < 0:
            return count

        if text1[ind1] == text2[ind2]:
            count = self.recursion(ind1 - 1, ind2 - 1, text1, text2, count + 1)

        option1 = self.recursion(ind1 - 1, ind2, text1, text2, 0)
        option2 = self.recursion(ind1, ind2 - 1, text1, text2, 0)

        return max(count, option1, option2)

    def longestCommonSubstr(self, text1, text2):
        n1 = len(text1)
        n2 = len(text2)
        return self.recursion(n1 - 1, n2 - 1, text1, text2, 0)







    #USING MEMOIZATION
    def memoization(self, ind1, ind2, text1, text2, dp, count):
        if ind1 < 0 or ind2 < 0:
            return count

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        new_count = count
        if text1[ind1] == text2[ind2]:
            new_count = self.memoization(ind1 - 1, ind2 - 1, text1, text2, dp, count + 1)

        option1 = self.memoization(ind1 - 1, ind2, text1, text2, dp, 0)
        option2 = self.memoization(ind1, ind2 - 1, text1, text2, dp, 0)

        dp[ind1][ind2] = max(new_count, option1, option2)
        return dp[ind1][ind2]

    def longestCommonSubstr_memo(self, text1, text2):
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return self.memoization(n1 - 1, n2 - 1, text1, text2, dp, 0)







    #USING TABULATION
    def longestCommonSubstr_tabu(self, text1, text2):

        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for ind1 in range(n1 + 1):
            dp[ind1][0] = 0
        for ind2 in range(n2 + 1):
            dp[0][ind2] = 0
        maxi = 0
        for ind1 in range(1, n1 + 1):
            for ind2 in range(1, n2 + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                    maxi = max(maxi, dp[ind1][ind2])
                else:
                    dp[ind1][ind2] = 0

        return maxi







    #USING TABULATION WITH SPACE OPTIMIZATION
    def longestCommonSubstr_tabuSpaceOpt(self, text1, text2):

        n1 = len(text1)
        n2 = len(text2)
        prev = [0 for _ in range(n2 + 1)]
        maxi = 0

        for ind1 in range(1, n1 + 1):
            curr = [0 for _ in range(n2 + 1)]
            for ind2 in range(1, n2 + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    curr[ind2] = 1 + prev[ind2 - 1]
                    maxi = max(maxi, curr[ind2])
                else:
                    curr[ind2] = 0
            prev = curr.copy()

        return maxi

    
obj = Solution()

text1 = "abcde"
text2 = "ace"
print(obj.longestCommonSubstr(text1, text2))
print(obj.longestCommonSubstr_memo(text1, text2))
print(obj.longestCommonSubstr_tabu(text1, text2))
print(obj.longestCommonSubstr_tabuSpaceOpt(text1, text2))

# Output : 1