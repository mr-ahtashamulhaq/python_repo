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

            #loop will used just for making level by level. other remove it and directly append in result
            for i in range(size):
                e = queue.popleft()
                current_level.append(e.val)

                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)


            result.append(current_level)
        return result


        # To print without level by level comment above while loop and run this
        """
        while queue:
            e = queue.popleft()
            result.append(e.val)

            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)

        return result
        """
    
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