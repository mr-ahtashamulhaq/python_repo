# Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.
class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        n = len(arr)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
        return True
obj = Solution()
arr= [1,2,5,8,3,10,14,15]
arr1= [3,5,6,8,9,10,20]
print(obj.isSorted(arr)) # False
print(obj.isSorted(arr1)) #True