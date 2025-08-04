"""Given an array arr[] consisting of n integers, the task is to find all the array elements which occurs more than floor(n/3) times.

Note: The returned array of majority elements should be sorted."""
class Solution:
    def majorityElement(self, arr):
        majorel = -1
        result = []
        tocheck = len(arr)//3
        for i in arr:
            if arr.count(i) > tocheck and i not in result:
                result.append(i)
        return result
obj = Solution()
arr = [2, 2, 3, 1, 3, 2, 1, 1]
print(obj.majorityElement(arr))