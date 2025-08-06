"""Given a string, find the minimum number of characters to be inserted to convert it to a palindrome string
Note:
A palindromic sequence is a sequence that reads the same forward and backward."""
class Solution:
    def minInsertionsToPalindrome(self, s):
        left = 0
        right = len(s) - 1
        count = 0
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                count += 1

                if s[left + 1] == s[right]:
                    left += 1
                elif s[right - 1] == s[left]:
                    right -= 1
                else:
                    right -= 1
        
        return count


obj = Solution()
print(obj.minInsertionsToPalindrome("abcda"))
print(obj.minInsertionsToPalindrome("race")) 