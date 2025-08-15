"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity."""
from typing import List

class Solution:
    def lower_bound(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        lowerbound = n 

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lowerbound = mid
                high = mid - 1
            else:
                low = mid + 1
        return lowerbound
    
    def upper_bound(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        upperbound = n

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                upperbound = mid
                high = mid - 1
            else:
                low = mid + 1
        return upperbound
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lower_bound(nums, target)
        
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        
        ub = self.upper_bound(nums, target)
        return [lb, ub - 1]

obj = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 6
print(obj.searchRange(nums, target))  
# Output: [-1, -1]