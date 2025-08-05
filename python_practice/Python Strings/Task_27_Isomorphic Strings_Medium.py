"""Given two strings s1 and s2 consisting of only lowercase English letters and of equal length, check if these two strings are isomorphic to each other.

If the characters in s1 can be changed to get s2, then two strings, s1 and s2 are isomorphic. A character must be completely swapped out for another character while maintaining the order of the characters."""
class Solution:
    def areIsomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        map1 = {}
        map2 = {}
        
        for i in range(len(s1)):
            c1 = s1[i]
            c2 = s2[i]
            
            if (c1 in map1 and map1[c1] != c2) or (c2 in map2 and map2[c2] != c1):
                return False
            
            map1[c1] = c2
            map2[c2] = c1
        
        return True


obj = Solution()
print(obj.areIsomorphic("egg", "add"))