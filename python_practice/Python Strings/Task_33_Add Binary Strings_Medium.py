"""Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings."""
class Solution:
    def addBinary(self, s1, s2):
        num1 = int(s1, 2)
        num2 = int(s2, 2)
        
        total = num1 + num2

        result = bin(total)[2:]
        
        return result.lstrip("0") or "0"

obj = Solution()
print(obj.addBinary("00101", "00011"))