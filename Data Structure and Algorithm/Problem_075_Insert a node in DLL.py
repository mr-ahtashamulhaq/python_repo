"""Given the head of a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at the position just after pth node in the doubly linked list and return the head of the updated list.

Note: The position is 0-based indexed."""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node     #type:ignore
            new_node.prev = self.tail     #type:ignore
            self.tail = new_node

    def traverse_forward(self):
        current = self.head
        if not current:
            print("Doubly Linked List is Empty")
            return
        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.tail
        if not current:
            print("Doubly Linked List is Empty")
            return
        while current:
            print(current.data, end="-->")
            current = current.prev
        print("None")

    def addNode(self, p, x):
        new_node = Node(x)
        current = self.head
        count = 0

        while current is not None and count < p:
            current = current.next
            count += 1

        if current is None:  
            return self.head

        new_node.next = current.next
        new_node.prev = current     #type:ignore

        if current.next:
            current.next.prev = new_node
        else:
            self.tail = new_node

        current.next = new_node     #type:ignore
        return self.head


if __name__ == "__main__":
    arr = [10, 20, 30, 40]
    dll = DoublyLinkedList()
    for val in arr:
        dll.append(val)

    print("Before insert:",end="    ")
    dll.traverse_forward()

    dll.addNode(2, 25)

    print("After insert:",end="     ")
    dll.traverse_forward()

# Before insert:    10-->20-->30-->40-->None
# After insert:     10-->20-->30-->25-->40-->None