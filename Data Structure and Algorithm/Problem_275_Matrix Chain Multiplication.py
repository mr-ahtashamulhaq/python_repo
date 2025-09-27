"""Given an array arr[] which represents the dimensions of a sequence of matrices where the ith matrix has the dimensions (arr[i-1] x arr[i]) for i>=1, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications."""
class Solution:
    # USING RECURSION
    def recursion(self, i, j, arr):
        if i == j:
            return 0

        best = float("inf")
        for k in range(i, j):
            cost_left = self.recursion(i, k, arr)
            cost_right = self.recursion(k + 1, j, arr)

            cost_mult = arr[i - 1] * arr[k] * arr[j]  # MCM Formula

            total = cost_left + cost_right + cost_mult

            if total < best:
                best = total

        return best

    def matrixMultiplication(self, arr):

        n = len(arr) - 1  # number of matrices

        return self.recursion(1, n, arr)









    # USING MEMOIZATION
    def memoization(self, i, j, dp, arr):
        if i == j:
            return 0

        if dp[i][j] != 0:
            return dp[i][j]

        best = float("inf")
        for k in range(i, j):
            cost_left = self.memoization(i, k, dp, arr)
            cost_right = self.memoization(k + 1, j, dp, arr)

            cost_mult = arr[i - 1] * arr[k] * arr[j]

            total = cost_left + cost_right + cost_mult  # MCM Formula

            if total < best:
                best = total

        dp[i][j] = best
        return dp[i][j]

    def matrixMultiplication_memo(self, arr):
        # code here
        n = len(arr) - 1
        dp = [[0 for _ in range(n + 1)] for _ in range(n)]
        return self.memoization(1, n, dp, arr)









    # USING TABULATION
    def matrixMultiplication_tabu(self, arr):

        n = len(arr) - 1

        # dp[i][j]: minimum cost to multiply matrices i through j
        # We'll use 1-based indexing for matrices (so dp is (n+2)x(n+2) or at least size (n+1)x(n+1))
        dp = [[0] * (n + 2) for _ in range(n + 2)]


        # length = chain length (number of matrices in the subproblem)
        # from 2 to n (length = 1 means only one matrix, cost 0)
        for length in range(2, n + 1):
            
            # i is start of chain
            for i in range(1, n - length + 2):
                
                j = i + length - 1  # end of chain
                dp[i][j] = float("inf")         #type: ignore
                
                # try splitting between k = i .. j-1
                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost

        return dp[1][n]


obj = Solution()
arr = [40, 20, 30, 10, 30]
print(obj.matrixMultiplication(arr))
print(obj.matrixMultiplication_memo(arr))
print(obj.matrixMultiplication_tabu(arr))

# Output : 26000