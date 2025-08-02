"""Given a number n, find the value of n raised to the power of its own reverse."""
class Solution:
    def reverseexponentiation(self, n):
        rev = int((str(n)[::-1]))
        val = n**rev
        return val

obj = Solution()
print(obj.reverseexponentiation(2))