"""Given an array arr, you need to reverse a subarray of that array. The range of this subarray is given by indices l and r (1-based indexing)."""
#User function Template for python3
class Solution:
    def reverseSubArray(self,arr,l,r):
        # code here
        if l >= r:
            return arr
        else:
            arr[l-1], arr[r-1] = arr[r-1] ,arr[l-1]
            return Solution.reverseSubArray(self,arr, l+1, r-1)

arr = [1, 6, 7, 4]
l = 1
r = 4
obj = Solution()
print(obj.reverseSubArray(arr,l,r))
# Output: [4, 7, 6, 1]