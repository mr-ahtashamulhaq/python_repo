"""Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not. The graph can have multiple component."""
from collections import deque
class Solution:
	def isCycle(self, V, edges):
		#Code here
		adj_list = [[] for _ in range(V)]
		
		for u , v in edges:
			adj_list[u].append(v)
			adj_list[v].append(u)
		visited = [0 for _ in range(V+1)]
		
		for i in range(0, V):
			if visited[i] == 1:
				continue
			queue = deque()
			queue.append((i, -1))
			visited[i] = 1
			
			while queue:
				node, parent = queue.popleft()
				for adjNode in adj_list[node]:
					if visited[adjNode] == 0:
						visited[adjNode] = 1
						queue.append((adjNode, node))
					else:
						if adjNode != parent:
							return True
		return False
						
obj = Solution()
V = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
print(obj.isCycle(V, edges))
# Output : True