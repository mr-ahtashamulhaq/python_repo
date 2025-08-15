"""Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. """
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
    
    def countFreq(self, nums, target):
        # code here
        
        lb = self.lower_bound(nums, target)
        
        if lb == len(nums) or nums[lb] != target:
            return 0
        
        ub = self.upper_bound(nums, target)
        return ub - lb

obj = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 6
print(obj.countFreq(nums, target))  
# Output: 0