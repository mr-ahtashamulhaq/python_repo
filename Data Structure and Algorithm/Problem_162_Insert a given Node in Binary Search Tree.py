"""You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them."""
from typing import Optional
class  Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[ Node], val: int) -> Optional[ Node]:
        val_node = Node(val)
        if root is None:
            return val_node

        temp = root
        
        while True:
            if val < temp.val:
                if temp.left is None:
                    temp.left = val_node
                    break
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = val_node
                    break
                temp = temp.right

        return root
    

obj = Solution()
arr = [3,9,17,36,5,24,8]
root = Node(arr[0])       # 3

root.right = Node(arr[1]) # 9
root.right.right = Node(arr[2]) # 17
root.right.right.right = Node(arr[3]) # 36
root.right.left = Node(arr[4])  # 5
root.right.right.right.left = Node(arr[5]) # 24
root.right.left.right = Node(arr[6]) # 8

print(obj.insertIntoBST(root,11))

# Output : <__main__.Node object at 0x000001FA82EF9400>