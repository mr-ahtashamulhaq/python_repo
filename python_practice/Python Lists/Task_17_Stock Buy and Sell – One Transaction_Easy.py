"""Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.
Note: Stock must be bought before being sold."""
class Solution:
    def maximumProfit(self, prices):
        index = 0
        lowest = prices[0]
        for j,i in enumerate(prices):
            if lowest >i:
                lowest = i
                index = j
        selling = 0
        for i in range(index,len(prices)):
            if prices[i]>selling:
                selling = prices[i]
        
        return 0 if selling==0 else selling-lowest

obj = Solution()
arr = [7, 10, 1, 3, 6, 9, 2]
print(obj.maximumProfit(arr))