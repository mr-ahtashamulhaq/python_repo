"""Given an array arr[], partition it into two subsets(possibly empty) such that each element must belong to only one subset. Let the sum of the elements of these two subsets be sum1 and sum2. Given a difference d, count the number of partitions in which sum1 is greater than or equal to sum2 and the difference between sum1 and sum2 is equal to d. """
class Solution:

    # --------------------------------------
    # RECURSION
    # --------------------------------------
    
    def recursion(self, index, target, arr):
        if index == 0:
            if target == 0 and arr[0] == 0: return 2  # two ways: include/exclude zero
            if target == 0 or target == arr[0]: return 1
            return 0
        
        not_pick = self.recursion(index - 1, target, arr)
        pick = 0
        if arr[index] <= target:
            pick = self.recursion(index - 1, target - arr[index], arr)
        return pick + not_pick

    def countPartitions(self, arr, d):
        n = len(arr)
        total = sum(arr)
        if total - d < 0 or (total - d) % 2: return 0
        target = (total - d) // 2
        return self.recursion(n - 1, target, arr)





    # --------------------------------------
    # MEMOIZATION
    # --------------------------------------
    
    def memoization(self, index, target, arr, dp):
        if index == 0:
            if target == 0 and arr[0] == 0: return 2
            if target == 0 or target == arr[0]: return 1
            return 0
        
        if dp[index][target] != -1:
            return dp[index][target]
        
        not_pick = self.memoization(index - 1, target, arr, dp)
        pick = 0
        if arr[index] <= target:
            pick = self.memoization(index - 1, target - arr[index], arr, dp)
        dp[index][target] = pick + not_pick
        return dp[index][target]

    def countPartitions_memo(self, arr, d):
        n = len(arr)
        total = sum(arr)
        if total - d < 0 or (total - d) % 2: return 0
        target = (total - d) // 2
        dp = [[-1] * (target + 1) for _ in range(n)]
        return self.memoization(n - 1, target, arr, dp)




    # --------------------------------------
    # TABULATION (2D DP)
    # --------------------------------------
    
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
            for total in range(target + 1):
                not_pick = dp[index - 1][total]
                pick = 0
                if arr[index] <= total:
                    pick = dp[index - 1][total - arr[index]]
                dp[index][total] = pick + not_pick
        
        return dp[n - 1][target]

    def countPartitions_tabu(self, arr, d):
        n = len(arr)
        total = sum(arr)
        if total - d < 0 or (total - d) % 2: return 0
        return self.perfectSum_tabu(arr, (total - d) // 2)




    # --------------------------------------
    # TABULATION WITH SPACE OPTIMIZATION
    # --------------------------------------
    
    def perfectSum_tabuSpaceOpt(self, arr, target):
        n = len(arr)
        prev = [0] * (target + 1)

        if arr[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1
            if arr[0] <= target:
                prev[arr[0]] = 1

        for index in range(1, n):
            curr = [0] * (target + 1)
            for total in range(target + 1):
                not_pick = prev[total]
                pick = 0
                if arr[index] <= total:
                    pick = prev[total - arr[index]]
                curr[total] = pick + not_pick
            prev = curr
        return prev[target]

    def countPartitions_tabuSpaceOpt(self, arr, d):
        n = len(arr)
        total = sum(arr)
        if total - d < 0 or (total - d) % 2: return 0
        return self.perfectSum_tabuSpaceOpt(arr, (total - d) // 2)


# Driver code
obj = Solution()
arr = [1, 1, 2, 3]
d = 1
print(obj.countPartitions(arr, d))
print(obj.countPartitions_memo(arr, d))
print(obj.countPartitions_tabu(arr, d))
print(obj.countPartitions_tabuSpaceOpt(arr, d))

# Output : 3