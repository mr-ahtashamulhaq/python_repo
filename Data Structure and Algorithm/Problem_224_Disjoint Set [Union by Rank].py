"""You are given n elements numbered from 1 to n. Initially, each element is in its own group.

You need to process k queries. Each query is one of the following types:

    UNION x z – Merge the groups that contain elements x and z. After this operation, both elements will belong to the same group.

    FIND x – Output the ultimate representative of the group containing element x. The representative is the element that acts as the "leader" of the group.

Initially, every element is the leader of its own group."""


class DisjoinetSet:
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

        else:                           # both parent are same --> use any of above conditions body
            self.parent[pv] = pu
            self.rank[pu] += 1
            


ds = DisjoinetSet(7)

ds.unionSet(1, 2)
ds.unionSet(2, 3)
ds.unionSet(4, 5)
ds.unionSet(6, 7)
ds.unionSet(5, 6)


print(ds.find(1))  # will return Ultimate parent of 1
print(ds.find(7))  # will return Ultimate parent of 7

# Output  :
# 1
# 4

# These are connected component because there ultimate parents are differnet