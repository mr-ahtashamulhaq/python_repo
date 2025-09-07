"""Given an undirected graph with V nodes and E edges, create and return an adjacency list of the graph. 0-based indexing is followed everywhere."""
class Solution:
    def printGraph(self, V , edges):
        # code here
        lst = [[]  for _ in range(V)]
        for u , v in edges:
            lst[u].append(v)
            lst[v].append(u)
            
        return lst

obj = Solution()
V = 5
edges = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
print(obj.printGraph(V, edges))

# Output : [[1, 4], [0, 4, 3, 2], [1, 3], [4, 1, 2], [0, 1, 3]]