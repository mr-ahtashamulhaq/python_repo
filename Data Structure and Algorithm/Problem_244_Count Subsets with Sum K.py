"""Given an array arr of non-negative integers and an integer target, the task is to count all subsets of the array whose sum is equal to the given target."""
class Solution:
    # USING RECURSION
    def recursion(self, index, total, arr):
        if index == 0:  # If reaches at end
            if total == 0 and arr[index] == 0:  # if end value is zero then 2 subset
                return 2
            if (
                total == 0 or arr[index] == total
            ):  # if end value also total then only one subset
                return 1
            return 0

        if arr[index] > total:
            ans1 = 0
        else:
            ans1 = self.recursion(index - 1, total - arr[index], arr)

        ans2 = self.recursion(index - 1, total, arr)

        return ans1 + ans2

    def perfectSum(self, arr, target):
        n = len(arr)
        return self.recursion(n - 1, target, arr)









    # USING MEMOIZATION
    def memoization(self, index, total, arr, dp):
        if index == 0:  # If reaches at end
            if total == 0 and arr[index] == 0:  # if end value is zero then 2 subset
                return 2
            if (
                total == 0 or arr[index] == total
            ):  # if end value also total then only one subset
                return 1
            return 0

        if dp[index][total] is not None:
            return dp[index][total]

        if arr[index] > total:
            ans1 = 0
        else:
            ans1 = self.memoization(index - 1, total - arr[index], arr, dp)

        ans2 = self.memoization(index - 1, total, arr, dp)

        dp[index][total] = ans1 + ans2
        return dp[index][total]

    def perfectSum_memo(self, arr, target):
        n = len(arr)
        dp = [[None for _ in range(target + 1)] for _ in range(n)]
        return self.memoization(n - 1, target, arr, dp)








    #USING TABULATION
    def perfectSum_tabu(self, arr, target):
        n = len(arr)
        dp = [[0 for _ in range(target + 1)] for _ in range(n)]

        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
            if arr[0] <= target:
                dp[0][arr[0]] = 1

        for index in range(1, n):
            for total in range(0, target + 1):

                if arr[index] > total:
                    ans1 = 0
                else:
                    ans1 = dp[index - 1][total - arr[index]]

                ans2 = dp[index - 1][total]

                dp[index][total] = ans1 + ans2

        return dp[n - 1][target]







    #USING TABULATION WITH SPACE OPTIMIZATION
    def perfectSum_tabuSpaceOpt(self, arr, target):
        n = len(arr)
        prev = [0 for _ in range(target + 1)]

        if arr[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1
            if arr[0] <= target:
                prev[arr[0]] = 1

        for index in range(1, n):
            curr = [0 for _ in range(target+1)]
            for total in range(0, target + 1):

                if arr[index] > total:
                    ans1 = 0
                else:
                    ans1 = prev[total - arr[index]]

                ans2 = prev[total]

                curr[total] = ans1 + ans2
            prev = curr.copy()
        return prev[target]



obj = Solution()
arr = [2, 3, 5, 6, 8, 10]
target = 10
print(obj.perfectSum(arr, target))
print(obj.perfectSum_memo(arr, target))
print(obj.perfectSum_tabu(arr, target))
print(obj.perfectSum_tabuSpaceOpt(arr, target))

# Output : 3