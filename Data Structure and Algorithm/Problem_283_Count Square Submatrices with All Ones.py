"""Given a m * n matrix of ones and zeros, return how many square submatrices have all ones."""
from typing import List, Optional
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        cnt = matrix[0].count(1)
        for i in range(1, r):
            cnt += matrix[i][0]
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1])
                cnt += matrix[i][j]
        return cnt


obj = Solution()
matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
print(obj.countSquares(matrix))

# Output : 15