"""Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node."""
from typing import Optional
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[Node], key: int) -> Optional[Node]:
        if root is None:
            return None

        if root.val == key:
            return self.deletion(root)
        temp = root
        while temp is not None:
            if temp.val > key:
                if temp.left is not None and temp.left.val==key:
                    temp.left = self.deletion(temp.left)
                    break
                else:
                    temp = temp.left

            else:
                if temp.right is not None and temp.right.val  == key:
                    temp.right = self.deletion (temp.right)
                    break

                else:
                    temp = temp.right
        return root
    
    def deletion(self, node):
        if node.left is None:
            return node.right
        
        elif node.right is None:
            return node.left
        
        else:

            right_child = node.right
            last_right_child = self.lastRightChild(node.left)
            last_right_child.right = right_child
            return node.left

    def lastRightChild(self, node : Node):
        while node.right is not None:
            node = node.right
        return node

obj = Solution()
arr = [3,9,17,36,5,24,8]
root = Node(arr[0])       # 3

root.right = Node(arr[1]) # 9
root.right.right = Node(arr[2]) # 17
root.right.right.right = Node(arr[3]) # 36
root.right.left = Node(arr[4])  # 5
root.right.right.right.left = Node(arr[5]) # 24
root.right.left.right = Node(arr[6]) # 8

print((obj.deleteNode(root, 17)).val)           #type: ignore
# Output : 3