"""Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row."""
from typing import List
class Solution:
    # USING RECURSION
    def solve(self, row, col, triangle):
        if row == len(triangle) - 1:
            return triangle[row][col]

        down = triangle[row][col] + self.solve(row + 1, col, triangle)
        diagonal = triangle[row][col] + self.solve(row + 1, col + 1, triangle)

        return min(down, diagonal)

    def minimumTotal(self, triangle: List[List[int]]) -> int:

        return self.solve(0, 0, triangle)





    # USING MEMOIZATION
    def memoization(self, row, col, triangle, dp):
        if row == len(triangle) - 1:
            return triangle[row][col]

        if dp[row][col] is not None:
            return dp[row][col]

        down = triangle[row][col] + self.memoization(row + 1, col, triangle, dp)
        diagonal = triangle[row][col] + self.memoization(row + 1, col + 1, triangle, dp)

        dp[row][col] = min(down, diagonal)
        return dp[row][col]

    def minimumTotal_memo(self, triangle):
        n = len(triangle)
        dp = [[None] * n for i in range(1, n + 1)]

        return self.memoization(0, 0, triangle, dp)





    # USING TABULATION
    def minimumTotal_tabu(self, triangle):
        n = len(triangle)
        dp = [[None] * n for i in range(1, n + 1)]

        for j in range(0, n):
            dp[n - 1][j] = triangle[n - 1][j]

        for i in range(n - 2, -1, -1):
            for j in range(i, -1, -1):
                down = triangle[i][j] + dp[i + 1][j]
                diagonal = triangle[i][j] + dp[i + 1][j + 1]

                dp[i][j] = min(down, diagonal)

        return dp[0][0]





    # USING TABULATION WITH SPACE OPTIMIZATION
    def minimumTotal_tabuSpaceOpt(self, triangle):
        n = len(triangle)
        prev = [None] * n
        for j in range(0, n):
            prev[j] = triangle[n - 1][j]

        for i in range(n - 2, -1, -1):
            curr = [None] * n
            for j in range(i, -1, -1):
                down = triangle[i][j] + prev[j]
                diagonal = triangle[i][j] + prev[j + 1]

                curr[j] = min(down, diagonal)
            
            prev = curr.copy()

        return prev[0]


obj = Solution()
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(obj.minimumTotal(triangle))
print(obj.minimumTotal_memo(triangle))
print(obj.minimumTotal_tabu(triangle))
print(obj.minimumTotal_tabuSpaceOpt(triangle))

# Output : 11