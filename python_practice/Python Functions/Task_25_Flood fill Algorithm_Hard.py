"""You are given a 2D grid image[][] of size n*m, where each image[i][j] represents the color of a pixel in the image. Also provided a coordinate(sr, sc) representing the starting pixel (row and column) and a new color value newColor.

Your task is to perform a flood fill starting from the pixel (sr, sc), changing its color to newColor and the color of all the connected pixels that have the same original color. Two pixels are considered connected if they are adjacent horizontally or vertically (not diagonally) and have the same original color."""
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        rows = len(image)
        cols = len(image[0])
        originalColor = image[sr][sc]

        if originalColor == newColor:
            return image

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != originalColor:
                return

            image[r][c] = newColor

            dfs(r+1, c)  
            dfs(r-1, c)           
            dfs(r, c+1)
            dfs(r, c-1)  

        dfs(sr, sc)
        return image
    
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr = 1
sc = 1
newColor = 2

sol = Solution()
result = sol.floodFill(image, sr, sc, newColor)

for row in result:
    print(row)

