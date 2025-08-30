"""Given the root of a binary tree, Traverse it and return the traversal of its nodes'values.'
Note: Your can choose in which order you want to traverse (PreOrder, InOrder, PostOrder)"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse_recursion(self,node, result):
        if node == None:
            return 
        result.append(node.val)

        self.traverse_recursion(node.left, result)
        self.traverse_recursion(node.right, result)
    def TreeTraversal(self, root ):
        result = []
        self.traverse_recursion(root,result)
        return result
        

# Code here
obj = Solution()
l = [150,250,350,450,550,650,750]
root = Node(l[0])
root.left= Node((l[1]))
root.right= Node((l[2]))
root.left.left= Node((l[3]))                
root.left.right= Node((l[4]))              
root.right.left= Node((l[5]))               
root.right.right= Node((l[6]))       

print(obj.TreeTraversal(root))
# Output : [150, 250, 450, 550, 350, 650, 750]