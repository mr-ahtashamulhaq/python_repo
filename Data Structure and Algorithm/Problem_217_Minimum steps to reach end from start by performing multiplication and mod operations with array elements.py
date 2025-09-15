"""Given start, end and an array arr of n numbers. At each step, start is multiplied with any number in the array and then mod operation with 100000 is done to get the new start.

Your task is to find the minimum steps in which end can be achieved starting from start. If it is not possible to reach end, then return -1.
"""

from typing import List
from collections import deque


class Solution:

    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:

        distance = [float("inf") for _ in range(0, 100000)]
        distance[start] = 0
        queue = deque()
        queue.append([0, start])

        while queue:
            dist, num = queue.popleft()

            if num == end:
                return dist

            for arr_num in arr:
                new_num = (arr_num * num) % 100000
                new_dist = dist + 1

                if new_dist < distance[new_num]:
                    queue.append([new_dist, new_num])
                    distance[new_num] = new_dist

        return -1


obj = Solution()
arr = [3, 4, 65]
start = 7
end = 66175
print(obj.minimumMultiplications(arr, start, end))

# Output  : 4
