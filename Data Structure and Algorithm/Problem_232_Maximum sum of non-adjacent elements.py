"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police."""
from typing import List, Optional
class Solution:
    #USING RECURSION
    def recursion(self, index, nums):
        if index == 0:
            return nums[index]
        if index < 0:
            return 0

        pick = nums[index] + self.recursion(index - 2, nums)
        not_pick = 0 + self.recursion(index - 1, nums)

        return max(pick, not_pick)

    def rob_recursion(self, nums: List[int]) -> int:
        n = len(nums)
        return self.recursion(n - 1, nums)






    #USING MEMOIZATION
    def memoization(self, index, dp, nums):
        if index == 0:
            return nums[index]

        if index < 0:
            return 0

        if dp[index] != -1:
            return dp[index]

        pick = nums[index] + self.memoization(index - 2, dp, nums)
        not_pick = 0 + self.memoization(index - 1, dp, nums)

        dp[index] = max(pick, not_pick)
        return dp[index]

    def rob_memo(self, nums):
        n = len(nums)
        dp = [-1 for _ in range(n + 1)]

        return self.memoization(n - 1, dp, nums)






    #USING TABULATION
    def rob_tabu(self, nums):
        n = len(nums)
        dp = [-1 for _ in range(n + 1)]

        dp[0] = nums[0]

        for index in range(1, n):

            if index > 0:
                pick = nums[index] + dp[index - 2]
            else:
                pick = nums[index] + 0

            not_pick = 0 + dp[index - 1]

            dp[index] = max(pick, not_pick)

        return dp[n - 1]






    #USING TABULATION WITH SPACE OPTIMIZATION
    def rob_tabuSpaceOpt(self, nums):
        n = len(nums)
        prev = nums[0]
        prev2 = 0
        curr = 0

        for index in range(1, n):

            if index > 0:
                pick = nums[index] + prev2
            else:
                pick = nums[index] + 0

            not_pick = 0 + prev

            curr = max(pick, not_pick)
            prev2 = prev
            prev = curr

        return curr


obj = Solution()
nums = [104, 209, 137, 52, 158, 67, 213, 86, 141]
print(obj.rob_recursion(nums))
print(obj.rob_memo(nums))
print(obj.rob_tabu(nums))
print(obj.rob_tabuSpaceOpt(nums))

# Output  : 753