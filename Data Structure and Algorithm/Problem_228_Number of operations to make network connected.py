"""There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1."""

from typing import List, Optional
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
            return True

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv

        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu

        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

        return False


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)

        extra_edge = 0

        for u, v in connections:
            if ds.unionSet(u, v) == True:
                extra_edge += 1

        connected_comp = 0
        for i in range(n):
            if ds.find(i) == i:
                connected_comp += 1

        if extra_edge >= connected_comp - 1:
            return connected_comp - 1
        return -1


obj = Solution()
n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
print(obj.makeConnected(n, connections))

# Output  : 2