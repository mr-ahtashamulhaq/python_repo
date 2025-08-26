"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""
class Solution:
    def isValid(self, s: str):
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)

            else:
                if len(stack) ==0:
                    return False
                
                popitem = stack.pop()
                if (popitem == "(" and char == ")"
                    or  popitem == "{" and char == "}"
                    or popitem == "[" and char == "]"):
                    continue

                else:
                    return False
                
        if len(stack) !=0:
            return False
        
        return True
    


obj = Solution()
print(obj.isValid("()[]{}"))
# Output : True   