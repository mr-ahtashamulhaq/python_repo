"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space."""
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ans = 0

        # if we xor two same numbers it would return 0 and if we xor any number with 0 it would return that number

        for i in nums:
            ans = ans ^ i
        return ans
        
obj = Solution()
print(obj.singleNumber([5,2,3,8,5,6,3,2,8]))
# Output : 6