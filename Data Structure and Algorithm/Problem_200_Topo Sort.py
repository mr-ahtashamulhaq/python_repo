"""Given a Directed Acyclic Graph (DAG) of V (0 to V-1) vertices and E edges represented as a 2D list of edges[][], where each entry edges[i] = [u, v] denotes a directed edge u -> v. Return the topological sort for the given graph.

    Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.

Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be true else false."""
from typing import List, Optional
class Solution:
    def dfs_algo(self, node, visited, adj_list,  stack):
        visited[node] = 1
        
        for adjNode in adj_list[node]:
            if visited[adjNode] == 0:
                self.dfs_algo(adjNode , visited , adj_list, stack)
        stack.append(node)
    
    def topoSort(self, V, edges):
        # Code here
        visited = [0 for _ in range(V)]
        adj_list = [[] for _ in range(V)]
        stack = []
        for u ,v in edges:
            adj_list[u].append(v)
            
            
        for i in range(0,V):
            if visited[i] == 0:
                self.dfs_algo(i, visited, adj_list , stack)
        return stack[::-1]
obj = Solution()
V = 4
edges = [[3, 0], [1, 0], [2, 0]]
print( obj.topoSort(V, edges) )
# Output : [3, 2, 1, 0]