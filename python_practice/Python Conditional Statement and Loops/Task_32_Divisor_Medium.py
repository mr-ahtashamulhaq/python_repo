"""Given an integer n. Write a program to print all the divisors of n in a single line."""
class Solution:
    def print_divisors(self, n):
        for i in range(1,n+1):
            if n%i == 0:
                print(i,end=" ")

# obj = Solution()
# obj.print_divisors(12)