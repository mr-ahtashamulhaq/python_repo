"""You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target."""
class Solution:
    # USING RECURSION
    # Function intuition : number of ways to reach target, with given current total --> summ.
    def recursion(self, index, summ, target, nums):
        if index == 0:
            ways = 0
            if summ - nums[0] == target:
                ways += 1
            if summ + nums[0] == target:
                ways += 1
            return ways

        add = self.recursion(index - 1, summ + nums[index], target, nums)

        subtract = self.recursion(index - 1, summ - nums[index], target, nums)

        return add + subtract

    def findTargetSumWays(self, nums, target: int) -> int:
        n = len(nums)
        return self.recursion(n - 1, 0, target, nums)







    #USING MEMOIZATION
    def memoization(self, index, summ, target, nums, dp):
        if index == 0:
            ways = 0
            if summ - nums[0] == target:
                ways += 1
            if summ + nums[0] == target:
                ways += 1
            return ways

        if dp[index][summ] is not None:
            return dp[index][summ]

        add = self.memoization(index - 1, summ + nums[index], target, nums, dp)

        subtract = self.memoization(index - 1, summ - nums[index], target, nums, dp)

        dp[index][summ] = add + subtract
        return dp[index][summ]

    def findTargetSumWays_memo(self, nums, target: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        dp = [[None for _ in range(2 * total_sum + 1)] for _ in range(n)]

        return self.memoization(n - 1, 0, target, nums, dp)







    #USING TABULATION
    def findTargetSumWays_tabu(self, nums, target: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        offset = total_sum   # to shift negative sums into valid indices
        
        dp = [[0 for _ in range(2 * total_sum + 1)] for _ in range(n)]

        dp[0][nums[0] + offset] += 1
        dp[0][-nums[0] + offset] += 1


        for index in range(1, n):
            for summ in range(-total_sum, total_sum + 1):
                if dp[index - 1][summ + offset] > 0:   
                    # Add current numbers
                    new_sum = summ + nums[index]
                    if -total_sum <= new_sum <= total_sum:
                        dp[index][new_sum + offset] += dp[index - 1][summ + offset]

                    # Subtract current number
                    new_sum = summ - nums[index]
                    if -total_sum <= new_sum <= total_sum:
                        dp[index][new_sum + offset] += dp[index - 1][summ + offset]


        if -total_sum <= target <= total_sum:
            return dp[n - 1][target + offset]
        return 0
    
    
    
    
    
    
    
    
    # USING TABULATION WITH SPACE OPTIMIZATION
    def findTargetSumWays_tabu_optimized(self, nums, target: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        offset = total_sum  
        size = 2 * total_sum + 1

        prev = [0] * size

        prev[nums[0] + offset] += 1
        prev[-nums[0] + offset] += 1


        for index in range(1, n):
            curr = [0] * size
            for summ in range(-total_sum, total_sum + 1):
                if prev[summ + offset] > 0:
                    # Add nums[index]
                    new_sum = summ + nums[index]
                    if -total_sum <= new_sum <= total_sum:
                        curr[new_sum + offset] += prev[summ + offset]

                    # Subtract nums[index]
                    new_sum = summ - nums[index]
                    if -total_sum <= new_sum <= total_sum:
                        curr[new_sum + offset] += prev[summ + offset]

            prev = curr  


        if -total_sum <= target <= total_sum:
            return prev[target + offset]
        return 0




obj = Solution()
nums = [1, 1, 1, 1, 1]
target = 3
print(obj.findTargetSumWays(nums, target))
print(obj.findTargetSumWays_memo(nums, target))
print(obj.findTargetSumWays_tabu(nums, target))
print(obj.findTargetSumWays_tabu_optimized(nums, target))

# Output : 5
