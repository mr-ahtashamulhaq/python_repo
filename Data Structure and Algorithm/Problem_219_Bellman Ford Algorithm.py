"""Given an weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by a 2d array edges[][], where edges[i] = [u, v, w] represents a direct edge from node u to v having w edge weight. You are also given a source vertex src.

Your task is to compute the shortest distances from the source to all other vertices. If a vertex is unreachable from the source, its distance should be marked as 108. Additionally, if the graph contains a negative weight cycle, return [-1] to indicate that shortest paths cannot be reliably computed"""
class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        
        distance = [10**8 for _ in range(V)]
        distance[src] = 0
        
        # This loop will compute the shortest distane from source node to every node
        for _ in range(V-1):
            for u ,v ,w in edges:
                if distance[u] != 10**8:    # Only relax if it is not infinity , Because infinity cannot calculated / cannot sum infinity
                    if distance[u] + w < distance[v]:
                        distance[v] = distance[u] +w
            
        # This one time loop is to check if there is any negative cycle involded
        for u ,v, w in edges:
            if distance[u] != 10**8:
                if distance[u] +w < distance[v]:    #if still relaxing mean cycle is invloved 
                    return [-1]
                    
        
        return distance
obj = Solution()
V = 5
edges= [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
src = 0
print( obj.bellmanFord(V, edges, src) )

# Output  : [0, 5, 6, 6, 7]