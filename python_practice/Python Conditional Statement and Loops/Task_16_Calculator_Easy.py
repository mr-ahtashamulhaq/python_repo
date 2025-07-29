"""Given two numbers a and b. You need to perform basic mathematical operations on them. You will be provided an integer named as operator.

If the operator equals to 1 add a and b, then print the result.
If the operator equals to 2 subtract b from a, then print the result.
If the operator equals to 3 multiply a and b, then print the result.
If the operator equals to any other number, print "Invalid Input"(without quotes)."""
class Solution:
    def calculate(self, a: int, b: int, operator: int) -> None:
        #code here
        if operator == 1:
            print(a + b)
        elif operator == 2:
            print(a - b)
        elif operator == 3:
            print(a * b)
        else:
            print("Invalid Input")

# obj = Solution()
# obj.calculate(2,3,3)

