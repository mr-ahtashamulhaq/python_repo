"""You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its infix form."""
class Solution:
    def postToInfix(self, postfix : str):
        # Code here
        result = []

        for char in postfix:
            if char.isalnum() == True:
                result.append(char)
            
            else:
                if result:
                    last = result.pop()
                    secondlast = result.pop()
                    templist = f"({secondlast}{char}{last})"
                    result.append(templist)

        return result[-1]
 
obj = Solution()
s = "ab*c+"
print(obj.postToInfix(s))

# Output: ((a*b)+c)