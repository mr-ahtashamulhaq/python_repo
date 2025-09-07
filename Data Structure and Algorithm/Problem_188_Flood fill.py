"""You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill."""
from copy import deepcopy
from typing import List
from collections import deque
class Solution:
    #Helper Function for DFS --> this will call recursively
    def flood_fill_DFS(self, i ,j , new_color , initial_color, visited, rows , cols):
        if i < 0 or j < 0 or i == rows or j == cols:
            return
        if visited[i][j] != initial_color:
            return
        if visited[i][j] == initial_color:
            visited[i][j] = new_color

        self.flood_fill_DFS(i+1 ,j   , new_color, initial_color, visited, rows, cols)
        self.flood_fill_DFS(i-1 ,j   , new_color, initial_color, visited, rows, cols)
        self.flood_fill_DFS(i   ,j-1 , new_color, initial_color, visited, rows, cols)
        self.flood_fill_DFS(i   ,j+1 , new_color, initial_color, visited, rows, cols)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
                
        visited = deepcopy(image)
        rows = len(visited)
        cols = len(visited[0])
        original_color = visited[sr][sc]

        self.flood_fill_DFS( sr , sc , color , original_color ,visited, rows , cols )
        return visited

    def flooed_fill_BFS(self, image , sr, sc, color):
        if image[sr][sc] == color:
            return image
        
        image_copy = deepcopy(image)
        initial_color = image_copy[sr][sc]
        rows  = len(image)
        cols  = len(image[0])

        queue = deque()
        queue.append((sr,sc))
        
        while queue:
            i, j = queue.popleft()
            image_copy[i][j] = color

            for x , y in [(-1 , 0), (1, 0) , (0 ,-1) , (0, 1)]:
                new_i = i + x 
                new_j = j + y

                if new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols:
                    continue
                if image_copy[new_i][new_j] != initial_color:
                    continue
                queue.append((new_i, new_j))

        return image_copy

            



obj = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(obj.floodFill(image, sr , sc, color))
print(obj.flooed_fill_BFS(image, sr, sc, color))

# Output
# [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
# [[2, 2, 2], [2, 2, 0], [2, 0, 1]]