"""Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1."""
from typing import List
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        queue = deque()
        rows  = len(mat)
        cols = len(mat[0])

        visited  = [[0 for _ in range(cols)] for _ in range(rows) ]
        distance  = [[0 for _ in range(cols)] for _ in range(rows) ]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append([i,j, 0])
                    visited[i][j] = 1
        while queue:
            i , j ,d  = queue.popleft()
            distance[i][j] = d

            for x, y in [(-1, 0) , (1, 0) , (0 ,-1) , (0,1)]:
                new_i = i + x
                new_j = j + y

                if new_i < 0 or new_i>=rows or new_j < 0 or new_j >= cols:
                    continue
                if visited[new_i][new_j] ==1:
                    continue
                queue.append([new_i , new_j , d+1])
                visited[new_i][new_j] = 1
                
        return distance

obj = Solution()
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(obj.updateMatrix(mat))
# Output : [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
