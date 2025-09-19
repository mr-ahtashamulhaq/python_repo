"""Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time."""
class Solution:
    #USING RECURSION
    def recursion(self, i, j, grid):
        if i == 0 and j == 0:
            return grid[i][j]

        if i < 0 or j < 0:
            return float("inf")

        up = self.recursion(i - 1, j, grid)
        left = self.recursion(i, j - 1, grid)

        return grid[i][j] + min(up, left)

    def minPathSum(self,grid):
        m = len(grid)
        n = len(grid[0])
        return self.recursion(m - 1, n - 1 , grid)
    
    
    
    
    
    
    #USING MEMOIZATION
    def memoization(self, i, j, grid, dp):
        if i == 0 and j == 0:
            return grid[i][j]

        if i < 0 or j < 0:
            return float("inf")
        
        if dp[i][j] != -1:
            return dp[i][j]

        up = self.memoization(i - 1, j, grid, dp)
        left = self.memoization(i, j - 1, grid, dp)

        dp[i][j] = grid[i][j] + min(up, left)
        return dp[i][j]

    def minPathSum_memo(self,grid):
        m = len(grid)
        n = len(grid[0])
        dp= [[-1 for _ in range(n)] for _ in range(m)]
        return self.memoization(m - 1, n - 1 , grid, dp)
    
    
    
    
    
    #USING TABULATION
    def minPathSum_tabu(self,grid):
        m = len(grid)
        n = len(grid[0])
        dp= [[-1 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(0 , m):
            for j in range(0, n):
                
                if i == 0 and j == 0:
                    continue
                
                if i > 0:
                    up = dp[i-1][j]
                else:
                    up = float("inf")
                    
                if j>0:
                    left = dp[i][j-1]
                else:
                    left = float("inf")
                    
                dp[i][j] = min(up, left) + grid[i][j]
        
        return dp[m-1][n-1]
        
    
    
    
    
    
    #USING TABULATION WITH SPACE OPTIMIZATION    
    def minPathSum_tabuSpaceOpt(self,grid):
        m = len(grid)
        n = len(grid[0])
        
        prev = [-1] * n        
        for i in range(0 , m):
            curr = [-1] * n
            for j in range(0, n):
                
                if i == 0 and j == 0:
                    curr[j] = grid[i][j]
                    continue
                
                if i > 0:
                    up = prev[j]
                else:
                    up = float("inf")
                    
                if j>0:
                    left = curr[j-1]
                else:
                    left = float("inf")
                    
                curr[j] = min(up, left) + grid[i][j]
                
            prev = curr.copy()
        
        return prev[n-1]
        
        
        
obj = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(obj.minPathSum(grid))
print(obj.minPathSum_memo(grid))
print(obj.minPathSum_tabu(grid))
print(obj.minPathSum_tabuSpaceOpt(grid))

# Output : 7