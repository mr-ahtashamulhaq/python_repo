"""Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not. The graph can have multiple component."""
class Solution:
    def dfs_algo(self, adj,  visited , node , parent):
        visited[node]  = 1

        for adjNode in adj[node]:
            if visited [adjNode] == 0:
                ans = self.dfs_algo(adj,  visited, adjNode, node)
                if ans == True :
                    return True
            elif adjNode != parent:
                    return True
        return False
    
    
    def isCycle(self, V, edges):
		
        adj_list = [[] for _ in range(V)]
        for u , v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [0 for _ in range(V+1)]
        
        for i in range(0, V):
            if visited[i] == 1:
                continue

            if self.dfs_algo(adj_list  , visited , i, -1):
                return True
            
        return False
		    
obj  = Solution()
V = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
print(obj.isCycle(V, edges))
# Output : True