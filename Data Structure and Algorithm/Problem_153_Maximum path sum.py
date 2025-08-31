"""A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path."""
from typing import Optional
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    total_sum = 0
    def checker (self, node ):
        if node==None:
            return 0

        #all left side sum
        left_sum = self.checker(node.left)

        # if left left_sum is negative make it zero because it will only decrease output
        if left_sum < 0:
            left_sum = 0

        #all right side sum
        right_sum = self.checker(node.right)

        #similarly if total right is negative make it zero
        if right_sum < 0:
            right_sum = 0

        self.total_sum = max(self.total_sum , (left_sum + right_sum + node.val))

        return  node.val + max(left_sum , right_sum)


    def maxPathSum(self, root: Optional[Node]) -> int:
        self.total_sum =float("-inf")
        self.checker(root)
        return self.total_sum       #type:ignore
    
obj = Solution()
l = [10,20,30,40,50,60,70]
root = Node(l[0])
root.left= Node((l[1]))
root.right= Node((l[2]))
root.left.left= Node((l[3]))                
root.left.right= Node((l[4]))              
root.right.left= Node((l[5]))               
root.right.right= Node((l[6]))

print(obj.maxPathSum(root))
# Output  : 180