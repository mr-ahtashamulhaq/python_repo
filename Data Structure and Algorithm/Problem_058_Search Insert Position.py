"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity."""
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lowerbound = n
        low = 0
        high = n-1

        while low<=high:
            mid = (low+high)//2
            
            if nums[mid] >= target:
                lowerbound = mid
                high = mid -1
            else:
                low = mid+1
        return lowerbound
obj = Solution()
nums = [1, 2, 4, 4, 5]
target = 4

print( obj.searchInsert(nums, target)) 
# output : 2