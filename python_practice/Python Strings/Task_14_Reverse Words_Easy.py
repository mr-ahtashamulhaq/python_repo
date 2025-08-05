"""Given a string s, reverse the string without reversing its individual words. Words are separated by dots(.)."""
class Solution:
    def reverseWords(self, s):
        str = (s.strip(".")).split(".")
        return ".".join(str[::-1])
                      
obj = Solution()
print(obj.reverseWords("...i.love.this.prgram..."))  