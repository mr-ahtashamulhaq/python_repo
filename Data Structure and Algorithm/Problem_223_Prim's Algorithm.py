"""Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is provided as a list of edges, where each edge is represented as [u, v, w], indicating an edge between vertex u and vertex v with edge weight w."""
import heapq
class Solution:
    def spanningTree(self, V, edges):

        adj_list = [ [] for _ in range(V) ]
        
        for u, v, w in edges:
            adj_list[u].append([v , w]) #node , weight
            adj_list[v].append([u , w])
        
        visited = [0 for _ in range(V)]
        
        mst_edges = []      #This will store all the edges of MST
        total_sum = 0
        
        priority_q = []
        priority_q.append([0, 0, -1]) #weight, node, parent
        
        
        while priority_q :
            weight , node, parent = heapq.heappop(priority_q)
            
            if visited[node] == 0:
                visited[node] = 1
                
                if visited[node] != -1 :
                    mst_edges.append([node , parent])
                    total_sum += weight  
                
                for adjNode , adj_wt in adj_list[node]:
                    if visited[adjNode] == 0:
                        heapq.heappush(priority_q , [adj_wt , adjNode , node])
        return total_sum
obj = Solution()
V = 3
E = 3
Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
print( obj.spanningTree(V, Edges) )

# Output  : 4