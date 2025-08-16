"""You are given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the head of modified Linked List."""
class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        

class Solution:
    def insertAtEnd(self, head, x):
        #code here
        new_node = Node(x)
        if head is None:
            return new_node
        
        current = head
        while current.next is not None:
            current = current.next

        current.next = new_node

        return head

        
head = Node(1)
head.next = Node(2)     #type: ignore
head.next.next = Node(3)        #type: ignore

obj = Solution()
head = obj.insertAtEnd(head, 99)

# Traverse to check
curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next

# output : 1 -> 2 -> 3 -> 99 -> 