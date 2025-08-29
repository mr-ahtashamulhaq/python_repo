"""You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise."""
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        
        for i in range(len(nums)):
            if i > max_index:
                return False

            max_index = max(max_index, i + nums[i])

        return True

obj = Solution()
print(obj.canJump([2,3,1,1,4]))
# Output : True