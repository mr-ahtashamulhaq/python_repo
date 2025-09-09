"""Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from verticex u to v."""
from collections import deque
class Solution:
    def isCycle(self, V, edges):
        
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
                
        if len(result) == V:
            return False
        return True
obj = Solution()
V = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 3]]
print( obj.isCycle(V , edges) )
# Output : True