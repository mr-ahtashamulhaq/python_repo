"""Given an integer n find the sum of the first n natural number."""
class Solution:
    def sumOfNumbers(self, n):
        # code here
        sum=0
        for i in range(1,n+1):
            sum+=i
        return sum
    
# obj = Solution()
# print(obj.sumOfNumbers(10))