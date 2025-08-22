"""Given an integer N , Print all binary strings of size N which do not contain consecutive 1s.

A binary string is that string which contains only 0 and 1."""
#User function Template for python3

class Solution:
    def solve(self,ind,flag ,numbers,result):
        
        if ind >= len(numbers):
            string = "".join(numbers)
            result.append(string)
            return
        
        numbers[ind] = "0"
        self.solve(ind+1,True,numbers,result)
        
        if flag == True:
            numbers[ind] = "1"
            self.solve(ind+1, False,numbers,result)
            numbers[ind] = "0"
        
            
    
    def generateBinaryStrings(self, n):
        # Code here
        numbers = ["0"]*n
        result = []
        self.solve(0,True,numbers,result)
        return result
        
        
obj = Solution()
print(obj.generateBinaryStrings(3))
# Output : ['000', '001', '010', '100', '101']