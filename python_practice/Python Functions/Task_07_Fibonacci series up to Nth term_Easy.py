"""You are given an integer n, return the fibonacci series till the nth(0-based indexing) term."""
#User function Template for python3

class Solution:
    def series(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return Solution.series(self,n-1) + Solution.series(self,n-2)
        
obj = Solution()
n = 10
for i in range(n+1):
    print(obj.series(i),end=" ")