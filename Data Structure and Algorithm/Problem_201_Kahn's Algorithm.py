"""Given a Directed Acyclic Graph (DAG) of V (0 to V-1) vertices and E edges represented as a 2D list of edges[][], where each entry edges[i] = [u, v] denotes a directed edge u -> v. Return the topological sort for the given graph.

    Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.

Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be true else false."""
from collections import deque
class Solution:
    def topoSort(self, V, edges):
        
        adj_list = [[] for _ in range(V)]
        indegree = [0 for _ in range(V)]
        for u ,v in edges:
            adj_list[u].append(v)
            indegree[v] +=1
        
        result = []
        queue = deque()
        for i in range(0 ,V):
            if indegree[i] == 0:
                queue.append(i)
            
        while queue:
            node  = queue.popleft()
            result.append(node)
            
            for adjNode in adj_list[node]:
                indegree[adjNode] -=1
                if indegree[adjNode]== 0:
                    queue.append(adjNode)
                
        return result
    
obj = Solution()
V = 4
edges = [[3, 0], [1, 0], [2, 0]]
print( obj.topoSort(V , edges) )

#Output : [1, 2, 3, 0]