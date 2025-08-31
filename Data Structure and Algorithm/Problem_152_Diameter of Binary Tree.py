"""Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them."""

from typing import Optional
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #class-variable (make at class so we can edit it in all fuctions )
    diameter = 0
    def checker (self, node ):
        if node == None:
            return 0
        
        left_depth = self.checker(node.left)
        right_depth = self.checker(node.right)

        self.diameter = max(self.diameter , left_depth + right_depth)

        return  1 + max(left_depth , right_depth)
    
    def diameterOfBinaryTree(self, root: Optional[Node]) -> int:
        # Initialize diameter and start recursion
        self.diameter = 0
        self.checker(root)

        return self.diameter
obj = Solution()
l = [10,20,30,40,50,60,70]
root = Node(l[0])
root.left= Node((l[1]))
root.right= Node((l[2]))
root.left.left= Node((l[3]))                
root.left.right= Node((l[4]))              
root.right.left= Node((l[5]))               
root.right.right= Node((l[6]))

print(obj.diameterOfBinaryTree(root))
# Output : 4

