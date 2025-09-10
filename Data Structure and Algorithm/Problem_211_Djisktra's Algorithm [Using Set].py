"""Given an undirected, weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by 2d array edges[][], where edges[i]=[u, v, w] represents the edge between the nodes u and v having w edge weight.
You have to find the shortest distance of all the vertices from the source vertex src, and return an array of integers where the ith element denotes the shortest distance between ith node and source vertex src.

Note: The Graph is connected and doesn't contain any negative weight edge."""
import sys

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):

        adj_list = [[] for _ in range(V)]
        for u, v, d in edges:
            adj_list[u].append([v, d])

        # Distance array & set
        distance = [sys.maxsize for _ in range(V)]
        distance[src] = 0

        my_set = set()
        my_set.add((0, src))                       # (dist, node)

        # Main loop
        while len(my_set) != 0:
            dist, node = min(my_set)
            my_set.discard((dist, node))           # remove picked pair

            for adjNode, weight in adj_list[node]:
                dist_trav = dist + weight          # path through 'node'

                if dist_trav < distance[adjNode]:  # found a better path
                    if distance[adjNode] != sys.maxsize:
                        my_set.discard((distance[adjNode], adjNode))

                    distance[adjNode] = dist_trav
                    my_set.add((dist_trav, adjNode))

        return distance
obj = Solution()
V = 5
edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]
src = 0
print( obj.dijkstra(V, edges, src)  )

# Output : [0, 4, 8, 10, 10]