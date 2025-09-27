"""Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing."""
from typing import List, Optional
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [1 for _ in range(n)]
        count = [1 for _ in range(n)]

        for index in range(n):
            for prev in range(0, index):
                if nums[prev] < nums[index]:
                    if 1 + dp[prev] > dp[index]:
                        dp[index] = 1 + dp[prev]
                        # Inherit
                        count[index] = count[prev]

                    elif nums[index] > nums[prev] and dp[prev] + 1 == dp[index]:
                        # Increase the count
                        count[index] += count[prev]

        longest = max(dp)
        result = 0
        for i in range(n):
            if dp[i] == longest:
                result += count[i]
        return result


obj = Solution()
nums = [1, 3, 5, 4, 7]
print(obj.findNumberOfLIS(nums))

# Output : 2