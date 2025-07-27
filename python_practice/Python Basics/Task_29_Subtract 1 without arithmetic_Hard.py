"""Given a number n , subtract one from it using bitwise operations."""
#User function Template for python3
class Solution:
    def subtractOne(self, x):
        #code here
        a = 1
        while(x & a == False):
            x = x^a
            a  = a<<1

        x = x^a
        return x