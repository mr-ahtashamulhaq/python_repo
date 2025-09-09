"""There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order."""
from typing import List, Optional
class Solution:
    # -------- helper DFS ----------
    def dfs(self, current_node, adj_list, vis, path_vis, is_safe):
        vis[current_node] = 1       
        path_vis[current_node] = 1   

        for adjNode in adj_list[current_node]:
            if vis[adjNode] == 0:                    
                ans = self.dfs(adjNode, adj_list, vis, path_vis, is_safe)
                if ans == False:                    
                    return False
            elif path_vis[adjNode] == 1:            
                return False                         

        path_vis[current_node] = 0   
        is_safe[current_node] = 1    
        return True

    # -------- main function ----------
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        vis       = [0 for _ in range(V)]   # not processed yet
        path_vis  = [0 for _ in range(V)]   # not on current path
        is_safe   = [0 for _ in range(V)]   # 0 =  unsafe

        # launch DFS fro every unvisited node
        for i in range(V):
            if vis[i] == 0:
                self.dfs(i, graph, vis, path_vis, is_safe)

        # collect all nodes proven safe
        result = []
        for i in range(V):
            if is_safe[i] == 1:
                result.append(i)
        return result
    
obj = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print( obj.eventualSafeNodes(graph) )
# Output  : [2, 4, 5, 6]