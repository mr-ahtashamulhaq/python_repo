"""You are given a Doubly Linked List and an integer x. Remove the node at position x (positions are 1-indexed) from the list, and return the head of the updated list."""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def delete_node(self, head, x):
        if not head:
            return None
        
        current = head
        count = 1
        
        while current and count < x:
            current = current.next
            count += 1
        
        # If x is out of range
        if not current:
            return head
        
        # Deleting the head node
        if current == head:
            head = head.next
            if head:
                head.prev = None
            return head
        
        # Deleting middle or tail
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        
        return head


def print_forward(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


if __name__ == "__main__":
    # DLL: 10 <-> 20 <-> 30 <-> 40
    head = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    head.next = node2       #type:ignore
    node2.prev = head       #type:ignore
    node2.next = node3       #type:ignore
    node3.prev = node2       #type:ignore
    node3.next = node4       #type:ignore
    node4.prev = node3       #type:ignore


    sol = Solution()
    head = sol.delete_node(head, 2)   # Delete node at position 2 (20)

    print("After deleting node:")
    print_forward(head)

#Output: 10 -> 30 -> 40 -> None