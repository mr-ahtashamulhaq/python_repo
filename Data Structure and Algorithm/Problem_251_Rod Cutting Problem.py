"""Given a rod of length n inches and an array price[], where price[i] denotes the value of a piece of length i. Your task is to determine the maximum value obtainable by cutting up the rod and selling the pieces.

Note: n = size of price, and price[] is 1-indexed array."""
class Solution:
    # USING RECURSION

    # Function Intuition: Maximum value obtainable using pieces up-to index 'index' (inclusive) with remaining rod length 'length'
    def recursion(self, index, length, price):
        if index == 0:
            return length * price[0]

        not_cut = self.recursion(index - 1, length, price)

        cut = float('-inf')
        rod_length = index + 1
        if rod_length <= length:
            cut = price[index] + self.recursion(index, length - rod_length, price)

        return max(cut, not_cut)

    def cutRod(self, price, n):
        return self.recursion(n - 1, n, price)





    # USING MEMOIZATION
    def memoization(self, index, length, price, dp):
        if index == 0:
            return length * price[0]

        if dp[index][length] != -1:
            return dp[index][length]

        not_cut = self.memoization(index - 1, length, price, dp)

        cut = float('-inf')
        rod_length = index + 1
        if rod_length <= length:
            cut = price[index] + self.memoization(index, length - rod_length, price, dp)

        dp[index][length] = max(cut, not_cut)
        return dp[index][length]

    def cutRod_memo(self, price, n):
        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
        return self.memoization(n - 1, n, price, dp)





    # USING TABULATION
    def cutRod_tabu(self, price, n):
        dp = [[0 for _ in range(n + 1)] for _ in range(n)]

        for length in range(n + 1):
            dp[0][length] = length * price[0]

        for index in range(1, n):
            for length in range(n + 1):
                not_cut = dp[index - 1][length]

                cut = float('-inf')
                rod_length = index + 1
                if rod_length <= length:
                    cut = price[index] + dp[index][length - rod_length]

                dp[index][length] = max(cut, not_cut)        #type: ignore

        return dp[n - 1][n]





    # USING TABULATION WITH SPACE OPTIMIZATION
    def cutRod_tabuSpaceOpt(self, price, n):
        prev = [0 for _ in range(n + 1)]

        for length in range(n + 1):
            prev[length] = length * price[0]

        for index in range(1, n):
            curr = [0 for _ in range(n + 1)]
            for length in range(n + 1):
                not_cut = prev[length]

                cut = float('-inf')
                rod_length = index + 1
                if rod_length <= length:
                    cut = price[index] + curr[length - rod_length]

                curr[length] = max(cut, not_cut)        #type: ignore
            prev = curr

        return prev[n]


obj = Solution()
price = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(price)
print(obj.cutRod(price, n))
print(obj.cutRod_memo(price, n))
print(obj.cutRod_tabu(price, n))
print(obj.cutRod_tabuSpaceOpt(price, n))

#Output : 22
