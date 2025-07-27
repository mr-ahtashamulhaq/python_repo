"""Given two integers a and b, You have to compute their LCM and GCD and return an array containing their LCM and GCD."""
class Solution:
    def lcmAndGcd(self, a : int, b : int) -> list[int]:
        # code here
        # GCD CALCULATOR
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                gcd = i


        # LCM CALCULATOR
        if a == 1 and b == 1:
            return [1, 1]
        lcm = 1
        i = 2
        while a > 1 or b > 1:
            if a % i == 0 and b % i == 0:
                a //= i
                b //= i
                lcm *= i
            elif a % i == 0:
                a //= i
                lcm *= i
            elif b % i == 0:
                b //= i
                lcm *= i
            else:
                i += 1
        list = [lcm,gcd]
        return list
        





obj = Solution()
print(obj.lcmAndGcd(14 ,8))