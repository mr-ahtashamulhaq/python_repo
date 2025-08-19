"""Given a 32 bit unsigned integer num and an integer i. Perform following operations on the number - 

1. Get ith bit

2. Set ith bit

3. Clear ith bit

Note : For better understanding, we are starting bits from 1 instead 0. (1-based). You have to print space three space separated values ( as shown in output without a line break) and do not have to return anything."""
# User function Template for python3

class Solution:
    def bitManipulation(self, num, i):
        getbit = 1 if (num >> (i - 1)) & 1 == 1 else 0
        setbit = num | (1 << (i - 1))
        clearbit = num & (~(1 << (i - 1)))
        print(getbit, setbit, clearbit)


# test
s = Solution()
s.bitManipulation(5, 2)
# Output: 0 7 5