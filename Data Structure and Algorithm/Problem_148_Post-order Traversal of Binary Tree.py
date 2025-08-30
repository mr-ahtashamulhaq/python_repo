"""Given the root of a binary tree, return the postorder traversal of its nodes' values."""
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def post_order(self, node, result):
        if node == None:
            return 
        self.post_order(node.left, result)
        self.post_order(node.right, result)
        result.append(node.val)
    def postorderTraversal(self, root):
        
        result = []
        self.post_order(root, result)
        return result
    
obj = Solution()
obj = Solution()
l = [10,20,30,40,50,60,70]
root = Node(l[0])
root.left= Node((l[1]))
root.right= Node((l[2]))
root.left.left= Node((l[3]))                
root.left.right= Node((l[4]))              
root.right.left= Node((l[5]))               
root.right.right= Node((l[6]))       

print(obj.postorderTraversal(root))
# Output : [40, 50, 20, 60, 70, 30, 10]