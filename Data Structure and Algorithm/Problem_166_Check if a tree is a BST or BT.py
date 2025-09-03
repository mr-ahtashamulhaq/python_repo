"""Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees."""
from typing import Optional
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solver  (self ,root,  limit ):
        if root == None:
            return True
        if limit[0] < root.val < limit[1]:
            left = self.solver(root.left , [limit[0] , root.val])
            if left ==False:
                return False
            else:
                right = self.solver(root.right ,[root.val ,limit[1]])
        else:
            return False

        return left and right

    def isValidBST(self, root: Optional[Node]) -> bool:
        limit = [float("-inf") , float("inf")]
        return self.solver(root, limit)
    
obj = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node4.left = node2
node4.right = node6
node2.left = node1
node2.right = node3
node6.left = node5
node6.right = node7

root = node4
print(obj.isValidBST(root))
# Output : True