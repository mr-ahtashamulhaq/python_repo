"""Implement a Queue using an Array. Queries in the Queue are of the following type:
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the popped element. If the queue is empty then return -1)

We just have to implement the functions push and pop and the driver code will handle the output."""
class MyQueue:
    def __init__(self):
        self.queue = []

    #Function to push an element x in a queue.
    def push(self, x):
        self.queue.append(x)


    #Function to pop an element from queue and return that element.
    def pop(self): 
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)

queue = MyQueue()
queue.push(10)
queue.push(50)
queue.push(60)
queue.push(90)

print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())

# Output: 
# 10
# 50
# 60
# 90