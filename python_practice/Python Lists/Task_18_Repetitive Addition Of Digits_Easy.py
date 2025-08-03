"""You are given a positive integer n, you need to add all the digits of n and create a new number. Perform this operation until the resultant number has only one digit in it. Return the final number obtained after performing the given operation."""
class Solution:
    def singleDigit(self, n):
        while(n>9):
            sum = 0
            num = str(n)
            for i in num:
                sum += int(i)
            n = sum
        return n
    	

obj = Solution()
num = 5674
print(obj.singleDigit(num))