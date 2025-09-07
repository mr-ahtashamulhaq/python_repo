"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges 
(each edge is a pair of nodes), write a function to find the number of 
connected components in an undirected graph.
"""
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list representation
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        components = 0
        
        # DFS helper function
        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        # Count connected components
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1
        
        return components


obj = Solution()
n1 = 5
edges1 = [[0,1],[1,2],[3,4]]
result1 = obj.countComponents(n1, edges1)

print(f"Input: n = {n1}, edges = {edges1}")
print(f"Output: {result1}")

# Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
# Output: 2