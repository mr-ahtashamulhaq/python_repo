"""Geek is going for a training program for n days. He can perform any of these activities: Running, Fighting, and Learning Practice. Each activity has some point on each day. As Geek wants to improve all his skills, he can't do the same activity on two consecutive days. Given a 2D array arr[][] of size n where arr[i][0], arr[i][1], and arr[i][2] represent the merit points for Running, Fighting, and Learning on the i-th day, determine the maximum total merit points Geek can achieve ."""
class Solution:
    #USING RECURSION
    def recursion(self, index, last, arr):
        if index == 0:
            maxi = 0
            for i in range(0, 3):
                if i != last:
                    maxi = max(maxi, arr[index][i])
            return maxi

        maxi = 0
        for i in range(0, 3):

            if i != last:
                maxi = max(maxi, arr[index][i] + self.recursion(index - 1, i, arr))
        return maxi

    def maximumPoints(self, arr):
        n = len(arr)
        return self.recursion(n - 1, 3, arr)





    #USING MEMOIZATION
    def memoization(self, index, last, arr, dp):
        if index == 0:
            maxi = 0
            for i in range(0, 3):
                if i != last:
                    maxi = max(maxi, arr[index][i])
            return maxi

        if dp[index][last] != -1:
            return dp[index][last]
        maxi = 0

        for i in range(0, 3):
            if i != last:
                maxi = max(
                    maxi, arr[index][i] + self.memoization(index - 1, i, arr, dp))

        dp[index][last] = maxi
        return dp[index][last]

    def maximumPoints_memo(self, arr):
        n = len(arr)
        rows = len(arr)
        dp = [[-1, -1, -1, -1] for _ in range(rows)]
        return self.memoization(n - 1, 3, arr, dp)





    #USING TABULATION
    def maximumPoints_tabu(self, arr):
        n = len(arr)
        dp = [[-1, -1, -1, -1] for _ in range(n)]

        dp[0][0] = max(arr[0][1], arr[0][2])
        dp[0][1] = max(arr[0][0], arr[0][2])
        dp[0][2] = max(arr[0][0], arr[0][1])
        dp[0][3] = max(arr[0][0], arr[0][1], arr[0][2])

        for index in range(1, n):
            for last in range(0, 4):

                maxi = 0
                for i in range(0, 3):
                    if i != last:
                        maxi = max(maxi, arr[index][i] + dp[index - 1][i])

                dp[index][last] = maxi

        return dp[n - 1][3]






    #USING TABULATION WITH SPACE OPTIMIZATION
    def maximumPoints_tabuSapceOpt(self, arr):
        prev = [-1, -1, -1, -1]
        n = len(arr)
        prev[0] = max(arr[0][1], arr[0][2])
        prev[1] = max(arr[0][0], arr[0][2])
        prev[2] = max(arr[0][0], arr[0][1])
        prev[3] = max(arr[0][0], arr[0][1], arr[0][2])

        for index in range(1, n):
            curr = [0, 0, 0, 0]
            for last in range(0, 4):

                maxi = 0
                for i in range(0, 3):
                    if i != last:
                        maxi = max(maxi, arr[index][i] + prev[i])

                curr[last] = maxi
            prev = curr.copy()

        return prev[3]



obj = Solution()
arr = [[1, 2, 5], [3, 1, 1], [3, 3, 3]]
print(obj.maximumPoints(arr))
print(obj.maximumPoints_memo(arr))
print(obj.maximumPoints_tabu(arr))
print(obj.maximumPoints_tabuSapceOpt(arr))

# Output  : 11