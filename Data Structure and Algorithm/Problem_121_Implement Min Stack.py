"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function."""
class MinStack:

    def __init__(self):
        self.stack  = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val,val])
        else:
            minimum = min(self.stack[-1][1], val)
            self.stack.append([val,minimum])
            

        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

        

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())  
print(obj.getMin())  

# Output : 
# -3
# 0
# -2
