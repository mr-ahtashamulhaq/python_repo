"""There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

    There are no self-edges (graph[u] does not contain u).
    There are no parallel edges (graph[u] does not contain duplicate values).
    If v is in graph[u], then u is in graph[v] (the graph is undirected).
    The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite."""
from typing import List, Optional
class Solution:
    def dfs_algo(self, graph , visited , node, color):
        visited[node]  = color

        for n in graph[node]:
            if visited [n] != -1:

                #0 ,1
                if visited[n] == color:
                    return False

            else:
                if color == 0:
                    ans  = self.dfs_algo(graph, visited, n, 1)
                else:
                    ans  = self.dfs_algo(graph, visited, n, 0)

                if ans == False:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [-1 for _ in range(n)]

        for i in range(n):
            if visited[i] == -1:
                ans = self.dfs_algo(graph  , visited , i , 0)
                if ans ==False:
                    return False
        return True
obj = Solution()
graph = [[1,3],[0,2],[1,3],[0,2]]
print( obj .isBipartite(graph) )
# Output  : True