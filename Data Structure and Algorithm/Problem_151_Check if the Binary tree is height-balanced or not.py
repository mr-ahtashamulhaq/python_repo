"""Given a binary tree, determine if it is height-balanced.
Note : A 'height-balanced' binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.    """

from typing import Optional
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checker(self, root):
        if root is None:
            return 0   

        left_depth = self.checker(root.left)
        # if left is un-balanced no need to check further
        if left_depth == -1:
            return -1

        right_depth = self.checker(root.right)
        # if right is un-balanced no need to check further
        if right_depth ==-1:
            return -1
        # if this one is unbalanced no need to check further
        if abs(left_depth - right_depth ) > 1:
            return -1

        return 1 + max(left_depth, right_depth)

    def isBalanced(self, root: Optional[Node]) -> bool:
        result = self.checker(root)
        return False if result == -1 else True
        
obj = Solution()
l = [10,20,30,40,50,60,70]
root = Node(l[0])
root.left= Node((l[1]))
root.right= Node((l[2]))
root.left.left= Node((l[3]))                
root.left.right= Node((l[4]))              
root.right.left= Node((l[5]))               
root.right.right= Node((l[6]))

print(obj.isBalanced(root))
# Output : True