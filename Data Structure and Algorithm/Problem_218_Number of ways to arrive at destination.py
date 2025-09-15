"""You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.
"""

import heapq


class Solution:
    def countPaths(self, n, roads):

        adj_list = [[] for _ in range(n)]
        MOD = 10**9 + 7
        for u, v, weight in roads:
            adj_list[u].append([v, weight])
            adj_list[v].append([u, weight])

        ways = [0 for _ in range(n)]
        distance = [float("inf") for _ in range(n)]
        distance[0] = 0
        ways[0] = 1  # --> we have 1 number of ways to reach at 0

        priority_q = []
        priority_q.append([0, 0])  # [Dist , Node]

        while priority_q:
            dist, node = heapq.heappop(priority_q)

            for adjNode, weight in adj_list[node]:
                new_dist = dist + weight

                if new_dist < distance[adjNode]:
                    distance[adjNode] = new_dist
                    heapq.heappush(priority_q, [new_dist, adjNode])
                    ways[adjNode] = ways[node]

                elif new_dist == distance[adjNode]:
                    ways[adjNode] += ways[node]

        return ways[n - 1] % MOD


obj = Solution()
n = 7
roads = [
    [0, 6, 7],
    [0, 1, 2],
    [1, 2, 3],
    [1, 3, 3],
    [6, 3, 3],
    [3, 5, 1],
    [6, 5, 1],
    [2, 5, 1],
    [0, 4, 5],
    [4, 6, 2],
]
print(obj.countPaths(n, roads))

# Output : 4
