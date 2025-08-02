"""Given a stack s, delete the middle element of the stack without using any additional data structure."""

class Solution:
    def deleteMid(self, stack):
        stack.sort()
        stack.reverse()
        index = len(stack) // 2
        stack.pop(index)
        return stack
        
obj = Solution()
l = [10,20,30,40,50]
print(obj.deleteMid(l))