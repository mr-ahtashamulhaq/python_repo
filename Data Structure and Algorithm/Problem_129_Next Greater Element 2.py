"""Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number."""
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range((2*n)-1 , -1, -1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
                
            if stack and i < n:
                result[i] = stack[-1]

            stack.append(nums[i%n])
            
        return result
    
obj = Solution()
nums = [1,2,3,4,3]
print(obj.nextGreaterElements(nums))

# Output : [2, 3, 4, -1, 4]