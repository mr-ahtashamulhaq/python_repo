"""Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom."""
from typing import Optional ,List
from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class BFS:
    """RIGHT VIEW USING BFS"""
    def rightView(self, root: Optional[Node]) -> List[int]:
        if root == None:
            return []
        
        queue  = deque([])
        result = []
        queue.append(root)

        while len(queue) != 0:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                #check if its last element on that level because then it will be rightmost
                if i == size-1:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
    
    """LEFT VIEW USING BFS"""
    def leftView(self, root: Optional[Node]) -> List[int]:
        if root == None:
            return []
        
        queue  = deque([])
        result = []
        queue.append(root)
        
        while len(queue) != 0:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                # first element on this level = leftmost
                if i == 0:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
    
class DFS:
    """RIGTH VIEW USING DFS"""
    def reverse_postorder(self, node, level, result):
        if node ==None:
            return
        if len(result)  == level:
            result.append(node.data)
        # for rigth view, go left first then left
        self.reverse_postorder(node.right, level+1, result)
        self.reverse_postorder(node.left, level+1, result)
        return result
    
    
    def rightView(self, root: Optional[Node]) -> List[int]:
        result = []
        self.reverse_postorder(root,0,result)
        return result
    
    
    """LEFT VIEW USING DFS"""
    def leftViewSolver(self, node, level, result):
        if node == None:
            return
        if len(result) == level:
            result.append(node.data)

        # for left view, go left first then right
        self.leftViewSolver(node.left, level+1, result)  
        self.leftViewSolver(node.right, level+1, result) 
        return result


    def leftView(self, root: Optional[Node]) -> List[int]: 
        result = []
        self.leftViewSolver(root, 0, result)
        return result

    

bfs_obj = BFS()
dfs_obj = DFS()

l = [10,20,30,40,50,60,70]
root = Node(l[0])
root.left= Node((l[1]))                   #type:ignore          
root.right= Node((l[2]))                  #type:ignore              
root.left.left= Node((l[3]))              #type:ignore                                
root.left.right= Node((l[4]))             #type:ignore                               
root.right.left= Node((l[5]))             #type:ignore                                
root.right.right= Node((l[6]))            #type:ignore                    

print(bfs_obj.rightView(root))
print(dfs_obj.rightView(root))
print(bfs_obj.leftView(root))
print(dfs_obj.leftView(root))

# Output
# [10, 30, 70]
# [10, 30, 70]
# [10, 20, 40]
# [10, 20, 40]