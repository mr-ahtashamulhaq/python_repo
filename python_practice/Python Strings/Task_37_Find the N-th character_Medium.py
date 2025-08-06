"""Given a binary string s. Perform r iterations on string s, where in each iteration 0 becomes 01 and 1 becomes 10. 
Find the nth character (considering 0 based indexing) of the string after performing these r iterations (see examples for better understanding)."""
class Solution:
    def nthCharacter(self, s, r, n):
        for _ in range(r):
            new_string = []
            for ch in s:
                if ch == "0":
                    new_string.append("01")
                else:
                    new_string.append("10")
            s = "".join(new_string)
        return s[n]


obj = Solution()
print(obj.nthCharacter("1100", 2, 3))
