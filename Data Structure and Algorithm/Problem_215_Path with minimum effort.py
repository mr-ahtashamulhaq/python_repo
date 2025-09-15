"""You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell."""
from typing import List, Optional
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]):
        rows  = len(heights)
        cols  = len(heights[0])
        effort = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        
        priority_q = []
        priority_q.append([0 , 0 ,0 ])
        effort[0][0] = 0

        while priority_q:
            curr_eff , r , c = heapq.heappop(priority_q)

            if r == rows-1 and c == cols-1:
                return curr_eff

            for x, y in [[0,1] , [0,-1] , [1, 0] , [-1,0]]:
                new_r = r + x
                new_c = c + y

                if new_r < 0 or new_r >=rows or new_c<0 or new_c>=cols:
                    continue
                
                new_eff = max( curr_eff , abs(heights[r][c] - heights[new_r][new_c]))

                if new_eff < effort[new_r][new_c]:
                    effort[new_r][new_c] = new_eff
                    heapq.heappush(priority_q , [new_eff , new_r , new_c])
        
        
obj = Solution()
heights = [[1,2,2],[3,8,2],[5,3,5]]
print( obj.minimumEffortPath(heights))

# Output : 2