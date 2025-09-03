"""You are given a BST(Binary Search Tree) with n number of nodes and value x. your task is to find the greatest value node of the BST which is smaller than or equal to x.
Note: when x is smaller than the smallest node of BST then returns -1"""
#User function Template for python3
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Solution:
    def floor(self, root, x):
        # Code here
        floor = -1
        
        while root is not None:
            
            if x == root.data:
                return root.data
                
            elif x < root.data:
                root = root.left
            else :
                floor= root.data
                root = root.right
        return floor
    
obj = Solution()
l =[4,2,7,1,3]
root = Node(l[0])
root.left= Node((l[1]))                   #type:ignore          
root.right= Node((l[2]))                  #type:ignore              
root.left.left= Node((l[3]))              #type:ignore                                
root.left.right= Node((l[4]))             #type:ignore
print(obj.floor(root, 5))

# Output : 4