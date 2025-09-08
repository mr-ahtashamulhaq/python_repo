"""Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water."""

from typing import List, Optional
from collections import deque
class Solution:

    """BFS-Algo to solve problem"""
    def bfs_algo(self, i, j, visited, grid):
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        queue.append((i , j))
        visited[i][j] =1

        while queue:
            r, c = queue.popleft()

            for x , y in [(0,-1), (0, 1), (1, 0), (-1, 0)]:
                new_r = r+x
                new_c = c + y

                if new_r < 0 or new_c <0 or new_r >=rows or new_c >= cols:
                    continue
                if grid[new_r][new_c] == "0":
                    continue
                if visited[new_r][new_c]==1:
                    continue
                visited[new_r][new_c] = 1
                queue.append((new_r, new_c))


    """DFS-Algo to solve problem"""
    def dfs_algo(self, r, c, visited, grid):
        rows = len(grid)
        cols = len(grid[0])
        if r<0 or c <0 or r>=rows or c >= cols:
            return
        if grid[r][c] == "0":
            return
        if visited[r][c] == 1:
            return

        visited[r][c] = 1
        self.dfs_algo(r+1, c, visited, grid)
        self.dfs_algo(r-1, c, visited, grid)
        self.dfs_algo(r, c+1, visited, grid)
        self.dfs_algo(r, c-1, visited, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and visited [r][c]==0:
                    count +=1
                    self.dfs_algo(r, c, visited, grid)

        return count
obj = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
print(obj.numIslands(grid))

# Output : Using BFS --> 3 and Using DFS --> 3