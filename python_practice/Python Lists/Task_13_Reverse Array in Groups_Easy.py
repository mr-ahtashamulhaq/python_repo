"""Given an array arr[] of positive integers. Reverse every sub-array group of size k.
Note: If at any instance, k is greater or equal to the array size, then reverse the entire array. """
class Solution:
    def reverseingroups(self, arr, k):
        result = []
        while(len(arr) != 0):
            temp = []
            j = 0
            while( j < k and j<= len(arr)):
                temp.append(arr.pop(0))
                j += 1
            temp.reverse()
            for i in temp:
                result.append(i)
        return result
    
obj = Solution()
k = 3
arr = [1, 2, 3, 4, 5]
print(obj.reverseingroups(arr,k))