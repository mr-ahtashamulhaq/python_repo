"""You are given a string s. Your task is to determine if the string is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards."""
class Solution:
    def isPalindrome(self, s):
        s1 = s[::-1]
        if s == s1:
            return True
        else:
            return False
        
obj = Solution()
print(obj.isPalindrome("racecar"))