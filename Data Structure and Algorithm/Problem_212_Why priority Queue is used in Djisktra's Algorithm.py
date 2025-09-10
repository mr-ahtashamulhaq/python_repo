"""Why Priority Queue (Min-Heap)?

It always gives us the node with the smallest distance so far.
This matches Dijkstra’s requirement:
Process the closest node first.
Then relax its neighbors.
This way, when we pop a node, we are sure its shortest path is finalized."""
import heapq
class Solution:
    # DJIKSTRA Algorithm --> Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):

        adj_list = [[] for _ in range(V)]
        for u, v, d in edges:
            adj_list[u].append([v, d])
            adj_list[v].append([u, d])  # graph is undirected

        # Distance array: start with infinity, except src = 0
        distance = [float("inf")] * V
        distance[src] = 0

        # Min-Heap with (distance, node) --> heap ensures smallest distance is always processed first
        priority_queue = [[0, src]]

        while priority_queue:
            curr_dist, node = heapq.heappop(priority_queue)

            # if we already found a shorter path earlier, skip
            if curr_dist > distance[node]:
                continue

            # Relaxation step --> Mean for every neighbor, check if going through node gives a shorter distance → if yes, update and push to heap.
            
            for adjNode, weight in adj_list[node]:
                new_dist = curr_dist + weight
                if new_dist < distance[adjNode]:
                    distance[adjNode] = new_dist
                    heapq.heappush(priority_queue, [new_dist, adjNode])

        return distance
                         
          
obj = Solution()
V = 5
edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]
src = 0
print( obj.dijkstra(V , edges , src) )

# Output : [0, 4, 8, 10, 10]