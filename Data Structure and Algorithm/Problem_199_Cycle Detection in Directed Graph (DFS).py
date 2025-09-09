"""Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from verticex u to v."""
from typing import List, Optional
class Solution:
    #HELPER FUNCTION FOR DFS
    def dfs_algo(self,adj_list, node, visited ,path_visited):
        
        visited[node]= 1
        path_visited[node] = 1
        
        for adjNode in adj_list[node]:
            if visited[adjNode] == 0:
                ans = self.dfs_algo(adj_list, adjNode,visited, path_visited)
                if ans == True:
                    return True
            elif visited[adjNode] == 1 and path_visited[adjNode]==1:
                return True
        
        path_visited[node]=0
        return False
        
    def isCycle(self, V, edges):

        adj_list = [[] for _ in range(V)]
        for u ,v in edges:
            adj_list[u].append(v)
        
        visited = [0 for _ in range(V)]
        path_visited = [0 for _ in range(V)]
        
        for i in range(0,V):
            if visited[i] == 0:
                ans = self.dfs_algo(adj_list, i , visited, path_visited)
                if ans==True:
                    return True
                    
        return False
obj = Solution()
V = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 3]]
print( obj.isCycle(V , edges) )
# Output  : True