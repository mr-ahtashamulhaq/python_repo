"""You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely."""

from typing import List

class Solution:
    def recursion(self, l, r, nums, dp):
        if l > r:
            return 0

        if (l, r) in dp:
            return dp[(l, r)]

        dp[(l, r)] = 0
        for i in range(l, r + 1):
            coins = nums[l - 1] * nums[i] * nums[r + 1]
            coins += self.recursion(l, i - 1, nums, dp) + self.recursion(i + 1, r, nums, dp)
            dp[(l, r)] = max(dp[l, r], coins)

        return dp[(l, r)]

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        return self.recursion(1, len(nums) - 2, nums, dp)


obj = Solution()
nums = [3, 1, 5, 8]
print(obj.maxCoins(nums))

# Output : 167