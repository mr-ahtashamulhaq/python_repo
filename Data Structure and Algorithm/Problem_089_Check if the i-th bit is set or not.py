"""Given two positive integer n and  k, check if the kth index bit of n is set or not.
 Note: A bit is called set if it is 1. """
class Solution:
    def checkKthBit(self, n, k):
        return True if (n >> k) & 1 == 1 else False


s = Solution()
print(s.checkKthBit(5, 2))
# Output : True
