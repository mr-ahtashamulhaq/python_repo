"""Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string."""
class Solution:
    #USING RECURSION
    def recursion(self, ind1, ind2, text1, text2):
        if ind1 < 0 or ind2 < 0:
            return 0
        
        if text1[ind1] == text2[ind2]:
            return 1 + self.recursion(ind1-1 , ind2-1, text1, text2)
        else:
            return 0 + max( self.recursion(ind1-1, ind2, text1, text2) , self.recursion(ind1, ind2-1, text1, text2))
        
    def minDistance(self, word1: str, word2: str) -> int:

        n1 = len(word1)
        n2 = len(word2)
        
        LCS = self.recursion(n1-1, n2-1, word1, word2)

        return (n1 - LCS) + (n2-LCS)
    
    
    
    
    

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

    def minDistance_memo(self, text1: str, text2: str):
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        LCS = self.memoization(n1 - 1, n2 - 1, text1, text2, dp)
        return (n1 - LCS) + (n2 - LCS)
    
    
    
    
    
    
    
    #USING TABULATION
    def minDistance_tabu(self, text1: str, text2: str):
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

        return (n1 - dp[n1][n2]) + (n2 - dp[n1][n2])
    
    
    
    
    
    
    
    
    #USING TABULATION WITH SPACE OPTIMIZATION
    def minDistance_tabuSpaceOpt(self, text1: str, text2: str):
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
        return (n1 - prev[n2]) + (n2 - prev[n2])
    
    
obj = Solution()
word1 = "leetcode"
word2 = "etco"

print(obj.minDistance(word1, word2))
print(obj.minDistance_memo(word1, word2))
print(obj.minDistance_tabu(word1, word2))
print(obj.minDistance_tabuSpaceOpt(word1, word2))

# Output : 4