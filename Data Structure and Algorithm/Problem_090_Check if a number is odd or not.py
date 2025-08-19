"""Given a positive integer n, determine whether it is odd or even. Return true if the number is even and false if the number is odd."""
class Solution:
    def isEven(self, n):
        return True if n & 1 == 0 else False


s = Solution()
print(s.isEven(7))
# Output : False