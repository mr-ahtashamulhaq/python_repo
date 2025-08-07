"""Given a string s consisting of lowercase English Letters. return the first non-repeating character in s. If there is no non-repeating character, return '$'."""
class Solution:
    def nonRepeatingChar(self, s):
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return s[i]
        return "$"

obj = Solution()
print(obj.nonRepeatingChar("abbccc"))