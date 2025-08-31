from typing import Optional
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[Node], val: int):

        temp = root

        while temp is not None:
            if val == temp.val:
                return temp.val
            elif val < temp.val:
                temp = temp.left
            else:
                temp = temp.right
        return None
        
obj = Solution()

l =[4,2,7,1,3]
root = Node(l[0])
root.left= Node((l[1]))                   #type:ignore          
root.right= Node((l[2]))                  #type:ignore              
root.left.left= Node((l[3]))              #type:ignore                                
root.left.right= Node((l[4]))             #type:ignore                               

print(obj.searchBST(root , 2))

# Output : 2