"""Given a positive integer n, determine whether it is odd or even. Return true if the number is even and false if the number is odd."""
class Solution:
    def isEven (self, n):
        # code here 
        if (n % 2 == 0):
            return "Even"

        else:
            return "Odd"
        
# obj = Solution()
# print(obj.isEven(4))