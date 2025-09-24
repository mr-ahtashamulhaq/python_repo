"""You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

    You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
    The transaction fee is only charged once for each stock purchase and sale."""
class Solution:
    # USING RECURSION
    def recursion(self, index, buy_choice, prices, fee):
        n = len(prices)
        if index >= n:
            return 0

        if buy_choice == 1:  # mean it can buy
            buy = -prices[index] + self.recursion(index + 1, 0, prices, fee)
            not_buy = 0 + self.recursion(index + 1, 1, prices, fee)
            return max(buy, not_buy)

        else:  # cannot buy but have choice to sel or not
            sell = prices[index] - fee + self.recursion(index + 1, 1, prices, fee)
            not_sell = 0 + self.recursion(index + 1, 0, prices, fee)
            return max(sell, not_sell)

    def maxProfit(self, prices, fee) -> int:
        return self.recursion(0, 1, prices, fee) 
    
    
    
    
    
    
    
    
    # USING MEMOIZATION
    def memoization(self, index, buy_choice, prices, dp, fee):
        n = len(prices)
        if index >= n:
            return 0

        if dp[index][buy_choice] != -1:
            return dp[index][buy_choice]

        if buy_choice == 1:  # mean it can buy
            buy = -prices[index] + self.memoization(index + 1, 0, prices, dp, fee)
            not_buy = 0 + self.memoization(index + 1, 1, prices, dp, fee)
            profit = max(buy, not_buy)

        else:  
            sell = prices[index] - fee + self.memoization(index + 1, 1, prices, dp, fee)
            not_sell = 0 + self.memoization(index + 1, 0, prices, dp, fee)
            profit = max(sell, not_sell)

        dp[index][buy_choice] = profit
        return dp[index][buy_choice]

    def maxProfit_memo(self, prices, fee) -> int:
        n = len(prices)

  
        dp = [[-1, -1] for _ in range(n)]  # [-1, -1] --> [buy=0 , buy=1]
        return self.memoization(0, 1, prices, dp, fee)
    
    
    
    
    
    
    
    
    # USING TABULATION
    def maxProfit_tabu(self, prices, fee) -> int:
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
                    sell = prices[index] - fee + dp[index + 1][1]
                    not_sell = 0 + dp[index + 1][0]
                    profit = max(sell, not_sell)
                dp[index][buy_choice] = profit

        return dp[0][1]
    
    
    
    
    
    
    
    
    # USING TABULATION WITH SPACE OPTIMIZATION
    def maxProfit_tabuSpaceOpt(self, prices, fee) -> int:
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
                    sell = prices[index] - fee + ahead[1]
                    not_sell = 0 + ahead[0]
                    profit = max(sell, not_sell)

                curr[buy_choice] = profit
            ahead = curr.copy()

        return ahead[1]


obj = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(obj.maxProfit(prices, fee))
print(obj.maxProfit_memo(prices, fee))
print(obj.maxProfit_tabu(prices, fee))
print(obj.maxProfit_tabuSpaceOpt(prices, fee))

# Output : 8