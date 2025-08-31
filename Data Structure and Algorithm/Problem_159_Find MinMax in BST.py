"""Given the root of a Binary Search Tree. The task is to find the minimum valued element and MAximum valued element in this given BST."""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def minValue(self, root):
        ##Your code here
        temp = root
        
        while temp is not None and temp.left is not None:
            temp = temp.left
        return temp.data
    
    def maxValue(self, root):
        temp = root

        while temp is not None and temp.right is not None:
            temp = temp.right
        return temp.data

obj = Solution()

l =[4,2,7,1,3]
root = Node(l[0])
root.left= Node((l[1]))                   #type:ignore          
root.right= Node((l[2]))                  #type:ignore              
root.left.left= Node((l[3]))              #type:ignore                                
root.left.right= Node((l[4]))             #type: ignore

print(obj.minValue(root))
print(obj.maxValue(root))
# Output :    1     7