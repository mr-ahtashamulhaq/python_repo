"""You are given a root binary search tree and an integer x . Your task is to find the Ceil of x in the tree.
Note: Ceil(x) is a number that is either equal to x or is immediately greater than x.
If Ceil could not be found, return -1"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 

        
class Solution:
    def findCeil(self,root, x):
        ceil = -1
        # code here
        while root is not None:
            
            if x==root.data:
                ceil = root.data
                return ceil
            elif x > root.data:
                root = root.right
            else:
                ceil = root.data
                root = root.left
        return ceil
obj = Solution()
l =[4,2,7,1,3]
root = Node(l[0])
root.left= Node((l[1]))                   #type:ignore          
root.right= Node((l[2]))                  #type:ignore              
root.left.left= Node((l[3]))              #type:ignore                                
root.left.right= Node((l[4]))             #type:ignore
print(obj.findCeil(root, 7)) 

# Output : 7