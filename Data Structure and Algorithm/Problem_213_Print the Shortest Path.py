"""You are given a weighted undirected graph having n vertices numbered from 1 to n and m edges along with their weights. Find the shortest weight path between the vertex 1 and the vertex n,  if there exists a path, and return a list of integers whose first element is the weight of the path, and the rest consist of the nodes on that path. If no path exists, then return a list containing a single element -1.

The input list of edges is as follows - {a, b, w}, denoting there is an edge between a and b, and w is the weight of that edge.

Note: The driver code here will first check if the weight of the path returned is equal to the sum of the weights along the nodes on that path, if equal it will output the weight of the path, else -2. In case the list contains only a single element (-1) it will simply output -1. """
import heapq
from typing import List
class Solution:
    def shortestPath(self, n, m, edges ):

        src= 1
        adj_list = [[] for _ in range(n+1)]
        
        for u , v , d in edges:
            adj_list[u].append([v, d])
            adj_list[v].append([u ,d])
            
        distance = [float("inf") for _ in range(n+1)]
        parent = [i for i in range(n+1)]
        
        priority_q = []   
        priority_q.append([0 , src])
        distance[src] = 0
        
        while priority_q:
            curr_dist, node = heapq.heappop(priority_q)
            
            if curr_dist > distance[node]:
                continue
            
            for adjNode, weight in adj_list[node]:
                new_dist = curr_dist + weight
                
                if new_dist < distance[adjNode]:
                    heapq.heappush(priority_q , [new_dist , adjNode])
                    distance[adjNode] = new_dist
                    parent[adjNode] = node

        # if target not reachable
        if distance[n] == float("inf"):
            return [ -1]
        
        # reconstruct path
        path = []
        node = n
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        
        path.append(src)
        path = path[::-1]
                    
        return path

obj = Solution()
n = 5
m= 6
edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
print( obj.shortestPath(n , m, edges) )
# Output : [1, 4, 3, 5]