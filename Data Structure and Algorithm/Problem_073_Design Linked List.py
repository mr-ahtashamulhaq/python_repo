"""Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.

void addAtTail(int val) Append a node of value val as the last element of the linked list.

void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.

void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid."""
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0 

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next   #type: ignore
        return curr.val   #type: ignore

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head   #type: ignore
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node   #type: ignore
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next   #type: ignore
        new_node.next = curr.next   #type: ignore
        curr.next = new_node   #type: ignore
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next   #type: ignore
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next   #type: ignore
            curr.next = curr.next.next   #type: ignore
        self.size -= 1

# main
obj = MyLinkedList()
obj.addAtHead(1)          
obj.addAtTail(3)          
obj.addAtIndex(1, 2)       
print(obj.get(1))          # Output: 2
obj.deleteAtIndex(1)  
print(obj.get(1))          # Output: 3