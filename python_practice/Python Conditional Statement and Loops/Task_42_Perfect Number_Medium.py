"""Given a number n, check if the number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number."""
class Solution:
    def isPerfect(self, n):
        sum = 0
        for i in range(1,n):
            if n%i == 0:
                sum += i
        return True if sum==n else False

obj = Solution()
print(obj.isPerfect(10))