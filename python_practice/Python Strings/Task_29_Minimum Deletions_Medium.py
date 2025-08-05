"""Given a string s, write a program to delete the minimum number of characters from the string so that the resultant string is a palindrome, while maintaining the order of characters."""
class Solution:
    def minDeletionsToPalindrome(self, s):
        s = list(s)
        count = 0
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if s[i+1] == s[j]:
                    i += 1
                elif s[i] == s[j-1]:
                    j -= 1
                else:
                    i += 1
                count += 1
        return count

obj = Solution()
print(obj.minDeletionsToPalindrome("aebcbda"))