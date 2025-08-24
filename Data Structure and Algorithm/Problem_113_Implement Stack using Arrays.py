"""Write a program to implement a stack using an array oper[]. You need  to complete the push(int x) and pop() methods inside a class MyStack to simulate the standard stack operations:

push(x): Pushes the integer x onto the stack.

pop(): Removes and returns the topmost element of the stack. If the stack is empty, return -1.

You will be given a list of space-separated queries consisting of two types:
Type 1 : 1 x — Push x into the stack.
Type 2 : 2  — Pop the top element from the stack and print it. If the stack is empty, print -1.

Note: It is guaranteed that for Type 1, there will always be a value x."""
class MyStack:
    def __init__(self):
        self.arr=[]
    
    def push(self,data):
        #add code here
        self.arr.append(data)
        
    
    def pop(self):
        #add code here
        if len(self.arr)==0:
            return -1
        x = self.arr.pop()
        return x
        
        
stack = MyStack()
stack.push(10)
stack.push(500)
stack.push(300)
stack.push(750)
stack.push(900)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())


# Output:  
# 900
# 750
# 300
# 500
# 10