"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""
class Solution:
    # USING RECURSION
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    
    
    

    # USING MEMOIZATION
    def memoization(self, n, dp):
        if n == 0 or n == 1:
            return 1
        if dp[n] != -1:
            return dp[n]

        dp[n] = self.memoization(n - 1, dp) + self.memoization(n - 2, dp)
        return dp[n]

    def climbStairs_memo(self, n):
        dp = [-1 for _ in range(n + 1)]

        return self.memoization(n, dp)
    
    
    

    # USING TABULATION
    def climbStairs_tabu(self, n):
        dp = [-1 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for num in range(2, n + 1):
            dp[num] = dp[num - 1] + dp[num - 2]

        return dp[n]
    
    
    

    # TABULATION WITH SPACE OPTIMIZATION
    def climbStairs_tabuSpaceOpt(self, n):
        prev = 1
        prev2 = 1
        curr = 1

        for num in range(2, n + 1):
            curr = prev + prev2
            prev2 = prev
            prev = curr

        return curr


obj = Solution()
print(obj.climbStairs(10))
print(obj.climbStairs_memo(10))
print(obj.climbStairs_tabu(10))
print(obj.climbStairs_tabuSpaceOpt(10))

# Ouput:
# 89
# 89
# 89
# 89
