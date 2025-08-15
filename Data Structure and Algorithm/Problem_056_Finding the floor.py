"""Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element in arr[] that is less than or equal to x. This element is called the floor of x. If such an element does not exist, return -1.

Note: In case of multiple occurrences of ceil of x, return the index of the last occurrence."""
class Solution:
    def findFloor(self, arr, x):
        n = len(arr)
        ans = -1
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                ans = mid 
                low = mid + 1
            else:
                high = mid - 1
        
        return ans

    
obj = Solution()
arr = [1, 2, 8, 10, 10, 12, 19]
x = 80
print(obj.findFloor(arr,x))
# output : 6
