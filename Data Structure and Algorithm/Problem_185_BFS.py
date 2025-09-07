"""Given a connected undirected graph containing V vertices, represented by a 2-d adjacency list adj[][], where each adj[i] represents the list of vertices connected to vertex i. Perform a Breadth First Search (BFS) traversal starting from vertex 0, visiting vertices from left to right according to the given adjacency list, and return a list containing the BFS traversal of the graph.

Note: Do traverse in the same order as they are in the given adjacency list."""
from collections import deque
class Solution:
    #Helper function
    def bfs_algo(self, n , adj, starting):
        queue = deque()
        result = []
        visited = [0 for _ in range(n)]

        queue.append(starting)
        visited[starting]  = 1

        while queue:
            e = queue.popleft()
            result.append(e)
            for node in adj[e]:
                if visited[node] == 0:
                    queue.append(node)
                    visited[node] = 1
        return result

    def bfs(self, adj):
        n = len(adj)
        return self.bfs_algo(n, adj, 0)

obj =  Solution()
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(obj.bfs(adj))
# Output : [0, 2, 3, 1, 4]