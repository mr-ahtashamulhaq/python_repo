"""Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ans  =[]
        n = len(nums)

        for i in range(k):
            heapq.heappush(ans, nums[i])

        for i in range(k , n):
            if nums[i] > ans[0]:
                heapq.heappop(ans)
                heapq.heappush(ans, nums[i])

        return ans[0]

obj =   Solution()
arr = nums = [3,2,3,1,2,4,5,5,6]; k = 4
print(obj.findKthLargest(arr , k))