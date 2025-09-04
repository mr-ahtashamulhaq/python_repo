"""Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTree_solver(self,node ,p , q):
        if node is None:
            return None  
        if node==p or node == q:
            return node

        left  = self.binaryTree_solver(node.left , p , q)
        right  = self.binaryTree_solver(node.right , p , q)

        if left == None:
            return right
        elif right == None:
            return left
        return node



    def binarySearchTree(self, node , p, q):
        current  = node

        while True:
            if current.val < p.val and current.val < q.val:
                current = current.right
            elif current.val > p.val and current.val > q.val:
                current = current.left
            elif current == p :
                return p
            elif current == q:
                return q
            else:
                return current

    def lowestCommonAncestor_BT(self, root, p ,q):
        return self.binaryTree_solver(root, p ,q)
    

obj = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node4.left = node2              #type: ignore
node4.right = node6             #type: ignore
node2.left = node1              #type: ignore
node2.right = node3             #type: ignore
node6.left = node5              #type: ignore
node6.right = node7             #type: ignore

root = node4
print(obj.lowestCommonAncestor_BT(root, node2 , node6).val) #type: ignore
print(obj.binarySearchTree(root, node2 , node6).val)    #type: ignore
# Output : 4