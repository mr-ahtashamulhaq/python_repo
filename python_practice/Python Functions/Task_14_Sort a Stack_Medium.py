"""Given a stack, the task is to sort it such that the top of the stack has the greatest element."""

class Solution:
    def Sorted(self, s):
        s.sort()
        s.reverse()
        return s

obj = Solution()
l = [3,4,1,9,6]
print(obj.Sorted(l))