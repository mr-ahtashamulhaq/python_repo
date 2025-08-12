"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0."""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxlim = 2**31 -1
        minlim = -2**31
        sign  = -1 if x<0 else 1
        
        revnum = int(str(abs(x))[::-1]) * sign

        return revnum if minlim <= revnum <=maxlim else 0

obj = Solution()
print(obj.reverse(87634))

# output : 43678