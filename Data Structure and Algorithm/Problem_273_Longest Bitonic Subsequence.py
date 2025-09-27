"""Given an array of positive integers. Find the maximum length of Bitonic subsequence.
A subsequence of array is called Bitonic if it is first strictly increasing, then strictly decreasing. Return the maximum length of bitonic subsequence.

Note : A strictly increasing or a strictly decreasing sequence should not be considered as a bitonic sequence
"""

from typing import List, Optional


class Solution:
    def LongestBitonicSequence(self, n: int, nums: List[int]) -> int:
        # code here
        dp1 = [1 for _ in range(n)]
        # 1) dp1[i] = length of LIS ending at i (strictly increasing)

        for index in range(n):
            for prev in range(0, index):
                if nums[index] > nums[prev]:
                    dp1[index] = max(dp1[index], 1 + dp1[prev])


        # 2) dp2[i] = length of LDS starting at i (strictly decreasing)
        dp2 = [1 for _ in range(n)]

        for index in range(n - 1, -1, -1):
            for prev in range(n - 1, index - 1, -1):
                if nums[index] > nums[prev]:
                    dp2[index] = max(dp2[index], 1 + dp2[prev])


        maxi = 0
        for i in range(n):
            # 3) Combine: only consider peaks that have both sides (dp1>1 and dp2>1)
            if dp1[i] > 1 and dp2[i] > 1:
                maxi = max(maxi, dp1[i] + dp2[i] - 1)

        return maxi


obj = Solution()
n = 9
nums = [1, 11, 2, 10, 4, 5, 2, 1, 12]
print(obj.LongestBitonicSequence(n, nums))

# Output : 6
