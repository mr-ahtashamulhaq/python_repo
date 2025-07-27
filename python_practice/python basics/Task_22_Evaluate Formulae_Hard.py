"""Given four inputs that are stored in variables a, b, c, and d. You need to write an expression to evaluate the following formula. Use integer division. The expression should be a single statement."""

#    a + b
#  ----------  + d
#      c

class Solution:
    def calculate(self, a: int, b: int, c: int, d: int) -> int:
        #Code here
        return ((a+b)//c)+d