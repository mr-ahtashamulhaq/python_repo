"""You're given an array (arr)
Return the frequency of element x in the given array"""
class Solution:
    def findFrequency(self, arr, x):
        # code here
        count = 0
        for i in arr:
            if i ==x:
                count +=1
        return count
    
obj = Solution()
arr = [1,2,5,3,6,7,7,7,4,3,6]
x = 3
print(obj.findFrequency(arr,x))
# Output : 2