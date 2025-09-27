"""A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

    't' that evaluates to true.
    'f' that evaluates to false.
    '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
    '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
    '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.

Given a string expression that represents a boolean expression, return the evaluation of that expression.
"""


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        s = expression
        i = 0

        def helper():
            nonlocal i
            c = s[i]
            i += 1

            if c == "t":
                return True
            if c == "f":
                return False

            # Handle '!' operator
            if c == "!":
                i += 1  # Skip '('
                result = not helper()
                i += 1  # Skip ')'
                return result

            # Handle '&' and '|' operators
            children = []
            i += 1  # Skip '('

            while s[i] != ")":
                if s[i] == ",":
                    i += 1
                else:
                    children.append(helper())

            i += 1  # Skip ')'

            if c == "&":
                return all(children)
            else:  # c == '|'
                return any(children)

        return helper()


obj = Solution()
expression = "|(&(t,f,t),!(t))"
print(obj.parseBoolExpr(expression))

# Output : False