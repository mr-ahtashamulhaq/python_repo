"""Implement a Queue using Linked List. 
A Query Q is of 2 Types
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the poped element"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = None  
        self.rear = None  

    # add at rear
    def push(self, item):
        new_node = Node(item)

        # Empty queue: front and rear both point to new node
        if self.rear is None:
            self.front = self.rear = new_node
            return
        
        # Attach new node to rear and update rear pointer
        self.rear.next = new_node           #type:ignore
        self.rear = new_node

    # remove from front
    def pop(self):
        if self.front is None:
            return -1  # Queue empty
        popped = self.front.data
        self.front = self.front.next
        
        # If queue becomes empty, rear also must be None
        if self.front is None:
            self.rear = None
        return popped
    
q = MyQueue()
q.push(10)
q.push(20)
q.push(30)

print(q.pop())
print(q.pop())  
print(q.pop()) 
print(q.pop())  

# Output: 
# 10
# 20
# 30
# -1