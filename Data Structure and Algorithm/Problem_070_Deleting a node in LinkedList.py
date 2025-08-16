"""There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order."""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        # Copy the next node's value into this node
        node.val = node.next.val
        # Skip the next node
        node.next = node.next.next

# Create Linked List: 5 -> 8 -> 5
head = ListNode(5)
head.next = ListNode(8) #type: ignore
head.next.next = ListNode(5) #type: ignore

obj = Solution()
obj.deleteNode(head.next)  # deleting node with value 8

# Traverse and print the linked list
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next

#  Output: 5 -> 5 -> 