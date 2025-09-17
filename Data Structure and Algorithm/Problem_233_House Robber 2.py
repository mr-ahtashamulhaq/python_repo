"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police."""
from typing import List, Optional
class Solution:
    #USING RECURSION
    def recursion(self, index, nums):
        if index == 0:
            return nums[index]

        if index == -1:
            return 0
        
        pick = nums[index] + self.recursion(index - 2, nums)
        notpick = self.recursion(index - 1, nums)

        return max(pick, notpick)
    def rob_recursion(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        ans1 = self.recursion(n - 2, nums[0 : n - 1])
        ans2 = self.recursion(n - 2, nums[1 : n])
        
        return max(ans1, ans2)
    
    
    
    
    
    #USING MEMOIZATION
    def memoization(self, index, nums, dp):
        if index == 0:
            return nums[index]

        if index == -1:
            return 0

        if dp[index] != -1:
            return dp[index]

        pick = nums[index] + self.memoization(index - 2, nums, dp)
        notpick = self.memoization(index - 1, nums, dp)
        
        dp[index] = max(pick, notpick)
        
        return dp[index]
    
    def rob_memo(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp1 = [-1] * (n - 1)
        
        ans1 = self.memoization(n - 2, nums[0 : n - 1], dp1)

        dp2 = [-1] * (n - 1)
        ans2 = self.memoization(n - 2, nums[1 : n], dp2)
        
        return max(ans1, ans2)
    
    
    
    
    
    
    #USING TABULATION
    def solve_tabu(self, nums):
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        for index in range(1, n):
            
            if index > 1:
                pick = nums[index] + dp[index - 2]
            else:
                pick = nums[index]
           
            not_pick = dp[index - 1]
            dp[index] = max(pick, not_pick)
        return dp[n - 1]
    
    def rob_tabu(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        ans1 = self.solve_tabu(nums[0 : n - 1])
        ans2 = self.solve_tabu(nums[1 : n])
        return max(ans1, ans2)
    
    
    
    
    
    #USING TABULATION WITH SPACE OPTIMIZATION
    def solve(self, nums):
        n = len(nums)
        prev = nums[0]   
        prev2 = 0        
        for index in range(1, n):
            
            if index > 1:
                pick = nums[index] + prev2
            else:
                pick = nums[index]
           
            not_pick = prev
            curr = max(pick, not_pick)
            
           
            prev2 = prev
            prev = curr
        return prev
    
    def rob_tabuSpaceOpt(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # Try both scenarios (excluding first or last house)
        ans1 = self.solve(nums[0 : n - 1])
        ans2 = self.solve(nums[1 : n])
        return max(ans1, ans2)
    
    
    
obj = Solution()
nums = [104, 209, 137, 52, 158, 67, 213, 86, 141]
print( obj.rob_recursion(nums) )
print( obj.rob_memo(nums) )
print( obj.rob_tabu(nums) )
print( obj.rob_tabuSpaceOpt(nums) )

# Output : 721