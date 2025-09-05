"""You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks."""
from typing import List , Counter
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count= Counter(tasks)
        maxheap = []

        for i in count.values():
            maxheap.append(-i)
        heapq.heapify(maxheap)

        time = 0
        queue = deque()

        while queue or maxheap:
            time +=1

            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt :
                    queue.append([cnt , time +n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap , queue.popleft()[0])
        return time

obj = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
print(obj.leastInterval(tasks , n))
# Output  : 8