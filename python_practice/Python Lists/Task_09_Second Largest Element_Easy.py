"""Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1."""
class Solution:
    def getSecondLargest(self, arr):
        highest = 0
        highest2nd = -1
        for i in arr:
            if i>highest:
                highest = i
    
        for j,i in enumerate(arr):
            if i == highest:
                continue
            elif i>highest2nd:
                highest2nd = i
        return highest2nd

          
obj = Solution()
arr = [12,3,6,8,5,15]
print(obj.getSecondLargest(arr))