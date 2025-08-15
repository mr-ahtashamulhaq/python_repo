"""Given an m x n matrix, return all elements of the matrix in spiral order."""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        row = len(matrix)
        col = len(matrix[0])

        result = []
        left = 0
        top = 0
        bottom = row -1
        right = col -1

        while top <= bottom and left <= right:
            # from left to  right
            for i in range (left,right+1):
                result.append(matrix[top][i])
            top +=1

            # from top to bottom
            for i in range (top,bottom+1):
                result.append(matrix[i][right])
            right -=1

            # from right to left
            if top<= bottom: #if matrix only has only 1 row (which has been visited already)
                for i in range (right, left-1 , -1):
                    result.append(matrix[bottom][i])
                bottom -=1
            
            # from bottom to top
            if left<=right: # #if matrix only has only 1 col (which has been visited already)
                for i in range (bottom, top-1 , -1):
                    result.append(matrix[i][left])
                left +=1
        return result
    
obj = Solution()
matrix = [[1, 2, 3, 4, 5, 6],
          [20,21,22,23,24,7],
          [19,32,33,34,25,8],
          [18,31,36,35,26,9], 
          [17,30,29,28,27,10], 
          [16,15,14,13,12,11]]

print(obj.spiralOrder(matrix))

# Output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]