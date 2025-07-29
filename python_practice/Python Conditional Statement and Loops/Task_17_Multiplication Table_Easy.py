"""Create the multiplication table from 1 to 10 for a given number n"""
#User function Template for python3

class Solution:
    def getTable(self,n):
        # code here
        for i in range(1,11):
            print(n*i , end=" ")

# obj = Solution()
# obj.getTable(9)