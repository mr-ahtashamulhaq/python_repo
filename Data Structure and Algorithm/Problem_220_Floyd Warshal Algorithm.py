"""You are given an weighted directed graph, represented by an adjacency matrix, dist[][] of size n x n, where dist[i][j] represents the weight of the edge from node i to node j. If there is no direct edge, dist[i][j] is set to a large value (i.e., 108) to represent infinity.
The graph may contain negative edge weights, but it does not contain any negative weight cycles.

Your task is to find the shortest distance between every pair of nodes i and j in the graph.

Note: Modify the distances for every pair in place"""
class Solution:
	def floydWarshall(self, dist):
		n = len(dist)
		for via in range(n):
			for i in range(n):
				for j in range(n):
					if dist[i][via] != 10**8  and dist[via][j] != 10**8:
						dist[i][j] = min(dist[i][j] , dist[i][via] + dist[via][j])
		return dist
obj = Solution()
dist= [[0, 4, 10**8, 5, 10**8], [10**8, 0, 1, 10**8, 6], [2, 10**8, 0, 3, 10**8], [10**8, 10**8, 1, 0, 2], [1, 10**8, 10**8, 4, 0]]
print( obj.floydWarshall(dist) )

# Output : [[0, 4, 5, 5, 7], [3, 0, 1, 4, 6], [2, 6, 0, 3, 5], [3, 7, 1, 0, 2], [1, 5, 5, 4, 0]]