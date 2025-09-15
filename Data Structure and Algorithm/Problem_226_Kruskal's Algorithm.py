"""Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is provided as a list of edges, where each edge is represented as [u, v, w], indicating an edge between vertex u and vertex v with edge weight w."""


class DisjoinetSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unionSet(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False  # return False if they are Connected Component

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

        return True  # return True if they are not Connected Component


class Solution:
    def spanningTree(self, V, edges):

        modified_edges = []
        seen = set()

        for u, v, w in edges:
            modified_edges.append((w, u, v))

        modified_edges.sort()

        ds = DisjoinetSet(V)
        mst_weight = 0

        for w, u, v in modified_edges:
            if ds.unionSet(u, v):  # if They are not connected component then increase size
                mst_weight += w

        return mst_weight


obj = Solution()
V = 3
E = 3
Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
print(obj.spanningTree(V, Edges))

# Output : 4