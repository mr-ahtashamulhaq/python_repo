"""Given a string s, of lowercase english alphabets, find the length of the longest prefix which is also a suffix.
Note: Prefix and suffix can be overlapping but they should not be equal to the entire string."""
class Solution:
    def longestPrefixSuffix(self, s):
        n = len(s)
        max_len = 0
        
        for length in range(n-1, 0, -1):
            if s[:length] == s[-length:]:
                max_len = length
                break
        
        return max_len


obj = Solution()
print(obj.longestPrefixSuffix("abcdabc"))