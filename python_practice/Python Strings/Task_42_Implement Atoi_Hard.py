"""Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

Cases for atoi() conversion:

Skip any leading whitespaces.
Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231."""
class Solution:
    def myAtoi(self, s):
        string = s.strip()
        if len(string) == 0:
            return 0
        
        sign = 1
        start_index = 0
        if string[0] == "-":
            sign = -1
            start_index = 1
        elif string[0] == "+":
            start_index = 1
        
        num = 0
        for i in range(start_index, len(string)):
            if string[i] >= "0" and string[i] <= "9": 
                num = num * 10 + (ord(string[i]) - ord("0"))
            else:
                break
        
        num *= sign
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num


obj = Solution()
print(obj.myAtoi("-123"))  
print(obj.myAtoi("   +42abc"))