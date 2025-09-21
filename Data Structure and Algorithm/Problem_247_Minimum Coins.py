"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin."""
class Solution:
    
    # USING RECURSION
    def recursion(self, index, amount, coins):
        if index == 0:
            if amount % coins[index] == 0:
                return amount // coins[index]

            return float("inf")

        if coins[index] > amount:
            same_pick = float("inf")
        else:
            same_pick = 1 + self.recursion(index, amount - coins[index], coins)

        prev_pick = 0 + self.recursion(index - 1, amount, coins)

        return min(same_pick, prev_pick)

    def coinChange(self, coins, amount):

        n = len(coins)
        solve = self.recursion(n - 1, amount, coins)
        if solve != float("inf"):
            return solve
        return -1







    #USING MEMOIZATION
    def memoization(self, index, amount, coins, dp):

        if index == 0:
            if amount % coins[index] == 0:
                return amount // coins[index]

            return float("inf")

        if dp[index][amount] != -1:
            return dp[index][amount]

        if coins[index] > amount:
            same_pick = float("inf")
        else:
            same_pick = 1 + self.memoization(index, amount - coins[index], coins, dp)

        prev_pick = 0 + self.memoization(index - 1, amount, coins, dp)

        dp[index][amount] = min(same_pick, prev_pick)
        return dp[index][amount]

    def coinChange_memo(self, coins, amount):

        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        solve = self.memoization(n - 1, amount, coins, dp)
        if solve != float("inf"):
            return solve
        return -1






    # USING TABULATION
    def coinChange_tabu(self, coins, amount):

        n = len(coins)
        dp = [[float("inf") for _ in range(amount + 1)] for _ in range(n)]

        for amt in range(amount + 1):
            if amt % coins[0] == 0:
                dp[0][amt] = amt // coins[0]

        for index in range(1, n):
            for amt in range(0, amount + 1):
                if coins[index] > amt:
                    same_pick = float("inf")
                else:
                    same_pick = 1 + dp[index][amt - coins[index]]

                prev_pick = 0 + dp[index - 1][amt]

                dp[index][amt] = min(same_pick, prev_pick)

        if dp[n - 1][amount] != float("inf"):
            return dp[n - 1][amount]
        return -1







    #USING TABULATION WITH SOACE OPTIMIZATION
    def coinChange_tabuSpaceOpt(self, coins, amount):

        n = len(coins)
        prev = [float("inf") for _ in range(amount + 1)]
        
        for amt in range(amount + 1):
            if amt % coins[0] == 0:
                prev[amt] = amt // coins[0]

        for index in range(1, n):
            curr = [float("inf") for _ in range(amount + 1)]
            
            for amt in range(0, amount + 1):
                if coins[index] > amt:
                    same_pick = float("inf")
                else:
                    same_pick = 1 + curr[amt - coins[index]]

                prev_pick = 0 + prev[amt]

                curr[amt] = min(same_pick, prev_pick)
            prev = curr.copy()

        if prev[amount] != float("inf"):
            return prev[amount]
        return -1
    
    
obj = Solution()
coins = [1, 2, 5]
amount = 11
print(obj.coinChange(coins, amount))
print(obj.coinChange_memo(coins, amount))
print(obj.coinChange_tabu(coins, amount))
print(obj.coinChange_tabuSpaceOpt(coins, amount))
# Output : 3