"""Given a doubly linked list. Your task is to reverse the doubly linked list and return its head."""
class DLLNode:
    def __init__(self, val):
         self.data = val
         self.next = None
         self.prev = None

class Solution:
    def reverseDLL(self, head):
        if head is None or head.next is None:
            return head

        current = head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node

        return prev
    



def print_forward(head):
    curr = head
    while curr:
        print(curr.data, end=" <-> ")
        curr = curr.next
    print("None")


# DLL: 1 <-> 2 <-> 3 <-> 4
head = DLLNode(1)
node2 = DLLNode(2)
node3 = DLLNode(3)
node4 = DLLNode(4)

head.next = node2       #type: ignore
node2.prev = head       #type: ignore
node2.next = node3       #type: ignore
node3.prev = node2       #type: ignore
node3.next = node4       #type: ignore
node4.prev = node3       #type: ignore

print("Original:",end = "   ")
print_forward(head)

sol = Solution()
head = sol.reverseDLL(head)

print("Reversed:", end="    ")
print_forward(head)

# Original:   1 <-> 2 <-> 3 <-> 4 <-> None
# Reversed:    4 <-> 3 <-> 2 <-> 1 <-> None