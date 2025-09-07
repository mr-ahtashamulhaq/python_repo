"""Given a connected undirected graph containing V vertices represented by a 2-d adjacency list adj[][], where each adj[i] represents the list of vertices connected to vertex i. Perform a Depth First Search (DFS) traversal starting from vertex 0, visiting vertices from left to right as per the given adjacency list, and return a list containing the DFS traversal of the graph.

Note: Do traverse in the same order as they are in the given adjacency list."""

class Solution:
    #Helper function
    def dfs_algo(self, adj, result , visited , node):
        visited[node]  = 1
        result.append(node)

        for n in adj[node]:
            if visited [n] == 0:
                self.dfs_algo(adj, result, visited, n)

    # DFS Calculation main function
    def dfs(self, adj):
        n = len(adj)
        result  = []
        visited = [0 for _ in range(n)]

        self.dfs_algo(adj , result , visited , 0)
        return result


obj =Solution()
adj= [[2, 3, 1], [0], [0, 4], [0], [2]]
print(obj.dfs(adj))
# Output : [0, 2, 4, 3, 1]