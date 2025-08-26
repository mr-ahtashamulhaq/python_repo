"""You are given an infix expression in the form of a string s, consisting of:

Lowercase alphabetical operands (a to z).
Standard arithmetic operators: +, -, *, /, ^.
Optional parentheses for grouping.


Your task is to convert this infix expression into its equivalent prefix expression and return it as a string."""
class Solution:
    def precedence(self,operator):
        if operator == "^":
            return 3
        if operator == "*" or operator == "/":
            return 2
        if operator == "+" or operator == "-":
            return 1
        
        return 0
    
    #main function in class
    def infixToPrefix(self, s):
        #code here
        s = s[::-1]
        s=s.replace("(","temp").replace(")","(").replace("temp",")")

        result = []
        stack = []

        for char in s:
            if "a"<= char <= "z" or "A"<= char <= "Z" or "0"<= char <= "1" :
                result.append(char)
            elif char == "(":
                stack.append(char)

            # If character is ')', pop until '(' is encountered
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()  # Discard the '('

            # If character is an operator
            else:

                # in the infix to postfix used '>='
                # But in the infix to prefix algorithm change '>='  to '>'

                while stack and self.precedence(stack[-1]) > self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)
            
        while stack:
            result.append(stack.pop())

        #  Reverse the result to get prefix expression
        return "".join(result[::-1])
        

obj = Solution()
s = "(a-b/c)*(a/k-l)"

print(obj.infixToPrefix(s))
#  Output : *-a/bc-/akl