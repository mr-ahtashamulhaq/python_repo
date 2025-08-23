"""The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively"""
from typing import List

"""BRUTE-FORCE SOLUTION"""

class Solution_Bruteforce:
    #main funciton in class
    def solveNQueens(self, n: int):
        board = ["." *n for _ in range(n)]
        ans=[]
        self.solve(0,board,ans,n)
        return ans

    #first helper function
    def solve(self,col,board,ans,n):
        if col == n:
            ans.append(board.copy())
            return
        
        for row in range(n):
            if self.is_safe(row,col,board,n):

                board[row] = board[row][:col] + "Q" + board[row][col+1:]

                self.solve(col+1,board,ans,n)
                
                board[row] = board[row][:col] + "." + board[row][col+1:]

    #second helper function
    def is_safe(self,row,col,board,n):
        duprow = row
        dupcol = col

        row = duprow
        col = dupcol
        while(row>=0 and col>=0):
            if board[row][col] == "Q":
                return False
            row -=1
            col -=1
        
        row = duprow
        col = dupcol
        while(col>=0):
            if board[row][col] == "Q":
                return False
            col -=1

        row = duprow
        col = dupcol
        while(row<n and col >=0):
            if board[row][col]== "Q":
                return False
            row +=1
            col -=1
        return True
    

""" ---OPTIMAL SOLUTION---  """

class Solution_optimal:
    #main function in class
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = ["." *n for _ in range(n)]
        left_row = [0] *n
        upper_diagonal = [0] * ( (2*n) -1)
        lower_diagonal = [0] * ( (2*n) -1)

        ans=[]
        self.solve(0,left_row,upper_diagonal,lower_diagonal,board,ans,n)
        return ans
    
    #Helper Function
    def solve(self,col,left_row,upper_diagonal,lower_diagonal,board,ans,n):
        if col == n:
            ans.append(board[:])
            return
        
        for row in range(n):
            if (left_row[row] == 0   
                and lower_diagonal [row + col] == 0    
                and upper_diagonal [n-1 + (col - row)]==0):

                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                left_row[row] =1   
                lower_diagonal [row + col] = 1   
                upper_diagonal[n-1 + (col - row)] =1


                self.solve(col+1,left_row,upper_diagonal,lower_diagonal,board,ans,n)

                board[row] = board[row][:col] + "." + board[row][col+1:]
                left_row[row] = 0   
                lower_diagonal [row + col] = 0    
                upper_diagonal[n-1 + (col - row)] = 0



obj = Solution_Bruteforce()
print(f"Brute-Force :   {obj.solveNQueens(4)}")


obj1 = Solution_optimal()
print(f"\nOptimal :       {obj1.solveNQueens(4)}")

# Output:
# Brute-Force :   [['..Q.', 'Q...', '...Q', '.Q..'], ['.Q..', '...Q', 'Q...', '..Q.']]

# Optimal :       [['..Q.', 'Q...', '...Q', '.Q..'], ['.Q..', '...Q', 'Q...', '..Q.']]