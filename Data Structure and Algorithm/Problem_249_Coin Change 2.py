"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer."""
class Solution:
    # USING RECURSION

    # Function Intuition:Number of combinations to form amount using coins up-to index 'index' (inclusive)
    def recursion(self, index, amount, coins):
        if index == 0:
            if amount % coins[0] == 0:
                return 1
            return 0

        not_pick = self.recursion(index - 1, amount, coins)

        # pick current coin (only if coin <= amount)
        pick = 0
        if coins[index] <= amount:
            pick = self.recursion(index, amount - coins[index], coins)

        return pick + not_pick

    def change(self, amount: int, coins) -> int:
        n = len(coins)
        return self.recursion(n - 1, amount, coins)







    # USING MEMOIZATION
    def memoization(self, index, amount, coins, dp):
        if index == 0:
            if amount % coins[0] == 0:
                return 1
            return 0

        if dp[index][amount] != -1:
            return dp[index][amount]

        not_pick = self.memoization(index - 1, amount, coins, dp)

        # pick current coin (only if coin <= amount)
        pick = 0
        if coins[index] <= amount:
            pick = self.memoization(index, amount - coins[index], coins, dp)

        dp[index][amount] = pick + not_pick
        return dp[index][amount]

    def change_memo(self, amount: int, coins) -> int:

        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        return self.memoization(n - 1, amount, coins, dp)







    # USING TABULATION
    def change_tabu(self, amount: int, coins) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        for amt in range(amount + 1):
            if amt % coins[0] == 0:
                dp[0][amt] = 1
            else:
                dp[0][amt] = 0

        for index in range(1, n):
            for amt in range(amount + 1):
                not_pick = dp[index - 1][amt]

                pick = 0
                if coins[index] <= amt:
                    pick = dp[index][amt - coins[index]]

                dp[index][amt] = pick + not_pick

        return dp[n - 1][amount]







    #USING TABULATION WITH SPACE OPTIMIZATION
    def change_tabuSpaceOpt(self, amount: int, coins) -> int:
        n = len(coins)
        prev = [0 for _ in range(amount + 1)]

        for amt in range(amount + 1):
            if amt % coins[0] == 0:
                prev[amt] = 1
            else:
                prev[amt] = 0

        for index in range(1, n):
            curr = [0 for _ in range(amount + 1)]
            for amt in range(amount + 1):
                not_pick = prev[amt]

                pick = 0
                if coins[index] <= amt:
                    pick = curr[amt - coins[index]]

                curr[amt] = pick + not_pick
            prev = curr

        return prev[amount]


obj = Solution()
amount = 5
coins = [1, 2, 5]
print(obj.change(amount, coins))
print(obj.change_memo(amount, coins))
print(obj.change_tabu(amount, coins))
print(obj.change_tabuSpaceOpt(amount, coins))

# Output : 4