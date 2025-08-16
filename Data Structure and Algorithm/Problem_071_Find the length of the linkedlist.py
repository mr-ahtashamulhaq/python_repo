"""Given head of a singly linked list. The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def getCount(self, head):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        return count

# Create linked list: 10 -> 20 -> 30
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)

Node1.next = Node2      #type:ignore
Node2.next = Node3      #type: ignore

# Count nodes
obj = Solution()
print(obj.getCount(Node1))  
 #Output: 3