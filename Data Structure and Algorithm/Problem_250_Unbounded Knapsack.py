"""Given a set of items, each with a weight and a value, represented by the array wt and val respectively. Also, a knapsack with a weight limit capacity.
The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.
Note: Each item can be taken any number of times."""
class Solution:
    # USING RECURSION
    #maximum profit we can achieve using items from 0...index with remaining knapsack capacity -->capacity
    
    def recursion(self, index, capacity, val, wt):
        if index == 0:
            return (capacity // wt[0]) * val[0]

        not_take = self.recursion(index - 1, capacity, val, wt)
        take = float('-inf')
        if wt[index] <= capacity:
            take = val[index] + self.recursion(index, capacity - wt[index], val, wt)

        return max(take, not_take)

    def knapSack(self, val, wt, W):
        n = len(wt)
        return self.recursion(n - 1, W, val, wt)





    # USING MEMOIZATION
    def memoization(self, index, capacity, val, wt, dp):
        if index == 0:
            return (capacity // wt[0]) * val[0]

        if dp[index][capacity] != -1:
            return dp[index][capacity]

        not_take = self.memoization(index - 1, capacity, val, wt, dp)
        take = float('-inf')
        if wt[index] <= capacity:
            take = val[index] + self.memoization(index, capacity - wt[index], val, wt, dp)

        dp[index][capacity] = max(take, not_take)
        return dp[index][capacity]

    def knapSack_memo(self, val, wt, W):
        n = len(wt)
        dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
        return self.memoization(n - 1, W, val, wt, dp)






    # USING TABULATION
    def knapSack_tabu(self, val, wt, W):
        n = len(wt)
        dp = [[0 for _ in range(W + 1)] for _ in range(n)]

        for cap in range(W + 1):
            if wt[0] <= cap:
                dp[0][cap] = (cap // wt[0]) * val[0]

        for index in range(1, n):
            for cap in range(W + 1):
                not_take = dp[index - 1][cap]
                take = 0
                if wt[index] <= cap:
                    take = val[index] + dp[index][cap - wt[index]]
                dp[index][cap] = max(take, not_take)

        return dp[n - 1][W]






    # USING TABULATION WITH SPACE OPTIMIZATION
    def knapSack_tabuSpaceOpt(self, val, wt, W):
        n = len(wt)
        dp = [0 for _ in range(W + 1)]

        for cap in range(W + 1):
            if wt[0] <= cap:
                dp[cap] = (cap // wt[0]) * val[0]

        for index in range(1, n):
            for cap in range(W + 1):
                not_take = dp[cap]
                take = 0
                if wt[index] <= cap:
                    take = val[index] + dp[cap - wt[index]]
                dp[cap] = max(take, not_take)

        return dp[W]


obj = Solution()
val = [15, 14, 10, 45, 30]
wt = [2, 5, 1, 3, 4]
W = 7
print(obj.knapSack(val, wt, W))
print(obj.knapSack_memo(val, wt, W))
print(obj.knapSack_tabu(val, wt, W))
print(obj.knapSack_tabuSpaceOpt(val, wt, W))

# Output : 100