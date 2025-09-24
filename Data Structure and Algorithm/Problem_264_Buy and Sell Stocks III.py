"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again)."""
class Solution:
    # USING RECURSION
    def recursion(self, index, buy_choice, prices, limit):
        n = len(prices)
        if index >= n:
            return 0
        if limit == 0:
            return 0

        if buy_choice == 1:  # mean it can buy
            buy = -prices[index] + self.recursion(index + 1, 0, prices, limit)
            not_buy = 0 + self.recursion(index + 1, 1, prices, limit)
            return max(buy, not_buy)

        else:  # cannot buy but have choice to sel or not
            sell = prices[index] + self.recursion(index + 1, 1, prices, limit - 1)
            not_sell = 0 + self.recursion(index + 1, 0, prices, limit)
            return max(sell, not_sell)

    def maxProfit(self, prices) -> int:
        return self.recursion(0, 1, prices, 2)








    # USING MEMOIZATION
    def memoization(self, index, buy_choice, prices, limit, dp):
        n = len(prices)
        if index >= n:
            return 0
        if limit == 0:
            return 0
        if dp[index][buy_choice][limit] != -1:
            return dp[index][buy_choice][limit]

        if buy_choice == 1:  # mean it can buy
            buy = -prices[index] + self.memoization(index + 1, 0, prices, limit, dp)
            not_buy = 0 + self.memoization(index + 1, 1, prices, limit, dp)
            profit = max(buy, not_buy)

        else:  # cannot buy but have choice to sel or not
            sell = prices[index] + self.memoization(index + 1, 1, prices, limit - 1, dp)
            not_sell = 0 + self.memoization(index + 1, 0, prices, limit, dp)
            profit = max(sell, not_sell)

        dp[index][buy_choice][limit] = profit
        return dp[index][buy_choice][limit]

    def maxProfit_memo(self, prices) -> int:
        n = len(prices)
        # DP  --> dp[index][buy_choice][limit]
        dp = [[[-1, -1, -1] for _ in range(2)] for _ in range(n)]
        return self.memoization(0, 1, prices, 2, dp)










    # USING TABULATION
    def maxProfit_tabu(self, prices) -> int:

        n = len(prices)
        dp = [[[-1, -1, -1] for _ in range(2)] for _ in range(n + 1)]

        # Base Case --> if index == n make it 0
        for buy in range(2):
            for limit in range(3):
                dp[n][buy][limit] = 0

        # Base Case --> if limit == n make it 0 --> No matter what is 'index' or 'buy' value is
        for index in range(n + 1):
            for buy in range(2):
                dp[index][buy][0] = 0

        for index in range(n - 1, -1, -1):
            for buy_choice in range(2):
                for limit in range(1, 3):

                    if buy_choice == 1:  # mean it can buy
                        buy = -prices[index] + dp[index + 1][0][limit]
                        not_buy = 0 + dp[index + 1][1][limit]
                        profit = max(buy, not_buy)

                    else:  # cannot buy but have choice to sel or not
                        sell = prices[index] + dp[index + 1][1][limit - 1]
                        not_sell = 0 + dp[index + 1][0][limit]
                        profit = max(sell, not_sell)

                    dp[index][buy_choice][limit] = profit
        return dp[0][1][2]










    # USING TABULATION WITH SPACE OPTIMIZATION
    def maxProfit_tabuSpaceOpt(self, prices) -> int:

        n = len(prices)
        ahead = [[-1, -1, -1] for _ in range(2)]

        # Base Case --> if index == n make it 0
        for buy in range(2):
            for limit in range(3):
                ahead[buy][limit] = 0

        # Base Case --> if limit == n make it 0 --> No matter what is 'index' or 'buy' value is
        for buy in range(2):
            ahead[buy][0] = 0

        for index in range(n - 1, -1, -1):
            curr = [[-1, -1, -1] for _ in range(2)]
            for buy_choice in range(2):
                for limit in range(0, 3):

                    if limit == 0:
                        profit = 0

                    elif buy_choice == 1:  # mean it can buy
                        buy = -prices[index] + ahead[0][limit]
                        not_buy = 0 + ahead[1][limit]
                        profit = max(buy, not_buy)

                    else:  # cannot buy but have choice to sel or not
                        sell = prices[index] + ahead[1][limit - 1]
                        not_sell = 0 + ahead[0][limit]
                        profit = max(sell, not_sell)

                    curr[buy_choice][limit] = profit
            ahead = curr.copy()
        return ahead[1][2]


obj = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(obj.maxProfit(prices))
print(obj.maxProfit_memo(prices))
print(obj.maxProfit_tabu(prices))
print(obj.maxProfit_tabuSpaceOpt(prices))

# Output : 6