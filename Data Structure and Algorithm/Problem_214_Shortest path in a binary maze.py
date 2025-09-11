"""Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path."""
from typing import List, Optional
import sys
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Blocked start means no path
        if grid[0][0] == 1:
            return -1

        rows = len(grid)
        cols = len(grid[0])

        # distance matrix – start cell has distance 1
        distance = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        distance[0][0] = 1

        queue = deque()
        queue.append([1, 0, 0])        # [current_dist, row, col]

        while queue:
            dist, i, j = queue.popleft()

            # 8 possible moves
            for x, y in [
                [1, 0],   [0, -1],  [-1, 0],  [0, 1],
                [-1, -1], [-1, 1],  [1, 1],   [1, -1],
            ]:
                new_i, new_j = i + x, j + y

                # skip if out of bounds
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                # skip if blocked
                if grid[new_i][new_j] == 1:
                    continue

                new_dist = dist + 1
                # relax distance
                if new_dist < distance[new_i][new_j]:
                    # if we reached the goal, return immediately
                    if new_i == rows - 1 and new_j == cols - 1:
                        return new_dist
                    distance[new_i][new_j] = new_dist
                    queue.append([new_dist, new_i, new_j])

        # If end cell still at ∞, no path exists
        return -1 if distance[rows - 1][cols - 1] == sys.maxsize else distance[rows - 1][cols - 1]
obj = Solution()
grid = [[0,0,0],[1,1,0],[1,1,0]]
print( obj.shortestPathBinaryMatrix(grid) )

# Output : 4