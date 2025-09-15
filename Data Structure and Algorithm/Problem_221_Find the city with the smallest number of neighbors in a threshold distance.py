"""There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path."""
class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        adj_matrix = [[float("inf") for _ in range(n)] for _ in range(n)]

        for u, v, w in edges:
            adj_matrix[u][v] = w
            adj_matrix[v][u] = w

        for i in range(n):
            adj_matrix[i][i] = 0

        n = len(adj_matrix)
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if adj_matrix[i][via] != 10**8 and adj_matrix[via][j] != 10**8:
                        adj_matrix[i][j] = min(
                            adj_matrix[i][j], adj_matrix[i][via] + adj_matrix[via][j])

        neighbour = n
        result = -1

        for i in range(n):
            count = 0
            for j in range(n):
                if adj_matrix[i][j] <= distanceThreshold:
                    count += 1

            if count <= neighbour:
                neighbour = count
                result = i
        return result


obj = Solution()
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
print(obj.findTheCity(n, edges, distanceThreshold))

# Output  :  3
