"""Given an integer array nums, find the subarray with the largest sum, and return its sum."""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        maxi = float("-inf")
        for i in range(len(nums)):
            total += nums[i]
            maxi = max(total , maxi)
            if total<0:
                total = 0
        return maxi


obj = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(obj.maxSubArray(nums))
# Output : 6