"""For an integer n, find the number of trailing zeroes in n!."""
class Solution:
    def trailingZeroes(self, n):
        fact=1
        for i in range(1,n+1):
            fact*=i

        st = str(fact)
        zeros = 0

        for i in st[::-1]:
            if i == "0":
                zeros += 1
                
        return zeros

obj = Solution()
obj.trailingZeroes(6)