"""Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. """
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        totalwater = 0

        for i in range(1, n - 1):
            leftmax = max(arr[:i])
            rightmax = max(arr[i+1:])

            minwall = min(leftmax, rightmax)
            if minwall > arr[i]:
                totalwater += minwall - arr[i]

        return totalwater

obj = Solution()
arr = [3, 0, 1, 0, 4, 0, 2]
print( obj.maxWater(arr))