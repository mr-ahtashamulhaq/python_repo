"""Given a string str of opening and closing brackets '(' and ')' only. The task is to find an equal point. An equal point is an index (0-based) such that the number of closing brackets on the right from that point must be equal to the number of opening brackets before that point."""
class Solution:
    def findEqualPoint(self, s):
        n = len(s)
        
        close_count = s.count(')')
        open_count = 0
        
        for i in range(n):
            if s[i] == '(':
                open_count += 1
            else:
                close_count -= 1 
            
            if open_count == close_count:
                return i + 1 
        
        return -1

obj = Solution()
print(obj.findEqualPoint("(())))("))