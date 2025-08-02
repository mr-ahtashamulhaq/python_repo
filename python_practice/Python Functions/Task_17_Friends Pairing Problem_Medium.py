"""Given n friends, each one can remain single or can be paired up with some other friend. Each friend can be paired only once. Find out the total number of ways in which friends can remain single or can be paired up."""
class Solution:
    def count_friend_pairings(self,n):
        if n == 0 or n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        print(dp)
    
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]
            print(dp)
    
        return dp[n]

obj = Solution()
print(obj.count_friend_pairings(3))
