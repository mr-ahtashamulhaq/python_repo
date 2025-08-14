"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place."""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row  = len(matrix)
        col = len(matrix[0])
        row_track = [0] * row
        col_track = [0] * col

        for i in range(row):
            for j in range(col):
                if matrix [i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1
        
        for i in range(row): 
            for j in range(col):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0
        return matrix

obj = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(obj.setZeroes(matrix))
# Output : [[1, 0, 1], [0, 0, 0], [1, 0, 1]]