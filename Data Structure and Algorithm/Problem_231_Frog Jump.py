"""Given an integer array height[] where height[i] represents the height of the i-th stair, a frog starts from the first stair and wants to reach the top. From any stair i, the frog has two options: it can either jump to the (i+1)th stair or the (i+2)th stair. The cost of a jump is the absolute difference in height between the two stairs. Determine the minimum total cost required for the frog to reach the top"""


class Solution:

    # USING RECURSION
    def recursion(self, heights, n):
        if n == 0:
            return 0
        if n == 1:
            return abs(heights[0] - heights[1])

        jump1 = self.recursion(heights, n - 1) + abs(heights[n - 1] - heights[n])
        jump2 = self.recursion(heights, n - 2) + abs(heights[n - 2] - heights[n])
        return min(jump1, jump2)

    def minCost(self, height):
        return self.recursion(height, len(height) - 1)
    
    
    
    
    

    # USING MEMOIZATION
    def memoization(self, heights, n, dp):
        if n == 0:
            return 0
        if n == 1:
            return abs(heights[0] - heights[1])

        if dp[n] != -1:
            return dp[n]

        jump1 = self.memoization(heights, n - 1, dp) + abs(heights[n - 1] - heights[n])
        jump2 = self.memoization(heights, n - 2, dp) + abs(heights[n - 2] - heights[n])

        dp[n] = min(jump1, jump2)

        return dp[n]

    def minCost_memo(self, height):
        dp = [-1 for _ in range(len(height))]
        return self.memoization(height, len(height) - 1, dp)
    
    
    
    
    

    # USING TABULATION
    def minCost_tabu(self, height):
        n = len(height)
        if n == 0 or n == 1:
            return 0

        dp = [-1 for _ in range(n)]
        dp[0] = 0
        dp[1] = abs(height[0] - height[1])

        for num in range(2, n):
            
            jump1 = dp[num - 1] + abs(height[num] - height[num - 1])
            jump2 = dp[num - 2] + abs(height[num - 2] - height[num])
            
            dp[num] = min(jump1, jump2)

        return dp[n - 1]
    
    
    
    
    

    # USING TABULATION WITH SPACE OPTIMIZATION
    def minCost_tabuSpaceOpt(self, height):
        n = len(height)
        if n == 0 or n == 1:
            return 0

        prev2 = 0
        prev = abs(height[0] - height[1])
        curr = 0

        for num in range(2, n):
            
            jump1 = prev + abs(height[num] - height[num - 1])
            jump2 = prev2 + abs(height[num - 2] - height[num])
            
            curr = min(jump1 , jump2)
            prev2 = prev
            prev = curr

        return prev


obj = Solution()
height = [20, 30, 40, 20]
print(obj.minCost(height))
print(obj.minCost_memo(height))
print(obj.minCost_tabu(height))
print(obj.minCost_tabuSpaceOpt(height))

# Output  : 20