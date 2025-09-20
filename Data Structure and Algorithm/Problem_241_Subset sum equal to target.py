"""Given an array of positive integers arr[] and a value sum, determine if there is a subset of arr[] with sum equal to given sum."""
class Solution:
    # USING RECURSION
    def recursion(self, index, remaining, arr):
        if remaining == 0:
            return True

        if index == 0:
            if arr[0] == remaining:
                return True
            return False

        if arr[index] > remaining:
            ans1 = False
        else:
            ans1 = self.recursion(index - 1, remaining - arr[index], arr)

        ans2 = self.recursion(index - 1, remaining, arr)

        return ans1 or ans2

    def isSubsetSum(self, arr, sum):
        n = len(arr)
        solve = self.recursion(n - 1, sum, arr)
        return solve
    
    
    
    
    
    
    
    #USING MEMOIZATION
    def memoization(self, index, remaining, arr, dp):
        if remaining == 0:
            return True

        if index == 0:
            if arr[0] == remaining:
                return True
            return False
        if dp[index][remaining] != -1:
            return dp[index][remaining]

        if arr[index] > remaining:
            ans1 = False
        else:
            ans1 = self.memoization(index - 1, remaining - arr[index], arr, dp)

        ans2 = self.memoization(index - 1, remaining, arr, dp)

        dp[index][remaining] = ans1 or ans2
        return dp[index][remaining]

    def isSubsetSum_memo(self, arr, sum):
        n = len(arr)

        dp = [[-1 for _ in range(sum + 1)] for _ in range(len(arr))]
        solve = self.memoization(n - 1, sum, arr, dp)

        return solve







    #USING TABULATION
    def isSubsetSum_tabu(self, arr, sum):
        n = len(arr)

        dp = [[False for _ in range(sum + 1)] for _ in range(len(arr))]

        for index in range(0, n):
            dp[index][0] = True

        if arr[0] <= sum:
            dp[0][arr[0]] = True

        for index in range(1, n):
            for remaining in range(0, sum + 1):
                if arr[index] > remaining:
                    ans1 = False
                else:
                    ans1 = dp[index - 1][remaining - arr[index]]

                ans2 = dp[index - 1][remaining]

                dp[index][remaining] = ans1 or ans2

        return dp[n - 1][sum]
    
    
    
    
    
    
    
    # USING TABULATION WITH SPACE OPTIMIZATION
    def isSubsetSum_tabuSpaceOpt(self, arr, sum):
        n = len(arr)
        prev = [False for _ in range(sum+1)]
        
        prev[0] = True
        if arr[0] <= sum:
            prev[arr[0]] = True

        for index in range(1, n):
            curr = [False for _ in range(sum+1)]
            
            for remaining in range(0, sum + 1):
                if arr[index] > remaining:
                    ans1 = False
                else:
                    ans1 = prev[remaining - arr[index]]

                ans2 = prev[remaining]

                curr[remaining] = ans1 or ans2
            prev = curr.copy()
            
        return prev[sum]
    
    


obj = Solution()
arr = [3, 34, 4, 12, 5, 2]
K = 9
print(obj.isSubsetSum(arr, K))
print(obj.isSubsetSum_memo(arr, K))
print(obj.isSubsetSum_tabu(arr, K))
print(obj.isSubsetSum_tabuSpaceOpt(arr, K))

# Output : True