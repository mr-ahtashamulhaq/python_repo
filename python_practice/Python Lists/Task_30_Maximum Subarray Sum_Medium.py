"""You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[]."""
class Solution:
    def maxSubarraySum(self, arr):
        maxsum = arr[0]
        currentsum = arr[0]

        for num in arr[1::]:
            currentsum = max(num , currentsum + num)
            maxsum = max(maxsum , currentsum)
        
        return maxsum
    
obj = Solution()
arr = [2, 3, -8, 7, -1, 2, 3]
print(obj.maxSubarraySum(arr))