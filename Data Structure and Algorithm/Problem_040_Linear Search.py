"""Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist."""

class Solution:
    def search(self, arr, x):
        # code here
        index  = -1
        for j,i in enumerate(arr):
            if i == x:
                index = j
                break
        return index
    
obj = Solution()
arr = [1, 2, 3, 4]
x = 3
print(obj.search(arr,x))
# Output : 2
