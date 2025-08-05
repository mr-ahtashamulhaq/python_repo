"""Given an integer n, your task is to complete the function convertToRoman which prints the corresponding roman number of n. Various symbols and their values are given below

Note:- There are a few exceptions for some numbers like 4 in roman is IV,9 in roman is IX, similarly, 40 is XL while 90 is XC. Similarly, 400 is CD while 900 is CM"""
class Solution:
    def convertRoman(self, n):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman =  ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = []

        while n > 0:
            for j, i in enumerate(values):
                if n >= i:
                    n -= i
                    result.append(roman[j])
                    break
        
        return "".join(result)  
obj = Solution()
print(obj.convertRoman(15))