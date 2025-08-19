"""Given a non-negative number n . The problem is to set the rightmost unset bit in the binary representation of n"""
class Solution:
    def setBit(self, n):
        return n | (n + 1)

s = Solution()
print(s.setBit(10)) 
#Output: 11