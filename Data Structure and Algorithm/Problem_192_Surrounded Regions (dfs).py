"""You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

    Connect: A cell is connected to adjacent cells horizontally or vertically.
    Region: To form a region connect every 'O' cell.
    Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.

To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything."""
from typing import List
class Solution:
    def dfs_algo(self, r, c, rows, cols, visited, board):
        if r<0 or c <0 or r>=rows or c >= cols:
            return
        if board[r][c] == "X":
            return
        if visited[r][c] == 1:
            return

        visited[r][c] = 1
        self.dfs_algo(r+1, c, rows, cols, visited, board)
        self.dfs_algo(r-1, c, rows, cols, visited, board)
        self.dfs_algo(r, c+1, rows, cols, visited, board)
        self.dfs_algo(r, c-1, rows, cols, visited, board)


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows  = len(board)
        cols  = len(board[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        #Upper row
        r = 0
        for c in range(cols):
            if board[r][c] == "O":
                if visited[r][c] == 0:
                    self.dfs_algo(r, c, rows, cols, visited, board)
             
        #Bottom row
        r = rows-1
        for c in range(cols):
            if board[r][c] == "O":
                if visited[r][c] == 0:
                    self.dfs_algo(r, c, rows, cols, visited, board)

        #Left column
        c = 0
        for r in range(rows):
            if board[r][c] == "O":
                if visited[r][c] == 0:
                    self.dfs_algo(r, c, rows, cols, visited, board)

        #Right Column
        c = cols-1
        for r in range(rows):
            if board[r][c] == "O":
                if visited[r][c] == 0:
                    self.dfs_algo(r, c, rows, cols, visited, board) 

        #Marking 'O' --> 'X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and visited[r][c] == 0:
                    board[r][c] = "X"

obj = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
obj.solve(board)
print(board)

# INPUT
# 
#     ['X', 'X', 'X', 'X']
#     ['X', 'O', 'O', 'X']
#     ['X', 'X', 'O', 'X']
#     ['X', 'O', 'X', 'X']
# 
# OUTPUT
# 
#     ['X', 'X', 'X', 'X']
#     ['X', 'X', 'X', 'X']
#     ['X', 'X', 'X', 'X']
#     ['X', 'O', 'X', 'X']