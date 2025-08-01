"""You are given a 3-digit number n, Find whether it is an Armstrong number or not.
An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. """
#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        value = 0
        originalnum = n
        for i in range(2):
            value += (n%10)**3
            n = n//10
        value += (n**3)
        return True if value==originalnum else False

obj = Solution()
print(obj.armstrongNumber(372))