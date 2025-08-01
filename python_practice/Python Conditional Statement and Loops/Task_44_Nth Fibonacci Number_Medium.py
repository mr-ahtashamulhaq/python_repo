"""Given a non-negative integer n, your task is to find the nth Fibonacci number."""
class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n==0:
         return 0
        elif n==1:
            return 1
        else:
            ans = Solution.nthFibonacci(self,n-1) + Solution.nthFibonacci(self,n-2)
            return ans

obj = Solution()
print(obj.nthFibonacci(8))