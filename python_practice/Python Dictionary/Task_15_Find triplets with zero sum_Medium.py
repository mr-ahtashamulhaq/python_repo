"""Given an array arr[] of integers, determine whether it contains a triplet whose sum equals zero. Return true if such a triplet exists, otherwise, return false."""
from itertools import combinations

class Solution:
    def hasTripletWithZeroSum(self, arr):
        for triplet in combinations(arr, 3):
            if sum(triplet) == 0:
                return True
        return False

obj = Solution()
arr = [0, -1, 2, -3, 1]
print(obj.hasTripletWithZeroSum(arr))