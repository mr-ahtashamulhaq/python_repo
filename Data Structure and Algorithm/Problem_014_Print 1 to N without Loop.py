"""You are given an integer n. You have  to print all numbers from 1 to n.
Note: You must use recursion only, and print all numbers from 1 to n in a single line, separated by spaces."""

class Solution:    
    def printNos(self,n):
        #Code here
        if n==0:
            return
        Solution.printNos(self,n-1)
        print(n, end=" ")

obj = Solution()
obj.printNos(10)

# Output : 1 2 3 4 5 6 7 8 9 10 