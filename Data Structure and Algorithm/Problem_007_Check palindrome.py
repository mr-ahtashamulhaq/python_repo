"""Given an integer x, return true if x is a palindrome, and false otherwise."""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        result = 0
        while(num>0):
            ld = num%10
            num = num//10
            result = (result*10) + ld
        return True if result == x else False

obj = Solution()
print(obj.isPalindrome(8745))

# output : False