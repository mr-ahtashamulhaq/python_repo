class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        palindrom = ""
        
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if substring == substring[::-1]:  # check palindrome
                    if len(substring) > len(palindrom):  # keep longest
                        palindrom = substring
        return palindrom


obj=Solution()
s = "babad"
print(obj.longestPalindrome(s))
# Output : bab