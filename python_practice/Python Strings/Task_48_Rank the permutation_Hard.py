"""Given a string, find the rank of the string amongst its permutations sorted lexicographically. """
from itertools import permutations
class Solution:
    def findRank(self, s):
        
        perms = sorted(set([''.join(p) for p in permutations(s)]))
        
        return perms.index(s) + 1


obj = Solution()
print(obj.findRank("abc"))