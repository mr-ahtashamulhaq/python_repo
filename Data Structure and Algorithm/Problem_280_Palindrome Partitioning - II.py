"""Given a string s, partition s such that every of the partition is a Return the minimum cuts needed for a palindrome partitioning of s."""


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        dp = [0] * n
        for i in range(n):
            if pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = min(dp[j] + 1 for j in range(i) if pal[j + 1][i])
        return dp[-1]


obj = Solution()
s = "aab"
print(obj.minCut(s))

# Output : 1