"""Given the root of a binary tree, return the preorder traversal of its nodes' values."""
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pre_order(self,node, result):
        if node == None:
            return 
        result.append(node.val)

        self.pre_order(node.left, result)
        self.pre_order(node.right, result)
    def preorderTraversal(self, root ):
        result = []
        self.pre_order(root,result)
        return result
        

# Code here
obj = Solution()
l = [10,20,30,40,50,60,70]
root = Node(l[0])
root.left= Node((l[1]))
root.right= Node((l[2]))
root.left.left= Node((l[3]))                
root.left.right= Node((l[4]))              
root.right.left= Node((l[5]))               
root.right.right= Node((l[6]))       

print(obj.preorderTraversal(root))
# Output : [10, 20, 40, 50, 30, 60, 70]