"""Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected)."""
import sys
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, r, c, base_r, base_c, shape, visited, rows, cols, grid):
        visited[r][c] = 1
        shape.append((r - base_r, c - base_c))
        
        # four possible directions: up, left, down, right
        for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_i, new_j = r + x, y + c

            if new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols:
                continue

            if grid[new_i][new_j] == 0:
                continue
            
            if visited[new_i][new_j] == 1:
                continue
            # explore next land cell
            self.dfs(new_i, new_j, base_r, base_c, shape,
                     visited, rows, cols, grid)

    # main function
    def countDistinctIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        unique_islands = set()                 # will store unique shapes
        
        for r in range(rows):
            for c in range(cols):
                # start DFS only on unvisited land
                if grid[r][c] == 1 and visited[r][c] == 0:
                    shape = []                # list to hold current shape
                    self.dfs(r, c, r, c, shape, visited, rows, cols, grid)
                    unique_islands.add(tuple(shape))  # add shape to set
        return len(unique_islands)
    

obj = Solution()
grid = [[1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1]]
print( obj.countDistinctIslands(grid) )
# Output  : 3