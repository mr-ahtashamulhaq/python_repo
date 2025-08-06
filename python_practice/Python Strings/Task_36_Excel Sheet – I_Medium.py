"""Given a positive integer N, return its corresponding column title as it would appear in an Excel sheet.
For N =1 we have column A, for 27 we have AA and so on.

Note: The alphabets are all in uppercase."""
class Solution:
    def excelColumn(self, N):
        result = ""
        
        while N > 0:
            N -= 1
            result = chr((N % 26) + ord('A')) + result
            N //= 26
        return result


obj = Solution()
print(obj.excelColumn(51))