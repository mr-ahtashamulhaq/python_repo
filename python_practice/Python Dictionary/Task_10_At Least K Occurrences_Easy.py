"""Given an array arr. Return the element that occurs at least k number of times.

Note:
If there are multiple answers, please return the first one.
If there is no element found, return -1."""

class Solution:
    def elementAtLeastKTimes(self, arr, k):
        for i in range(len(arr)):
            if arr.count(arr[i]) >= k:
                return arr[i]
        return -1

obj = Solution()
print(obj.elementAtLeastKTimes([1, 2, 2, 3, 1], 2))