"""Given a Directed Acyclic Graph of V vertices from 0 to n-1 and a 2D Integer array(or vector) edges[ ][ ] of length E, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i.

Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex."""
from typing import List, Optional
class Solution:
    #simple DFS_Algorithm
    def dfs_algo(self, node , visited, adj_list, stack):
        visited[node] =1
        
        for adjNode , d in adj_list[node]:
            if visited[adjNode] == 0:
                self.dfs_algo(adjNode, visited, adj_list , stack)
            
        stack.append(node)
        
    #Main function
    def shortestPath(self, V: int, E: int, edges: List[List[int]]):
        src = 0
        
        #Creating Adjency list
        adj_list = [[] for _ in range(V)]
        for u , v, d in edges:
            adj_list[u].append([v , d])
        
        # Calling DFS for every non visited node/vertes
        visited = [0 for _ in range(V)]
        stack = []
        for i in range(V):
            if visited[i]  == 0:
                self.dfs_algo(i , visited, adj_list, stack)
        
        """Now Stack is ready in sequence so we have to  just check distance of everynode from new node and store it""" 
        distance = [float("inf") for _ in range(V)]
        distance[src] = 0

        while len(stack) != 0:
            node = stack.pop()
            dist = distance[node]
            
            for adjNode, d in adj_list[node]:
                new_dist = d + dist
                #Only store if it is less than previous distance
                if new_dist < distance[adjNode]:
                    distance[adjNode] = new_dist
                    
        # replace float("inf") with -1 --> its question requirement
        for i in range(V):
            if distance[i] == float("inf"):
                distance[i] = -1
        
        return distance

obj = Solution()
V = 6
E = 7
edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]]
print( obj.shortestPath(V , E , edges) )

# Output : [0, 2, 3, 6, 1, 5]