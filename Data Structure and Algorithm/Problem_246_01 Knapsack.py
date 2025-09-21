"""Given n items, each with a specific weight and value, and a knapsack with a capacity of W, the task is to put the items in the knapsack such that the sum of weights of the items <= W and the sum of values associated with them is maximized. 

Note: You can either place an item entirely in the bag or leave it out entirely. Also, each item is available in single quantity."""
class Solution:
    #USING RECURSION
    def recursion(self, index, remaining, val, wt):
        if index == 0:
            if remaining >= wt[0]:
                return val[0]
            return 0

        if wt[index] > remaining:
            pick = float("-inf")
        else:
            pick = val[index] + self.recursion( index - 1, remaining - wt[index], val, wt )
        not_pick = 0 + self.recursion(index - 1, remaining, val, wt)

        return max(pick, not_pick)

    def knapsack(self, W, val, wt):
        return self.recursion(len(val) - 1, W, val, wt)






    #USING MEMOIZATION
    def memoization(self, index, remaining, val, wt, dp):
        if index == 0:
            if remaining >= wt[0]:
                return val[0]
            return 0

        if dp[index][remaining] != -1:
            return dp[index][remaining]

        if wt[index] > remaining:
            pick = float("-inf")
        else:
            pick = val[index] + self.memoization (index - 1, remaining - wt[index], val, wt, dp)

        not_pick = 0 + self.memoization (index - 1, remaining, val, wt, dp)

        dp[index][remaining] = max(pick, not_pick)
        return dp[index][remaining]

    def knapsack_memo(self, W, val, wt):
        n = len(val)
        dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
        return self.memoization(n - 1, W, val, wt, dp)







    #USING TABULATION
    def knapsack_tabu(self, W, val, wt):
        n = len(val)
        dp = [[0 for _ in range(W + 1)] for _ in range(n)]

        for weight in range(0, W + 1):
            if weight >= wt[0]:
                dp[0][weight] = val[0]

        for index in range(1, n):
            for remaining in range(0, W + 1):
                if wt[index] > remaining:
                    pick = float("-inf")
                else:
                    pick = val[index] + dp[index - 1][remaining - wt[index]]
                not_pick = 0 + dp[index - 1][remaining]

                dp[index][remaining] = max(pick, not_pick)          #type: ignore

        return dp[n - 1][W]







    #USING TABULATION WITH SPACE OPTIMIZATION
    def knapsack_tabuSpaceOpt(self, W, val, wt):
        n = len(val)
        prev = [0 for _ in range(W + 1)]

        for weight in range(0, W + 1):
            if weight >= wt[0]:
                prev[weight] = val[0]

        for index in range(1, n):
            curr = [0 for _ in range(W + 1)]
            for remaining in range(0, W + 1):

                if wt[index] > remaining:
                    pick = float("-inf")
                else:
                    pick = val[index] + prev[remaining - wt[index]]
                not_pick = 0 + prev[remaining]

                curr[remaining] = max(pick, not_pick)          #type: ignore
            prev = curr.copy()
        return prev[W]


obj = Solution()
W = 4
val = [1, 2, 3]
wt = [4, 5, 1]
print(obj.knapsack(W, val, wt))
print(obj.knapsack_memo(W, val, wt))
print(obj.knapsack_tabu(W, val, wt))
print(obj.knapsack_tabuSpaceOpt(W, val, wt))

# Output : 3