"""Given a sorted array nums of integers and a value target, implement two functions:

lower_bound(nums, target) → Returns the index of the first element in nums that is greater than or equal to target.
If all elements are smaller than target, return len(nums).

upper_bound(nums, target) → Returns the index of the first element in nums that is strictly greater than target.
If no element is greater than target, return len(nums).

You must write the functions with O(log n) time complexity."""
class Solution:
    # Lowerbound
    def lower_bound(self,nums, target):
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
    
    #UPPER BOUND
    def upper_bound(self,nums, target):
        n = len(nums)
        upperbound = n
        low = 0
        high = n-1

        while low<=high:
            mid = (low+high)//2
            
            if nums[mid] > target:
                upperbound = mid
                high = mid -1
            else:
                low = mid+1
        return upperbound

obj = Solution()
nums = [1, 2, 4, 4, 5]
target = 4

print("Lower Bound:", obj.lower_bound(nums, target))  # 2
print("Upper Bound:", obj.upper_bound(nums, target))  # 4