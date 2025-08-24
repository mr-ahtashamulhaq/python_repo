"""Let's give it a try! You have a linked list and must implement the functionalities push and pop of stack using this given linked list. Your task is to use the class as shown in the comments in the code editor and complete the functions push() and pop() to implement a stack. 
The push() method takes one argument, an integer 'x' to be pushed into the stack and pop() which returns an integer present at the top and popped out from the stack. If the stack is empty then return -1 from the pop() method."""
class Node:
    # Constructor to initialize a new node
    def __init__(self, data):
        self.data = data
        self.next = None    # next is the link to the next node

class MyStack:
    def __init__(self):
        # Stack top pointer (None means stack is empty)
        self.top = None

    # insert data at the top of the stack
    def push(self, data):
        new_node = Node(data)      
        new_node.next = self.top   # next of new node points to old top         #type:ignore
        self.top = new_node        # move top to new node

    # remove and return data from top of stack
    def pop(self):
        if self.top is None:
            return -1              # stack is empty
        popped = self.top.data    
        self.top = self.top.next   # move top to next node
        return popped
s = MyStack()
s.push(10)
s.push(20)
s.push(30)

print(s.pop()) 
print(s.pop())  
print(s.pop())  
print(s.pop())  
# Output :
# 30
# 20
# 10
# -1