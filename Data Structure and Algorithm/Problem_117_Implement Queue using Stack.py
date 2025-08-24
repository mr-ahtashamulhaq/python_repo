"""Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise."""
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        
    def pop(self) -> int:
        if len(self.stack1) == 0:
            return -1
        return self.stack1.pop()
        

    def peek(self) -> int:
        if len(self.stack1)==0:
            return -1
        return self.stack1[-1]

        

    def empty(self) -> bool:
        return True if len(self.stack1) == 0 else False
    
queue = MyQueue()
queue.push(30)
queue.push(50)
queue.push(70)
queue.push(100)

print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())

# Output :
# 30
# 50
# 70
# 100