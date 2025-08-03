"""You are given a sorted array arr[] containing positive integers. Your task is to remove all duplicate elements from this array such that each element appears only once. Return an array containing these distinct elements in the same order as they appeared."""
class Solution:
    def removeDuplicates(self, arr):
        return set(arr)
        

obj = Solution()
arr = [1,2,2,2,3,3,4]
print(obj.removeDuplicates(arr))