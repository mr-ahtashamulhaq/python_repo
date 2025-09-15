"""There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1."""
from collections import deque
import sys

class Solution:
    def findCheapestPrice(self, flights, src, dst, k):

        adj_list = [[] for _ in range(n)]      
        for u , v , cost in flights:
            adj_list[u].append([v, cost])

        min_cost = [sys.maxsize for _ in range(n)] 
        min_cost[src ] = 0
        queue = deque()
        queue.append([0 , src, 0])  # [step , src, cost]

        while queue:
            step , node, cost = queue.popleft()

            for adjNode , price in adj_list[node]:
                new_cost = cost + price

                if new_cost < min_cost[adjNode]:
                    new_step = step+1

                    if new_step == k+1:
                        if adjNode != dst:
                            continue

                    min_cost[adjNode] = new_cost
                    queue.append([new_step , adjNode, new_cost])

        if min_cost[dst] == sys.maxsize:
            return -1
        return min_cost[dst]

obj = Solution()
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print( obj.findCheapestPrice(flights, src, dst, k) )
# Output  :  700