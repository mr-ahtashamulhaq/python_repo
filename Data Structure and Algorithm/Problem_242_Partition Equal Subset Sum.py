"""Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise."""
class Solution:
    # USING RECURSION
    def recursion(self, index, target, arr):
        if target == 0:
            return True
        if index == 0:
            return arr[0] == target

        ans1 = False
        if arr[index] <= target:
            ans1 = self.recursion(index - 1, target - arr[index], arr)

        ans2 = self.recursion(index - 1, target, arr)

        return ans1 or ans2

    def canPartition(self, arr) -> bool:
        n = len(arr)
        total = sum(arr)

        if total % 2 != 0:
            return False

        target = total // 2
        return self.recursion(n - 1, target, arr)







    # USING MEMOIZATION
    def memoization(self, index, target, arr, dp):
        if target == 0:
            return True
        if index == 0:
            return arr[0] == target

        if dp[index][target] != -1:
            return dp[index][target]

        ans1 = False
        if arr[index] <= target:
            ans1 = self.memoization(index - 1, target - arr[index], arr, dp)

        ans2 = self.memoization(index - 1, target, arr, dp)

        dp[index][target] = ans1 or ans2
        return dp[index][target]

    def canPartition_memo(self, arr) -> bool:
        n = len(arr)
        total = sum(arr)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

        return self.memoization(n - 1, target, arr, dp)







    # USING TABULATION
    def canPartition_tabu(self, nums) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = [[False] * (target + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, n):
            for t in range(1, target + 1):
                not_pick = dp[i - 1][t]
                pick = False
                if nums[i] <= t:
                    pick = dp[i - 1][t - nums[i]]
                dp[i][t] = pick or not_pick

        return dp[n - 1][target]







    # USING TABULATION WITH SPACE OPTIMIZATION
    def canPartition_tabuwithSpceOpt(self, nums) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        prev = [False] * (target + 1)
        prev[0] = True

        if nums[0] <= target:
            prev[nums[0]] = True

        for index in range(1, n):
            curr = [False] * (target + 1)
            curr[0] = True
            for t in range(1, target + 1):
                not_pick = prev[t]
                pick = False
                if nums[index] <= t:
                    pick = prev[t - nums[index]]
                curr[t] = pick or not_pick
            prev = curr

        return prev[target]

    
    
    
obj = Solution()
nums = [1, 5, 11, 5]
print(obj.canPartition(nums))
print(obj.canPartition_memo(nums))
print(obj.canPartition_tabu(nums))
print(obj.canPartition_tabuwithSpceOpt(nums))

# Output  : True