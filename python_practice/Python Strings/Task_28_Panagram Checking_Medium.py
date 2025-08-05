"""Given a string s, check if it is a "Panagram" or not. Return true if the string is a Panagram, else return false.
A "Panagram" is a sentence containing every letter in the English Alphabet either in lowercase or Uppercase."""
class Solution:
    def checkPangram(self,s):
        string = s.lower()
        for i in range(97,123):
            if chr(i) not in string:
                return False
        return True

obj = Solution()
s = "Bawds jog, flick quartz, vex nymph"
print(obj.checkPangram(s))