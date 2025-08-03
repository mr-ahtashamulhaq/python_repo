"""Given a binary tree and the task is to find the spiral order traversal of the tree and return the list containing the elements.
Spiral order Traversal mean: Starting from level 0 for root node, for all the even levels we print the node's value from right to left and for all the odd levels we print the node's value from left to right."""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findspiral(self,root):
        if not root:
            return []
        result = []
        stack1 = [root]
        stack2 = []

        while stack1 or stack2:

            while stack1:
                node = stack1.pop()
                result.append(node.data)

                if node.right:
                    stack2.append(node.right)
                if node.left:
                    stack2.append(node.left)
            

            while stack2:
                node = stack2.pop()
                result.append(node.data)

                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
        return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)

sol = Solution()
print(sol.findspiral(root))