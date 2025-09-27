"""Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:

Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts."""
from typing import List
class Solution:
    # USING RECURSION
    def recursion(self, l, r, cuts, n):
        if r - l == 1:
            return 0

        result = float("inf")
        for c in cuts:
            if l < c < r:
                result = min(
                    result,
                    (
                        (r - l)
                        + self.recursion(l, c, cuts, n)
                        + self.recursion(c, r, cuts, n)
                    ),
                )

        result = 0 if result == float("inf") else result
        return result

    def minCost(self, n: int, cuts: List[int]):
        return self.recursion(0, n, cuts, n)

    # USING MEMOIZATION
    def memoization(self, l, r, cuts, n, dp):
        if r - l == 1:
            return 0

        if dp[l][r] != -1:
            return dp[l][r]

        result = float("inf")
        for c in cuts:
            if l < c < r:
                result = min(
                    result,
                    (
                        (r - l)
                        + self.memoization(l, c, cuts, n, dp)
                        + self.memoization(c, r, cuts, n, dp)
                    ),
                )

        result = 0 if result == float("inf") else result
        dp[l][r] = result
        return dp[l][r]

    def minCost_memo(self, n: int, cuts: List[int]) -> int:
        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
        return self.memoization(0, n, cuts, n, dp)


obj = Solution()
n = 7
cuts = [1, 3, 4, 5]
print(obj.minCost(n, cuts))
print(obj.minCost_memo(n, cuts))

# Output : 16