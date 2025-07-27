"""Given a decimal number n, return its binary equivalent."""
class Solution:
    def decToBinary(self, n):
        # code here
        temp = []
        while n>1:
            remainder = n % 2
            n = n//2
            temp.append(remainder)

        temp.append(n)
        temp.reverse()
        result = ((((str(temp)).replace("[","")).replace("]","")).replace(",","")).replace(" ","")



        return result