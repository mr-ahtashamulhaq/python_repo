"""Given an integer array nums, return the length of the longest strictly increasing Subsequence."""
class Solution:
    # USING RECURSION
    def recursion(self, ind, prev_ind, nums):
        if ind == len(nums):
            return 0

        not_pick = 0 + self.recursion(ind + 1, prev_ind, nums)
        pick = 0
        if nums[ind] > nums[prev_ind] or prev_ind == -1:
            pick = 1 + self.recursion(ind + 1, ind, nums)

        return max(pick, not_pick)

    def lengthOfLIS(self, nums) -> int:

        return self.recursion(0, -1, nums)







    # USING MEMOIZATION
    def memoization(self, ind, prev_ind, nums, dp):
        if ind == len(nums):
            return 0

        if dp[ind][prev_ind + 1] != -1:
            return dp[ind][prev_ind + 1]

        not_pick = 0 + self.memoization(ind + 1, prev_ind, nums, dp)
        pick = 0
        if prev_ind == -1 or nums[ind] > nums[prev_ind]:
            pick = 1 + self.memoization(ind + 1, ind, nums, dp)

        dp[ind][prev_ind + 1] = max(pick, not_pick)
        return dp[ind][prev_ind + 1]

    def lengthOfLIS_memo(self, nums) -> int:
        # dp = dp[ind][prev_ind] --> index could be from 0 to n-1 -->prev_ind could be from -1 to n-1
        # so dp will be --> N * N+1
        n = len(nums)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
        return self.memoization(0, -1, nums, dp)










    #USING MEMOIZATION
    def lengthOfLIS_tabu(self, nums) -> int:
        # dp = dp[ind][prev_ind] --> index could be from 0 to n-1 -->prev_ind could be from -1 to n-1
        # so dp will be --> N * N+1
        n = len(nums)
        dp = [
            [0 for _ in range(n + 1)] for _ in range(n+1)
        ]  # By Default it will be zero --> base cond = if ind == n return 0

        for ind in range(n - 1, -1, -1):
            for prev_ind in range(ind - 1, -2, -1):
                not_pick = 0 + dp[ind + 1][prev_ind+1]
                pick = 0
                if prev_ind == -1 or nums[ind] > nums[prev_ind]:
                    pick = 1 + dp[ind + 1][ind+1]

                dp[ind][prev_ind + 1] = max(pick, not_pick)
        return dp[0][-1 + 1]
 
    
    
    
    
    
    
    # USING DIFFRENT APPROACH WITH 1D - DP --> Called Algorithmic approach
    def lengthOfLIS_1D_DP (self, nums) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]

        for index in range(n):
            for prev in range(0, index):
                if nums[prev] < nums[index]:
                    dp[index] = max(dp[index] , 1+ dp[prev])
        
        return max(dp)
    
    
    
obj = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(obj.lengthOfLIS(nums))
print(obj.lengthOfLIS_memo(nums))
print(obj.lengthOfLIS_tabu(nums))
print(obj.lengthOfLIS_1D_DP(nums))

# Output : 4