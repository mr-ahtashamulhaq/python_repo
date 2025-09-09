"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array"""
from typing import List, Optional
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for u ,v in prerequisites:
            adj_list[v].append(u)
            indegree[u] +=1
        
        result = []
        queue = deque()
        for i in range(0 ,numCourses):
            if indegree[i] == 0:
                queue.append(i)
            
        while queue:
            node  = queue.popleft()
            result.append(node)
            
            for adjNode in adj_list[node]:
                indegree[adjNode] -=1
                if indegree[adjNode]== 0:
                    queue.append(adjNode)
                
        if len(result) == numCourses:
            return result
        else:
            return []
obj = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(obj.findOrder(numCourses , prerequisites))

# Output : [0, 1, 2, 3]