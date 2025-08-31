"""Given a binary tree, return an array where elements represent the bottom view of the binary tree from left to right.

Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the later one in the level order traversal is considered. For example, in the below diagram, 7 and 34 both are the bottommost nodes at a horizontal distance of 0 from the root, here 34 will be considered."""
from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def bottomView(self, root):
        if root == None:
            return []

        ans = []
        result = {}
        queue = deque([])
        
        queue.append((root, 0))
        
        while queue:
            node , line = queue.popleft()
            
            # In Top view there was just an if condition here
            result[line] = node.data
            
            if node.left:
                queue.append((node.left, line -1))
            if node.right:
                queue.append((node.right , line+1))
            
        for value in sorted(result.items()):
            ans.append(value[1])
            
        return ans
            
obj = Solution()
l = [10,20,30,40,50,60,70]
root = Node(l[0])
root.left= Node((l[1]))                   #type:ignore          
root.right= Node((l[2]))                  #type:ignore              
root.left.left= Node((l[3]))              #type:ignore                                
root.left.right= Node((l[4]))             #type:ignore                               
root.right.left= Node((l[5]))             #type:ignore                                
root.right.right= Node((l[6]))            #type:ignore                    

print(obj.bottomView(root))
# Output : [40, 20, 60, 30, 70]