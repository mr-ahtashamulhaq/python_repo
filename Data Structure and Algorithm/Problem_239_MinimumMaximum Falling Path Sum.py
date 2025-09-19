"""Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
"""
from typing import List
class Solution:
    # USING RECURSION  
    def solve(self, row, col, matrix):

        if row >= len(matrix) or col >= len(matrix[0]):
            return float("inf")

        if row < 0 or col < 0:
            return float("inf")

        if row == 0:
            return matrix[row][col]

        down = matrix[row][col] + self.solve(row - 1, col, matrix)
        diagonal_right = matrix[row][col] + self.solve(row - 1, col + 1, matrix)
        diagonal_left = matrix[row][col] + self.solve(row - 1, col - 1, matrix)

        return min(down, diagonal_right, diagonal_left)

    def minFallingPathSum(self, matrix: List[List[int]]):
        n = len(matrix)

        ans = float("inf")
        for i in range(n - 1, -1, -1):
            ans = min(ans, self.solve(n - 1, i, matrix))
        return ans





    # USING MEMOIZATION
    def memoization(self, row, col, matrix, dp):

        if row >= len(matrix) or col >= len(matrix[0]):
            return float("inf")

        if row < 0 or col < 0:
            return float("inf")

        if row == 0:
            return matrix[row][col]

        if dp[row][col] is not None:
            return dp[row][col]

        down = matrix[row][col] + self.memoization(row - 1, col, matrix, dp)
        diagonal_right = matrix[row][col] + self.memoization(
            row - 1, col + 1, matrix, dp
        )
        diagonal_left = matrix[row][col] + self.memoization(
            row - 1, col - 1, matrix, dp
        )

        dp[row][col] = min(down, diagonal_right, diagonal_left)
        return dp[row][col]

    def minFallingPathSum_memo(self, matrix: List[List[int]]):
        n = len(matrix)

        ans = float("inf")
        for i in range(n - 1, -1, -1):
            dp = [[None for _ in range(n)] for _ in range(n)]
            ans = min(ans, self.memoization(n - 1, i, matrix, dp))
        return ans






    # USING TABULATION
    def minFallingPathSum_tabu(self, matrix: List[List[int]]):
        n = len(matrix)
        dp = [[None for _ in range(n)] for _ in range(n)]

        for j in range(n):
            dp[0][j] = matrix[0][j]      #type:ignore

        for i in range(1, n):
            for j in range(0, n):

                up = matrix[i][j] + dp[i - 1][j]      #type:ignore
                if j == 0:
                    left = float("inf")
                else:
                    left = matrix[i][j] + dp[i - 1][j - 1]      #type:ignore

                if j == n - 1:
                    right = float("inf")
                else:
                    right = matrix[i][j] + dp[i - 1][j + 1]      #type:ignore

                dp[i][j] = min(left, up, right)      #type:ignore

        mini = float("inf")
        for j in range(n):
            mini = min(mini, dp[n - 1][j])      #type:ignore
        return mini





    # USING TABULATION WITH SPACE OPTIMIZATION
    def minFallingPathSum_tabuSpaceOpt(self, matrix: List[List[int]]):
        n = len(matrix)

        prev = [None for _ in range(n)]
        for j in range(n):
            prev[j] = matrix[0][j]      #type:ignore

        for i in range(1, n):
            curr = [None] * n
            for j in range(0, n):
       
                if j == 0:
                    left = float("inf")
                else:
                    left = matrix[i][j] + prev[j - 1]      #type:ignore

                up = matrix[i][j] + prev[j]      #type:ignore
    
                if j == n - 1:
                    right = float("inf")
                else:
                    right = matrix[i][j] + prev[j + 1]      #type:ignore
    
                curr[j] = min(left, up, right)      #type:ignore
            prev = curr

        mini = float("inf")
        for j in range(n):
            mini = min(mini, prev[j])      #type:ignore
        return mini


obj = Solution()
matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(obj.minFallingPathSum(matrix))
print(obj.minFallingPathSum_memo(matrix))
print(obj.minFallingPathSum_tabu(matrix))
print(obj.minFallingPathSum_tabuSpaceOpt(matrix))

# Output : 13