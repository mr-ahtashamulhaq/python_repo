""" Given a positive integer, n. Find the factorial of n."""

#User function Template for python3
class Solution:
    def factorial (self, n):
        # code here
        if n<=1:
            return 1
        else:
            return n * Solution.factorial(self,n-1)
    
obj = Solution()
print(obj.factorial(5))
# Output : 120
