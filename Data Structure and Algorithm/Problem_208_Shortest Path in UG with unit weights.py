"""You are given an adjacency list, adj of Undirected Graph having unit weight of the edges, find the shortest path from src to all the vertex and if it is unreachable to reach any vertex, then return -1 for that vertex."""
from collections import deque
class Solution:
    def shortestPath(self, adj, src):
        # code here
        
        queue = deque()
        
        distance = [-1 for _ in range(len(adj))]
        queue.append([src , 0])
        distance[src] = 0
        
        while queue:
            node , dist = queue.popleft()
            
            for adjNode in adj[node]:
                if distance[adjNode] == -1:
                    distance[adjNode] = dist+1
                    queue.append([adjNode , dist+1])
                    
        return distance
obj = Solution()
adj= [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]]
src=0
print( obj.shortestPath(adj, src) )
# Output : [0, 1, 2, 1, 2, 3, 3, 4, 4]