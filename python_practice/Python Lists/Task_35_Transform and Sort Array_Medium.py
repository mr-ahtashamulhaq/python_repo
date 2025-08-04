"""Given an integer array arr[] sorted in ascending order, along with three integers: A, B, and C. The task is to transform each element x in the array using the quadratic function A*(x2) + B*x + C. After applying this transformation to every element, return the modified array in sorted order."""
class Solution:
    def transformAndSort(self, arr, A, B, C):
        def f(x):
            return A * x * x + B * x + C
        
        result = [f(x) for x in arr]
        result.sort()
        return result
obj = Solution()
arr = [-4, -2, 0, 2, 4]
A=1
B=3
C=4
print(obj.transformAndSort(arr,A,B,C))