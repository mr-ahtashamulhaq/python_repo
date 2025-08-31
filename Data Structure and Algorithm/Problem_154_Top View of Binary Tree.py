"""You are given a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

Note:
Return the nodes from the leftmost node to the rightmost node.
If two nodes are at the same position (horizontal distance) and are outside the shadow of the tree, consider the leftmost node only. """
from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    
    def topView(self,root):
        if root == None:
            return []
        
        ans = []
        queue = deque([])
        result = {}

        queue.append((root, 0))
        
        while queue:
            node , line= queue.popleft()

            if line not in result:
                result[line] = node.data
            
            if node.left:
                queue.append([node.left , line - 1])
            if node.right:
                queue.append([node.right , line +1])

        for values in sorted(result.items()):
            ans.append(values[1])
        
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

print(obj.topView(root))

# Output : [40, 20, 10, 30, 70]