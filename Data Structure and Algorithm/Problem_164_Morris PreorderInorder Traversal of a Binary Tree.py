"""Given the root of a binary tree, return the 'inorder traversal' and 'Pre-order traversal' of its nodes' values."""

from typing import Optional, List
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def morrisAlgorithm_inorder(self, root: Optional[Node]) -> List[int]:

        result = []
        current = root

        while current is not None:
            if current.left is None:
                result.append(current.val)
                current= current.right
            else:
                predecessor = current.left

                while predecessor.right is not None and predecessor.right != current:
                    predecessor= predecessor.right
                
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    #Append in else condition in in-order
                    result.append(current.val)
                    current  =current.right
        return result 


    def morrisAlgorithm_preorder(self, root: Optional[Node]) -> List[int]:

        result = []
        current = root

        while current is not None:
            if current.left is None:
                result.append(current.val)
                current= current.right
            else:
                predecessor = current.left

                while predecessor.right is not None and predecessor.right != current:
                    predecessor= predecessor.right
                
                if predecessor.right is None:
                    #Append in if condition in pre-order
                    result.append(current.val)
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    current  =current.right

        return result
    
node1 = Node(1)
node2 = Node(2)
node7 = Node(7)
node3 = Node(3)
node4 = Node(4)
node8 = Node(8)
node9 = Node(9)
node5 = Node(5)
node6 = Node(6)

node2.left = node3
node2.right = node4
node4.right = node5
node5.right = node6
node7.left = node8
node7.right = node9
node1.left = node2
node1.right = node7

root  = node1
obj = Solution()
print(obj.morrisAlgorithm_inorder(root))
print(obj.morrisAlgorithm_preorder(root))

# Output  : [3, 2, 4, 5, 6, 1, 8, 7, 9]
# Output  : [1, 2, 3, 4, 5, 6, 7, 8, 9]