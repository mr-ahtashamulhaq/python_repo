"""There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order."""
from typing import List, Optional
from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        adj_list = [[] for _ in range( V)]
        indegree = [0 for _ in range(V)]

        #In Graph at every index we have nodes, by which it is connected , so we have to reverse it
        # if in first 0 is connected with 2 and 1 so we will reverse it and make connect 2 and 1 with 0
        for node in range(0,V):
            for adjNode in graph[node]:
                adj_list[adjNode].append(node)
                indegree[node] +=1
                
        result = []
        queue = deque()
        #append all 0 indegrees in queue
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            result.append(node)

            for adjNode in adj_list[node]:
                indegree[adjNode] -=1
                if indegree[adjNode] == 0:
                    queue.append(adjNode)

        return sorted(result)

obj = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print( obj.eventualSafeNodes(graph) )
# Output : [2, 4, 5, 6]