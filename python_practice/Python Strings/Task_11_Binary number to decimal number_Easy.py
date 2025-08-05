"""Given a string b representing a Binary Number, The problem is to find its decimal equivalent."""
class Solution:
    def binaryToDecimal(self, b):
        decimal = 0
        n = len(b)
        for i in b:
            decimal += int(i) * (2**(n-1))
            n -= 1
        return decimal

    
obj = Solution()
print(obj.binaryToDecimal("111"))