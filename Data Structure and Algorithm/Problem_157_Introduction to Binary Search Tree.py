"""Given an array of integers arr[] representing inorder traversal of elements of a binary tree. Return true if the given inorder traversal can be of a valid Binary Search Tree.

Note - In a valid Binary Search Tree all keys are unique."""
class Solution:
    def isBSTTraversal(self, arr):
        
        for i in range(1 , len(arr)):
            
            if arr[i] <= arr[i-1]:
                return False
        return True
        
        
obj  = Solution()
arr = [8, 14, 45, 64, 100]
print(obj.isBSTTraversal(arr))
# Output : True