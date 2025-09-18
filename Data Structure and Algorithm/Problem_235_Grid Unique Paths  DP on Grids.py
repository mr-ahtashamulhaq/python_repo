"""There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10**9."""

class Solution:
    #USING RECURSION
    def recursion(self, i, j):
        if i == 0 and j == 0:
            return 1

        if i < 0 or j < 0:
            return 0

        up = self.recursion(i - 1, j)
        left = self.recursion(i, j - 1)

        return up + left

    def uniquePaths(self, m: int, n: int) -> int:

        return self.recursion(m - 1, n - 1)




    #USING MEMOIZATION
    def memoization(self, i, j, dp):
        if i == 0 and j == 0:
            return 1

        if i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        up = self.memoization(i - 1, j, dp)
        left = self.memoization(i, j - 1, dp)

        dp[i][j] = up + left
        return dp[i][j]

    def uniquePaths_memo(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.memoization(m - 1, n - 1, dp)





    #USING TABULATION
    def uniquePaths_tabu(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        dp[0][0] = 1
        
        for i in range(0, m):
            for j in range(0, n):
                
                # Index out of range
                if i ==0 and j==0:
                    continue
                
                if i>0:
                    up = dp[i-1][j]
                else:
                    up = 0
                
                
                if j > 0:
                    left = dp[i][j-1]
                else:
                    left = 0
                
                dp[i][j] = up+left
                
        return dp[m-1][n-1]
    
    
    
    
    #USING TABULATION WITH SPACE OPTIMIZATION
    def uniquePaths_tabuSpaceOpt(self, m: int, n: int) -> int:
        prev = [-1] * n
        for i in range(0, m):
            curr = [-1] * n 
            for j in range(0, n):
                if i == 0 and j == 0:
                    curr[0] = 1  
                    continue
                
                if i == 0:
                    up = 0
                else:
                    up = prev[j]
               
                if j == 0:
                    left = 0
                else:
                    left = curr[j - 1]
                curr[j] = up + left
            prev = curr 
            
        return prev[n - 1]
    
    
obj = Solution()
print(obj.uniquePaths(3,7))
print(obj.uniquePaths_memo(3,7))
print(obj.uniquePaths_tabu(3,7))
print(obj.uniquePaths_tabuSpaceOpt(3,7))

# Output : 28