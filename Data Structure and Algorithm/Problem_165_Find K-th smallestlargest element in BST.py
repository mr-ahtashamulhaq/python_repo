# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solver (self, root, result):
        if root == None:
            return
        self.solver(root.left,result)
        result.append(root.val)
        self.solver(root.right,result)

    def kthSmallest(self, root, k):
        result = []
        self.solver(root,  result)
        print(result)
        return result[k-1]
    



    def largest_solver(self, root, result):
        if root is None:
            return
        self.largest_solver(root.left, result)
        result.append(root.val)
        self.largest_solver(root.right, result)

    def kthLargest(self, root, k):
        result = []
        self.largest_solver(root, result)
        n = len(result)
        return result[n - k]


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node4.left = node2
node4.right = node6
node2.left = node1
node2.right = node3
node6.left = node5
node6.right = node7

root = node4
obj = Solution()
print(obj.kthSmallest(root, 3))
print(obj.kthLargest(root,2))
# Output:
# [1, 2, 3, 4, 5, 6, 7]
# 3
# 6
