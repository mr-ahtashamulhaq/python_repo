"""Given an n-digit large number n in form of string, check whether it is divisible by 7 or not. Return 1 if divisible by 7, otherwise 0."""
#User function Template for python3
class Solution:
    def isdivisible7(self, num):
        n = int(num)
        if n%7 == 0:
            return "1"
        else:
            return "0"
        
obj = Solution()
print(obj.isdivisible7("49"))