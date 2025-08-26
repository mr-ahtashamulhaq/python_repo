"""You are given a string S of size N that represents the prefix form of a valid mathematical expression. The string S contains only lowercase and uppercase alphabets as operands and the operators are +, -, *, /, %, and ^.Convert it to its infix form."""
class Solution:
    def preToInfix(self, s: str):
        result = []

        for char in s[::-1]:
            if char.isalnum():
                result.append(char)
                
            else:
                last = result.pop()
                secondlast = result.pop()
                tempstring = f"({last}{char}{secondlast})"

                result.append(tempstring)
        return result[-1]
            
obj = Solution()
s = "*-A/BC-/AKL"
print(obj.preToInfix(s))
 
# Output: 
# ((A-(B/C))*((A/K)-L))