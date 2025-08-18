"""Geek is learning data structures and is familiar with linked lists, but he's curious about how to access the previous element in a linked list in the same way that we access the next element. His teacher explains doubly linked lists to him.

Given an integer array arr of size n. Construct the doubly linked list from arr and return the head of it."""
class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def constructDLL(self, arr):
        if not arr:
            return None

        self.head = Node(arr[0])
        self.tail = self.head
        current = self.head

        for i in range(1, len(arr)):
            new_node = Node(arr[i])
            current.next = new_node     #type: ignore
            new_node.prev = current     #type: ignore
            current = new_node
            self.tail = new_node  # update tail

        return self.head

    def traverse_forward(self):
        current = self.head
        if current is None:
            print("Doubly Linked List is Empty")
            return
        while current is not None:
            print(current.data, end="-->")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.tail
        if current is None:
            print("Doubly Linked List is Empty")
            return
        while current is not None:
            print(current.data, end="-->")
            current = current.prev
        print("None")


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    sol = Solution()
    sol.constructDLL(arr)

    print("Forward:")
    sol.traverse_forward()

    print("Backward:")
    sol.traverse_backward()

# Output:
# Forward:
# 10-->20-->30-->40-->50-->None
# Backward:
# 50-->40-->30-->20-->10-->None
