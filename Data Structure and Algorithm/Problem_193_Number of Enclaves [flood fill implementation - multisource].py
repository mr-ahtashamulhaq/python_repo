"""You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves."""
from typing import List, Optional
from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        queue = deque()
        #Put edges '1' in the queue and make its visited 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r == 0 or c ==0 or r==rows-1 or c == cols-1:
                        queue.append((r ,c))
                        visited[r][c] = 1
        count = 0
        while queue:
            #pop all edges '1' and check if there surrounding is 1 make its visited also 1
            r,c = queue.popleft()

            for x , y in [(0,-1), (0, 1), (1, 0), (-1, 0)]:
                new_r = r+x
                new_c = c + y

                if new_r < 0 or new_c <0 or new_r >=rows or new_c >= cols:
                    continue
                if grid[new_r][new_c] == 0:
                    continue
                if visited[new_r][new_c]==1:
                    continue
                
                visited[new_r][new_c] = 1
                queue.append((new_r , new_c))
        #check how many '1' are there which visited is not '1' so these are out ans
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    count +=1
        return count

obj = Solution()
grid  = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print( obj.numEnclaves(grid))

# input
#     [0,0,0,0]
#     [1,0,1,0]
#     [0,1,1,0]
#     [0,0,0,0]

# OUTPUT : 3