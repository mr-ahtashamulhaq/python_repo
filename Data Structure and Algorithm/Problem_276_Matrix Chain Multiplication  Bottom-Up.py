"""Given an array arr[] which represents the dimensions of a sequence of matrices where the ith matrix has the dimensions (arr[i-1] x arr[i]) for i>=1, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications."""
class Solution:
    def matrixMultiplication_tabu(self, arr):
        n = len(arr) - 1
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for length in range(2, n + 2):

            for i in range(1, n - length + 2):
                j = i + length - 1

                dp[i][j] = float("inf")  # type: ignore
                for k in range(i, j):
                    cost = ( dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j] )  # MCM FORMULA

                    if cost < dp[i][j]:
                        dp[i][j] = cost

        return dp[1][n]


obj = Solution()
arr = [40, 20, 30, 10, 30]
print(obj.matrixMultiplication_tabu(arr))

# Output : 26000