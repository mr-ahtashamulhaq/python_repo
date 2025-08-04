"""You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too."""
class Solution:
    def missingNumber(self, arr):
        arr = sorted(set(arr))  
        smallest = 1
        
        for num in arr:
            if num <= 0:
                continue
            if num != smallest:
                return smallest
            smallest += 1
            
        return smallest 
    
obj = Solution()
arr =[2, -3, 4, 1, 1, 7]
print(obj.missingNumber(arr))