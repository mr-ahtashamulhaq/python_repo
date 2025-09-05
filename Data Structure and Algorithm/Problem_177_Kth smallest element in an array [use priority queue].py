"""Given an array arr[] and an integer k where k is smaller than the size of the array, your task is to find the kth smallest element in the given array.

Follow up: Don't solve it using the inbuilt sort function."""

import heapq
class Solution:

    def kthSmallest(self, arr,k):
        ans = []
        n = len(arr)
        
        for i in range(k):
            heapq.heappush(ans, -arr[i])
            
            
        for i in range(k , n):
            if arr[i] < -ans[0]:
                heapq.heappop(ans)
                heapq.heappush(ans, -arr[i])
        return -ans[0]
    
obj = Solution()
arr = nums = [3,2,3,1,2,4,5,5,6]; k = 4
print(obj.kthSmallest(arr , k))
# Output  : 3