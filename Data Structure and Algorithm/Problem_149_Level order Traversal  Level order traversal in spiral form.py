"""Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)."""
from collections import deque
from typing import List, Optional
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[Node]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([])
        queue.append(root)

        while queue:
            current_level = []
            size  = len(queue)

            for i in range(size):
                e = queue.popleft()

                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)

                current_level.append(e.val)

            result.append(current_level)


        return result
    
obj = Solution()
l = [10,20,30,40,50,60,70]
root = Node(l[0])
root.left= Node((l[1]))
root.right= Node((l[2]))
root.left.left= Node((l[3]))                
root.left.right= Node((l[4]))              
root.right.left= Node((l[5]))               
root.right.right= Node((l[6]))       

print(obj.levelOrder(root))

# Output : [[10], [20, 30], [40, 50, 60, 70]]