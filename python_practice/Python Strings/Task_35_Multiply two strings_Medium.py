"""Given two numbers as strings s1 and s2. Calculate their Product.

Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.."""
class Solution:
    def multiplyStrings(self, s1, s2):
        s1 = s1.lstrip('0') or "0"
        s2 = s2.lstrip('0') or "0"

        if s1 == "0" or s2 == "0":
            return "0"

        n1, n2 = len(s1), len(s2)
        result = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                digit1 = ord(s1[i]) - ord('0')
                digit2 = ord(s2[j]) - ord('0')
                product = digit1 * digit2

                pos1 = i + j
                pos2 = i + j + 1

                total = product + result[pos2]
                result[pos2] = total % 10
                result[pos1] += total // 10

        return ''.join(str(d) for d in result).lstrip('0')


obj = Solution()
print(obj.multiplyStrings("123", "456")) 