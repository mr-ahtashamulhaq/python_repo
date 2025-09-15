"""Given an undirected graph with V vertices. We say two vertices u and v belong to a single province if there is a path from u to v or v to u. Your task is to find the number of provinces.

Note: A province is a group of directly or indirectly connected cities and no other cities outside of the group. """
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]

    # This will do path compression and return ultimate parent of 'x'
    def find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # This will connect two nodes/points of graph
    def unionSet(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv

        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu

        else:                          
            self.parent[pv] = pu
            self.rank[pu] += 1
        

        
class Solution:
    def numProvinces(self, adj, V):
        ds = DisjointSet(V)
        
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i != j:
                    ds.unionSet(i , j)
                    
        count  = 0
        for i in range(V):
            if ds.find(i) == i:
                count+=1
        return count   

obj = Solution()
adj = [[1, 0, 1],[0, 1, 0],[1, 0, 1]]
V = 3
print( obj.numProvinces(adj,V)  )         

# Output : 2