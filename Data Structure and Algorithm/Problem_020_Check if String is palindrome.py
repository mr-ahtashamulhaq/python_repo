"""You are given a string s. Your task is to determine if the string is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards."""
class Solution:
    def isPalindrome(self, s,l,r):
        # code here
        if l>=r:
            return True
        if s[l] != s[r]:
            return False
        return self.isPalindrome(s,l+1,r-1)
    
obj = Solution()
s = "racecar"
l=0
r=len(s)-1
print(obj.isPalindrome(s,l,r))

# output : True