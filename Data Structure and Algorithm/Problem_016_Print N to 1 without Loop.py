"""Print numbers from N to 1 (space separated) without the help of loops."""

#User function Template for python3
class Solution:
    def printNos(self, n):
        if n==0:
            return
        print(n, end=" ")
        Solution.printNos(self,n-1)

obj = Solution()
obj.printNos(10)
# Output : 10 9 8 7 6 5 4 3 2 1 