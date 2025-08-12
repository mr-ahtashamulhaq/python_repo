""" Print GFG n times without the loop."""

class Solution:
    def printGfg(self, n):
        if n==0:
            return
        print("GFG",end = " ")
        Solution.printGfg(self,n-1)

obj = Solution()
obj.printGfg(5)

# Output : GFG GFG GFG GFG GFG 