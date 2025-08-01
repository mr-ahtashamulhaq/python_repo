"""Given a number n , subtract one from it using bitwise operations."""
#User function Template for python3
class Solution:
    def subtractOne(self, x):
        a = 1
        while (a&x == False):
            x = x^a
            a= a<<1
        x= x^a
        return x
    
obj = Solution()
print(obj.subtractOne(15))