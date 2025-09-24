"""You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold than one share of the stock.

Find and return the maximum profit you can achieve."""
class Solution:
    def recursion(self, index, buy_choice, prices):
        n = len(prices)
        if index >= n:
            return 0

        if buy_choice == 1:  # mean it can buy
            buy = -prices[index] + self.recursion(index + 1, 0, prices)
            not_buy = 0 + self.recursion(index + 1, 1, prices)
            return max(buy, not_buy)

        else:  # cannot buy but have choice to sel or not
            sell = prices[index] + self.recursion(index + 1, 1, prices)
            not_sell = 0 + self.recursion(index + 1, 0, prices)
            return max(sell, not_sell)

    def maxProfit(self, prices) -> int:
        return self.recursion(0, 1, prices)
    
    
    
    
    
    
    
    

    # USING MEMOIZATION
    def memoization(self, index, buy_choice, prices, dp):
        n = len(prices)
        if index >= n:
            return 0

        if dp[index][buy_choice] != -1:
            return dp[index][buy_choice]

        if buy_choice == 1:  # mean it can buy
            buy = -prices[index] + self.memoization(index + 1, 0, prices, dp)
            not_buy = 0 + self.memoization(index + 1, 1, prices, dp)
            profit = max(buy, not_buy)

        else:  # cannot buy but have choice to sel or not
            sell = prices[index] + self.memoization(index + 1, 1, prices, dp)
            not_sell = 0 + self.memoization(index + 1, 0, prices, dp)
            profit = max(sell, not_sell)

        dp[index][buy_choice] = profit
        return dp[index][buy_choice]

    def maxProfit_memo(self, prices) -> int:
        n = len(prices)

        # DP will store dp[index][buy_choice] --> at this index with this buy value what would be highest profit
        dp = [[-1, -1] for _ in range(n)]  # [-1, -1] --> [buy=0 , buy=1]
        return self.memoization(0, 1, prices, dp)









    # USING TABULATION
    def maxProfit_tabu(self, prices) -> int:
        n = len(prices)
        # DP will be size of n+1 because we have to store base case --> if index = n --> ans will 0
        dp = [[-1, -1] for _ in range(n + 1)]

        # both index (buy / buy_not) will be zero
        dp[n][0] = 0
        dp[n][1] = 0

        for index in range(n - 1, -1, -1):
            for buy_choice in range(0, 2):
                if buy_choice == 1:
                    buy = -prices[index] + dp[index + 1][0]
                    not_buy = 0 + dp[index + 1][1]
                    profit = max(buy, not_buy)

                else:  # cannot buy but have choice to sel or not
                    sell = prices[index] + dp[index + 1][1]
                    not_sell = 0 + dp[index + 1][0]
                    profit = max(sell, not_sell)
                dp[index][buy_choice] = profit

        return dp[0][1]
    
    
    
    
    
    
    
    

    # USING TABULATION WITH SPACE OPTIMIZATION
    def maxProfit_tabuSpaceOpt(self, prices) -> int:
        n = len(prices)

        ahead = [-1, -1]

        ahead[0] = 0
        ahead[1] = 0

        for index in range(n - 1, -1, -1):
            curr = [0, 0]
            for buy_choice in range(0, 2):
                if buy_choice == 1:
                    buy = -prices[index] + ahead[0]
                    not_buy = 0 + ahead[1]
                    profit = max(buy, not_buy)

                else:  # cannot buy but have choice to sel or not
                    sell = prices[index] + ahead[1]
                    not_sell = 0 + ahead[0]
                    profit = max(sell, not_sell)

                curr[buy_choice] = profit
            ahead = curr.copy()

        return ahead[1]


obj = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(obj.maxProfit(prices))
print(obj.maxProfit_memo(prices))
print(obj.maxProfit_tabu(prices))
print(obj.maxProfit_tabuSpaceOpt(prices))

# Output : 7