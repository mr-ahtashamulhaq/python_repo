"""Given a number N, write a program to check whether given number is Adam Number or not.
Adam number is a number when reversed, the square of the number and the square of the reversed number should be numbers which are reverse of each other."""
#User function Template for python3
class Solution:
    def checkAdamOrNot(self, N):
        # code here 
        rev_N = int(str(N)[::-1])
        sq_N = N ** 2
        sq_rev_N = rev_N ** 2
        if str(sq_N)[::-1] == str(sq_rev_N):
            return "Yes"
        else:
            return "NO"