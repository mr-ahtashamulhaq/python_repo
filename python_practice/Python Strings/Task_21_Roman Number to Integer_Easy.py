"""Given a string s in Roman number format, your task is to convert it to an integer. Various symbols and their values are given below.

Note: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000"""
class Solution:
    def romanToInt(self, s):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman  = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        i = 0
        result = 0
        while i < len(s):
            for j, symbol in enumerate(roman):
                if s[i:i+len(symbol)] == symbol:
                    result += values[j]
                    i += len(symbol)
                    break
        return result

obj = Solution()
print(obj.romanToInt("IV"))