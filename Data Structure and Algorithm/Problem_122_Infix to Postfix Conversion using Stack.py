"""Given an infix expression in the form of string s. Convert this infix expression to a postfix expression.

Infix expression: The expression of the form a op b. When an operator is in between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^"""
class Solution:
    def precedence(self, ch):
        # Define operator precedence hierarchy
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":
            return 3
        return 0  # For non-operators like '(' and ')'

    def InfixtoPostfix(self, s):
        stack = []  
        result = []  


        for char in s:
            # If character is an operand, add it directly to result
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)
            
            # If character is '(', push it to the stack
            elif char == "(":
                stack.append(char)
            
            # If character is ')', pop until '(' is encountered
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()  # Discard the '('
            
            # If character is an operator
            else:
                # Pop operators until found lower hirearchy than its own
                while stack and self.precedence(stack[-1]) >= self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)  # Push current operator


        # Pop remaining operators from the stack
        while stack:
            result.append(stack.pop())

        return "".join(result)


                
obj = Solution()
s = "a+b*(c^d-e)^(f+g*h)-i"
print(obj.InfixtoPostfix(s))
# Output : abcd^e-fgh*+^*+i-