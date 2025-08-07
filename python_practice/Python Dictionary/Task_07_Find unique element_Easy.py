"""Given an array of elements occurring in multiples of k, except one element which doesn't occur in multiple of k. Return the unique element."""
class Solution:
    def find_unique(self, k, arr):
        for i in arr:
            if arr.count(i)%k != 0:
                return i
        return False
    
obj = Solution()
k = 3
arr= [6, 2, 5, 2, 2, 6, 6]
print(obj.find_unique(k,arr))