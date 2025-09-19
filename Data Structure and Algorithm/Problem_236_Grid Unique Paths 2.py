"""You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109."""
from typing import List
class Solution:
    # USING RECURSION
    def recursion(self, i, j, grid):
        if i < 0 or j < 0:
            return 0

        if grid[i][j] == 1:
            return 0

        if i == 0 and j == 0:
            if grid[i][j] == 1:
                return 0
            return 1

        up = self.recursion(i - 1, j, grid)
        left = self.recursion(i, j - 1, grid)

        return up + left

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.recursion(m - 1, n - 1, obstacleGrid)





    # USING MEMOIZATION
    def memoization(self, i, j, grid, dp):
        if i < 0 or j < 0:
            return 0

        if grid[i][j] == 1:
            return 0

        if i == 0 and j == 0:
            if grid[i][j] == 1:
                return 0
            return 1

        if dp[i][j] != -1:
            return dp[i][j]

        up = self.memoization(i - 1, j, grid, dp)
        left = self.memoization(i, j - 1, grid, dp)

        dp[i][j] = up + left
        return dp[i][j]

    def uniquePathsWithObstacles_memo(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.memoization(m - 1, n - 1, obstacleGrid, dp)

    
    
    

    

    # USING TABULATION
    def uniquePathsWithObstacles_tabu(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for i in range(0, m):
            for j in range(0, n):

                # Index out of range
                if i == 0 and j == 0:
                    continue

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                if i > 0:
                    up = dp[i - 1][j]
                else:
                    up = 0

                if j > 0:
                    left = dp[i][j - 1]
                else:
                    left = 0

                dp[i][j] = up + left

        return dp[m - 1][n - 1]
    
    
    
    
    
    # USING TABULATION WITH SPACE OPTIMIZATION
    def uniquePathsWithObstacles_tabuSpaceOpt(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        prev = [-1] * n
        for i in range(0, m):
            curr = [-1] * n 
            for j in range(0, n):
                
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                    continue
                
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
            prev = curr.copy()
            
        return prev[n - 1]




obj = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(obj.uniquePathsWithObstacles(obstacleGrid))
print(obj.uniquePathsWithObstacles_memo(obstacleGrid))
print(obj.uniquePathsWithObstacles_tabu(obstacleGrid))
print(obj.uniquePathsWithObstacles_tabuSpaceOpt(obstacleGrid))

# Output : 2