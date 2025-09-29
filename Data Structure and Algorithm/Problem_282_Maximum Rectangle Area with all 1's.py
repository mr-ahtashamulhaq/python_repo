"""Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area."""

from typing import List


class Solution:
    def oneRow(self, row: List[int]) -> int:
        maxArea = 0
        stack = []  # index , height
        n = len(row)
        for i, h in enumerate(row):
            start = i
            while stack and stack[-1][1] > h:

                index, height = stack.pop()

                maxArea = max(maxArea, (height * (i - index)))
                start = index

            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(row) - i))

        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        cols = len(matrix[0])
        result = 0
        row = [0] * cols
        for r in matrix:
            for j in range(cols):
                row[j] = 0 if r[j] == "0" else 1 + row[j]

            result = max(result, self.oneRow(row))

        return result


obj = Solution()
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(obj.maximalRectangle(matrix))

# Output : 6
