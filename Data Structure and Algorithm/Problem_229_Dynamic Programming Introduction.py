"""Given a non-negative integer n, your task is to find the nth Fibonacci number.

The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21

The Fibonacci sequence is defined as follows:

    F(0) = 0
    F(1) = 1
    F(n) = F(n - 1) + F(n - 2) for n > 1
"""
class Solution:

    # USING RECURSION
    def nthFib_recursion(self, n: int) -> int:
        # code here
        if n == 0 or n == 1:
            return n

        return self.nthFib_recursion(n - 1) + self.nthFib_recursion(n - 2)
    
    
    
    

    # USING MEMOIZATION --> its helper recursive function
    def memoization(self, dp, n):
        if n == 0 or n == 1:
            return n

        if dp[n] != -1:
            return dp[n]

        dp[n] = self.memoization(dp, n - 2) + self.memoization(dp, n - 1)
        return dp[n]
    
    # Main memoization
    def nthFib_memoization(self, n):
        dp = [-1 for _ in range(n + 1)]

        return self.memoization(dp, n)
    
    
    

    # USING TABULATION
    def nthFib_tabulation(self, n):
        dp = [-1 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1

        for num in range(2, n + 1):
            dp[num] = dp[num - 2] + dp[num - 1]

        return dp[n]
    
    

    
    # USING TABULATION with Constant Space
    def nthFib_tabulation_SpaceOptimized(self, n):
        prev = 1
        prev2 = 0
        curr = -1

        for num in range(2, n + 1):
            curr = prev2 + prev
            prev2 = prev
            prev = curr
        return curr


obj = Solution()
print(obj.nthFib_recursion(8))
print(obj.nthFib_memoization(8))
print(obj.nthFib_tabulation(8))
print(obj.nthFib_tabulation_SpaceOptimized(8))

# Output :
# 21
# 21
# 21
# 21