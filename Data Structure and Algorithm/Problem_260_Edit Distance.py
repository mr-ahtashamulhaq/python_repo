"""Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character
"""
class Solution:
    # USING RECURSION
    def recursion(self, i, j, text1, text2):
        if i < 0:  # text1 exhausted
            return j + 1  # need to insert all remaining chars of text2
        
        
        if j < 0:  # text2 exhausted
            return i + 1  # need to delete all remaining chars of text1


        if text1[i] == text2[j]:
            return self.recursion(i-1, j-1, text1, text2)
        else:
            # 1 operation will happen + which one return minimum
            
            insert = 1 + self.recursion(i, j-1, text1, text2)   # insert
            delete = 1 + self.recursion(i-1, j, text1, text2)   # delete
            replace = 1 + self.recursion(i-1, j-1, text1, text2) # replace
            return min(insert, delete, replace)

    def editDistance(self, word1: str, word2: str) -> int:
        return self.recursion(len(word1)-1, len(word2)-1, word1, word2)
    
    
    
    
    
    

    # USING MEMOIZATION
    def memoization(self, i, j, text1, text2, dp):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if dp[i][j] != -1:
            return dp[i][j]

        if text1[i] == text2[j]:
            dp[i][j] = self.memoization(i-1, j-1, text1, text2, dp)
        else:
            insert = 1 + self.memoization(i, j-1, text1, text2, dp)
            delete = 1 + self.memoization(i-1, j, text1, text2, dp)
            replace = 1 + self.memoization(i-1, j-1, text1, text2, dp)
            dp[i][j] = min(insert, delete, replace)

        return dp[i][j]

    def editDistance_memo(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return self.memoization(n1-1, n2-1, word1, word2, dp)







    # USING TABULATION
    def editDistance_tabu(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

        return dp[n1][n2]








    # USING TABULATION WITH SPACE OPTIMIZATION
    def editDistance_tabuSpaceOpt(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        prev = [j for j in range(n2 + 1)]

        for i in range(1, n1 + 1):
            curr = [0] * (n2 + 1)
            curr[0] = i
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(curr[j-1], prev[j], prev[j-1])
            prev = curr

        return prev[n2]
    

obj = Solution()
word1 = "horse"
word2 = "ros"
print(obj.editDistance(word1, word2))
print(obj.editDistance_memo(word1, word2))
print(obj.editDistance_tabu(word1, word2))
print(obj.editDistance_tabuSpaceOpt(word1, word2))

# Output : 3