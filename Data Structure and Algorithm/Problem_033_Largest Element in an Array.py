"""Given an array arr[]. The task is to find the largest element and return it."""
class Solution:
    def largest(self, arr):
        # code here
        largest = float("-inf")
        n = len(arr)
        for i in range(n):
            largest = max(largest,arr[i])
        return largest
        
obj = Solution()
arr = [32,56,83,8,2,99]
print(obj.largest(arr))
# Output : 99