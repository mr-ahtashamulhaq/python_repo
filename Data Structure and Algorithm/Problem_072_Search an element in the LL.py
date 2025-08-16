"""Given a linked list of n nodes and a key, the task is to check if the key is present in the linked list or not."""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def searchKey(self, n, head, key):
        current = head
        while current is not None:
            if current.data == key:
                return True  
            current = current.next
        return False         

# Create linked list: 10 -> 20 -> 30
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)

Node1.next = Node2      #type: ignore
Node2.next = Node3      #type: ignore

obj = Solution()
print(obj.searchKey(3, Node1, 20))  # Output: True
print(obj.searchKey(3, Node1, 50))  # Output: False