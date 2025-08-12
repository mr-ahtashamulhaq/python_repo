""" Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term."""

#User function Template for python3
class Solution:
    def sumOfSeries(self,n):
        #code here
        if n==1:
            return 1
        else:
            return n**3 + Solution.sumOfSeries(self,n-1)
        
obj =  Solution()
print(obj.sumOfSeries(5))

# Output : 225