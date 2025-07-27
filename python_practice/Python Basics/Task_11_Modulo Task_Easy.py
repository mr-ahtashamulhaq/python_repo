""" Given an integer N. FInd an integer K for which N%K is the largest ( 1 <= K < N). 
 You don't need to read input or print anything. Your task is to complete the function modTask() which takes a Integer N as input and returns an integer K(1 <= K < N) for which N%K is largest."""
#User function Template for python3

class Solution:
    def modTask(self, N):
        temp = -1
        for K in range(1,N):

            if (N%K > temp):
                temp =  N%K
                final_K = K

        return final_K