"""Given an array arr[]. Find the majority element in the array. If no majority element exists, return -1.

Note: A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array."""
class Solution:
    def majorityElement(self, arr):
        majorel = -1
        tocheck = len(arr)//2
        for i in arr:
            if arr.count(i) > tocheck:
                majorel = i
        return majorel
obj = Solution()
arr = [1, 1, 2, 1, 3, 5, 1]
print(obj.majorityElement(arr))