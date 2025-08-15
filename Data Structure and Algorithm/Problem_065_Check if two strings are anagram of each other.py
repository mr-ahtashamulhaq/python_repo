"""Given two strings s and t, return true if t is an anagram of s, and false otherwise"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #  if not have same length
        if len(s) != len(t):
            return False

        freq = {}
        #store each character number of occurance of 's'
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        #check if 't' has same number of occurences as 's'
        for char in t:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1

        return True

obj = Solution()
s= "anagram"
t = "aaamrgn"

print(obj.isAnagram(s,t))
# output : True