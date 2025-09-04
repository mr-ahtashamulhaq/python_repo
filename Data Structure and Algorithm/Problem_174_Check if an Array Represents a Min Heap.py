"""
Given an array `arr` representing a complete binary tree, 
determine whether it satisfies the **Min-Heap property** or the **Max-Heap property**.

Min-Heap:
- Every parent node must be less than or equal to its children.

Max-Heap:
- Every parent node must be greater than or equal to its children.
"""
class Solution:
    def checkMin(self, arr):
        n = len(arr)

        for ind in range(n//2):
            left_child = 2 * ind +1
            right_child = 2 * ind +2
            if left_child < n and arr[ind] > arr[left_child]:
                return False
            if right_child < n  and arr[ind] >  arr[right_child]:
                return False
        return True

    def checkMax(self, arr):
        n = len(arr)
        for ind in range(n//2):
            left_child = 2 * ind +1
            right_child = 2 * ind +2
            if left_child < n and arr[ind] < arr[left_child]:
                return False
            if right_child < n  and arr[ind] <  arr[right_child]:
                return False
        return True

obj = Solution()
arr = [10, 15, 20, 17, 25]

print(obj.checkMin(arr)) 
print(obj.checkMax(arr))
# True
# False