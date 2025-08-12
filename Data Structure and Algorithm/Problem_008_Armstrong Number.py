"""You are given a 3-digit number n, Find whether it is an Armstrong number or not.

An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. """
#User function Template for python3
class Solution:
    def armstrongNumber (self, n):
        # code here 
        num = n
        result = 0
        for i in range(3):
            ld = num%10
            result += ld**3
            num = num//10
        return n == result
obj = Solution()
print(obj.armstrongNumber(153))

# Output : True