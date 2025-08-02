"""Given a positive integer n, return the nth row of pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row."""
class Solution:
    def get_pascals_row(self,n):
        row = [1]
    
        for _ in range(n):
            new_row = [1]
        
            for i in range(1, len(row)):
                new_row.append(row[i-1] + row[i])
        
            new_row.append(1)
            row = new_row
    
        return row

		
obj = Solution()
print(obj.get_pascals_row(3))