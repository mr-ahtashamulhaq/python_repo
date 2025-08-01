"""You are given an integer n. You have  to print all numbers from 1 to n.
Note: You must use recursion only, and print all numbers from 1 to n in a single line, separated by spaces."""
class Solution:    
    def printNos(self,n):
        if n == 1:
            return 1
        else:
            return f"{Solution.printNos(self,n-1)} {n} "
obj = Solution()
print(obj.printNos(9))
        