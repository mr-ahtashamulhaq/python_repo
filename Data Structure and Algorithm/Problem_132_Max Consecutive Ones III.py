"""Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's."""
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result  = 0
        left  = 0
        right  = 0
        zeros  = 0

        # --- BETTER SOLUTION --- 
        while right < len(nums):
            if nums[right] == 0:
                zeros +=1
            while zeros>k:
                if nums[left] ==1:
                    left +=1
                else:
                    zeros -=1
                    left +=1
            if zeros <= k:
                result = max(result , (right - left) +1)
            right +=1

        # --- OPTIMAL SOLUTION ---
        # while right < len(nums):
        #     if nums[right] == 0:
        #         zeros +=1
        #     if zeros>k:
        #         if nums[left] ==1:
        #             left +=1
        #         else:
        #             zeros -=1
        #             left +=1
        #     if zeros <= k:
        #         result = max(result , (right - left) +1)
        #     right +=1


        return result

obj = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]; k = 2
print(obj.longestOnes(nums,k))
# Output : 6