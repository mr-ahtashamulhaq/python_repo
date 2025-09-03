class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def findPreSuc(self, root, key):
        predecessor = self.predecessor(root, key)
        successor = self.successor(root, key)
        return predecessor, successor

    def predecessor(self, root, key):
        current = root
        predecessor = None

        while current is not None:
            if current.data < key:
                predecessor = current
                current = current.right
            else:
                current = current.left
        return predecessor

    def successor(self, root, key):
        successor = None
        current = root

        while current is not None:
            if current.data > key:
                successor = current
                current = current.left
            else:
                current = current.right
        return successor


root = Node(20)
root.left = Node(10)                    #type:ignore
root.right = Node(30)                   #type:ignore
root.left.left = Node(5)                #type:ignore
root.left.right = Node(15)              #type:ignore
root.right.left = Node(25)              #type:ignore
root.right.right = Node(35)             #type:ignore

s = Solution()
pre, suc = s.findPreSuc(root, 20)
print("Predecessor:", pre.data if pre else None)
print("Successor:", suc.data if suc else None)

# Predecessor: 15
# Successor: 25