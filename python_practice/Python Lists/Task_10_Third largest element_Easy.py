"""Given an array, arr of positive integers. Find the third largest element in it. Return -1 if the third largest element is not found."""
class Solution:
    def getthirdLargest(self, arr):
        highest = 0
        highest2nd = -1
        highestthird = -1
        for i in arr:
            if i>highest:
                highest = i
    
        for j,i in enumerate(arr):
            if i == highest:
                continue
            elif i>highest2nd:
                highest2nd = i

        for i in arr:
            if i == highest or i==highest2nd:
                continue
            elif i>highestthird:
                highestthird = i

        return highestthird

          
obj = Solution()
arr = [12,3,6,8,5,15]
print(obj.getthirdLargest(arr))