"""Given two strings denoting non-negative numbers s1 and s2. Calculate the sum of s1 and s2."""
class Solution:
    def addStrings(self, s1, s2):
        num1 = int(s1)
        num2 = int(s2)
        total = num1 + num2

        return str(total)

obj = Solution()
print(obj.addStrings("123", "456"))