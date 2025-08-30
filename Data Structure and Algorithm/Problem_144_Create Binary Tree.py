"""You are given an array nodes. It contains 7 integers, which represents the value of nodes of the binary tree in level order traversal. You are also given a root of the tree which has a value equal to nodes[0].

Your task to construct a binary tree by creating nodes for the remaining 6 nodes."""
#User function Template for python3
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def createTree(self, root, l):
        # Code here
        root.left= Node((l[1]))
        root.right= Node((l[2]))
        root.left.left= Node((l[3]))                #type: ignore
        root.left.right= Node((l[4]))               #type: ignore
        root.right.left= Node((l[5]))               #type: ignore
        root.right.right= Node((l[6]))              #type: ignore
        
        return root
tree = Solution()
root = Node(1)
tree.createTree(root, [1,2,3,4,5,6,7])
print(root.val)
print(root.left.val)            #type: ignore
print(root.right.val)           #type: ignore
print(root.left.left.val)       #type: ignore
print(root.left.right.val)      #type: ignore
print(root.right.left.val)      #type: ignore
print(root.right.right.val)     #type: ignore
# Output : 
# 1
# 2
# 3
# 4
# 5
# 6
# 7