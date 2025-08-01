"""Given a number n, find the Juggler Sequence for this number as the first term of the sequence until it becomes 1."""
class Solution:
    def jugglerSequence(self, n):
        ans_list = [str(n)]
        while(n != 1):

            if n%2 != 0:
                n = int(n**(3/2))
                ans_list.append(str(n))
            else:
                n = int(n**(1/2))
                ans_list.append(str(n))
                
        return " ".join(ans_list)

            
obj = Solution()
print(obj.jugglerSequence(9))
            