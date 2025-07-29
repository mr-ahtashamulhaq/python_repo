"""Given two integers n and m (m != 0). The problem is to find the number closest to n and divisible by m. If there is more than one such number, then output the one having the maximum absolute value."""
class Solution:
    def closestNumber(self, n, m):
        q = n // m
        num1 = q * m
        num2 = (q + 1) * m
        diff1 = n - num1 if n >= num1 else num1 - n
        diff2 = n - num2 if n >= num2 else num2 - n

        if diff1 < diff2:
            return num1
        elif diff1 > diff2:
            return num2
        else:
            return num1 if (num1 < num2) else num2
# obj = Solution()
# print(obj.closestNumber(13 ,4))
