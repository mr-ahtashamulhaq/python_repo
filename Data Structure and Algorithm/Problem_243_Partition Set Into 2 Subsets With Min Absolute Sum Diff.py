"""Given an array arr[]  containing non-negative integers, the task is to divide it into two sets set1 and set2 such that the absolute difference between their sums is minimum and find the minimum difference."""
class Solution:
    # USING RECURSION
    def recursion(self, index, target, arr):
        if target == 0:
            return True
        if index == 0:
            return arr[0] == target
        not_pick = self.recursion(index - 1, target, arr)
        pick = False
        if arr[index] <= target:
            pick = self.recursion(index - 1, target - arr[index], arr)
        return pick or not_pick

    def minDifference(self, arr):
        n = len(arr)
        total = sum(arr)
        min_diff = float("inf")
        for s1 in range(total + 1):
            if self.recursion(n - 1, s1, arr):
                s2 = total - s1
                min_diff = min(min_diff, abs(s1 - s2))
        return min_diff







    # USING MEMOIZATION
    def memoization(self, index, target, arr, dp):
        if target == 0:
            return True
        if index == 0:
            return arr[0] == target
        if dp[index][target] != -1:
            return dp[index][target]
        not_pick = self.memoization(index - 1, target, arr, dp)
        pick = False
        if arr[index] <= target:
            pick = self.memoization(index - 1, target - arr[index], arr, dp)
        dp[index][target] = pick or not_pick
        return dp[index][target]

    def minDifference_memo(self, arr):
        n = len(arr)
        total = sum(arr)
        dp = [[-1] * (total + 1) for _ in range(n)]
        min_diff = float("inf")
        for s1 in range(total + 1):
            if self.memoization(n - 1, s1, arr, dp):
                s2 = total - s1
                min_diff = min(min_diff, abs(s1 - s2))
        return min_diff







    # USING TABULATION
    def minDifference_tabu(self, nums):
        n = len(nums)
        total = sum(nums)

        dp = [[False] * (total + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        if nums[0] <= total:
            dp[0][nums[0]] = True

        for i in range(1, n):
            for t in range(1, total + 1):
                not_pick = dp[i - 1][t]
                pick = False
                if nums[i] <= t:
                    pick = dp[i - 1][t - nums[i]]
                dp[i][t] = pick or not_pick

        min_diff = float("inf")
        for s1 in range(1, total + 1):
            if dp[n - 1][s1] == True:
                s2 = total - s1
                min_diff = min(min_diff, abs(s1 - s2))
        return min_diff







    # USING TABULATION WITH SPACE OPTIMIZATION
    def minDifference_tabuSpaceOpt(self, nums):
        n = len(nums)
        total = sum(nums)

        prev = [False] * (total + 1)
        prev[0] = True

        if nums[0] <= total:
            prev[nums[0]] = True

        for i in range(1, n):
            curr = [False] * (total + 1)
            curr[0] = True
            for t in range(1, total + 1):
                not_pick = prev[t]
                pick = False
                if nums[i] <= t:
                    pick = prev[t - nums[i]]
                curr[t] = pick or not_pick
            prev = curr

        min_diff = float("inf")
        for s1 in range(1, total + 1):
            if prev[s1] == True:
                s2 = total - s1
                min_diff = min(min_diff, abs(s1 - s2))
        return min_diff
    
    
    
obj = Solution()
nums = [1, 6, 11, 5]
print(obj.minDifference(nums))
print(obj.minDifference_memo(nums))
print(obj.minDifference_tabu(nums))
print(obj.minDifference_tabuSpaceOpt(nums))

# Output  : 1