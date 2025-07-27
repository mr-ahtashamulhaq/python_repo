"""Given three integers a, d and n. Where a is the first term, d is the common difference of an A.P.  Calculate the nth term of A.P(Arithmetic Progression) 
The nth term is given by an = a + (n-1)d"""

class Solution:
    def nthTerm(self, a, d, n):
        #code here 
        n_term = a + ((n-1)*d)
        return n_term