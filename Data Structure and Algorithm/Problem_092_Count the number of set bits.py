"""You are given a number n. Find the total count of set bits for all numbers from 1 to n (both inclusive)."""
class Solution:
    def countSetBits(self, n):
        total = 0
        i = 0
        while (1 << i) <= n:      # check each bit position

            cycle = 1 << (i + 1)  # length of repeating cycle

            total += (n + 1) // cycle * (1 << i)   # complete cycles

            total += max(0, (n + 1) % cycle - (1 << i))
            i += 1
        return total


s = Solution()
print(s.countSetBits(7)) 
# output: 12