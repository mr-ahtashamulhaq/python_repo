"""Given an array of integers, arr[]. Find if there is a subarray (of size at least one) with 0 sum. Return true/false depending upon whether there is a subarray present with 0-sum or not. """

class Solution:
    def subArrayWithZeroSum(self, arr):
        for i in range(len(arr)):
            total = 0
            for j in range(i, len(arr)):
                total += arr[j]
                if total == 0:
                    return True
        return False

obj = Solution()
arr = [4, 2, -3, 1, 6]
print(obj.subArrayWithZeroSum(arr)) 