"""Given an integer n representing number of vertices. Find out how many undirected graphs (not necessarily connected) can be constructed out of a given n number of vertices."""
class Solution:
    def count(self, n):
        # Code here
        x = n * (n-1) //2
        return 2**x
    
obj = Solution()
print(obj.count(5))
# Output : 1024