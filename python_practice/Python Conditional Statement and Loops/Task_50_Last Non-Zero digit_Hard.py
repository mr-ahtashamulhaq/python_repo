"""You will be given a list A of N non-negative integers. Your task is to find the rightmost non-zero digit in the product of list elements."""
#User function Template for python3

class Solution:
    def rightmostNonZeroDigit (self, N, A):
        product = 1
        for i in A:
            product *= i
        for i in range(len(str(A))):
            if product%10 != 0:
                lastdigit = product%10
                return lastdigit
            else:
                product = product//10

N = 5
A = [1,2,3,4,5]
obj = Solution()
print(obj.rightmostNonZeroDigit(N,A))    