"""You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

    Robot #1 is located at the top-left corner (0, 0), and
    Robot #2 is located at the top-right corner (0, cols - 1).

Return the maximum number of cherries collection using both robots by following the rules below:

    From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
    When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
    When both robots stay in the same cell, only one takes the cherries.
    Both robots cannot move outside of the grid at any moment.
    Both robots should reach the bottom row in grid.
"""
class Solution:
    #USING RECURSION
    def recursion(self, i, j1, j2, rows, cols, grid):
        if j1 < 0 or j1 >= cols or j2 < 0 or j2 >= cols:
            return float("-inf")
        if i == rows - 1:
            if j1 == j2:
                return grid[i][j1]
            return grid[i][j1] + grid[i][j2]

        maxi = 0
        for new_j1 in [-1, 0, 1]:
            for new_j2 in [-1, 0, 1]:

                if j1 == j2:
                    ans = grid[i][j1] + self.recursion(
                        i + 1, j1 + new_j1, j2 + new_j2, rows, cols, grid
                    )
                else:

                    ans = ( grid[i][j1] + grid[i][j2] + self.recursion( i + 1, j1 + new_j1, j2 + new_j2, rows, cols, grid))
                maxi = max(maxi, ans)

        return maxi

    def cherryPickup(self, grid):

        rows = len(grid)
        cols = len(grid[0])
        return self.recursion(0, 0, cols - 1, rows, cols, grid)









    #USING MEMOIZATION
    def memoization(self, i, j1, j2, rows, cols, grid, dp):
        if j1 < 0 or j1 >= cols or j2 < 0 or j2 >= cols:
            return float("-inf")

        if i == rows - 1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]

        if dp[i][j1][j2] != None:
            return dp[i][j1][j2]

        maxi = 0
        for new_j1 in [-1, 0, 1]:
            for new_j2 in [-1, 0, 1]:

                if j1 == j2:
                    ans = grid[i][j1] + self.memoization( i + 1, j1 + new_j1, j2 + new_j2, rows, cols, grid, dp)
                else:
                    ans = ( grid[i][j1] + grid[i][j2] + self.memoization( i + 1, j1 + new_j1, j2 + new_j2, rows, cols, grid, dp))
                maxi = max(maxi, ans)

        dp[i][j1][j2] = maxi
        return dp[i][j1][j2]

    def cherryPickup_memo(self, grid):

        rows = len(grid)
        cols = len(grid[0])
        dp = [[[None for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]

        return self.memoization(0, 0, cols - 1, rows, cols, grid, dp)






    #USING TABULATION
    def cherryPickup_tabu(self, grid):

        rows = len(grid)
        cols = len(grid[0])
        dp = [[[None for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]

        for j1 in range(cols):
            for j2 in range(cols):
                if j1 == j2:
                    dp[rows - 1][j1][j2] = grid[rows - 1][j2]
                else:
                    dp[rows - 1][j1][j2] = grid[rows - 1][j1] + grid[rows - 1][j2]

        for i in range(rows - 2, -1, -1):
            for j1 in range(cols):
                for j2 in range(cols):

                    maxi = 0
                    for new_j1 in [-1, 0, 1]:
                        for new_j2 in [-1, 0, 1]:
                            
                            if j1+new_j1 < 0 or j1 + new_j1>= cols or j2 + new_j2 < 0 or j2 + new_j2 >= cols:
                                ans = float("-inf")

                            elif j1 == j2:
                                ans = grid[i][j1] + dp[i + 1][j1 + new_j1][j2 + new_j2]
                            else:
                                ans = grid[i][j1] + grid[i][j2] + dp[i + 1][j1 + new_j1][j2 + new_j2]

                            maxi = max(maxi, ans)

                    dp[i][j1][j2] = maxi            #type:ignore
        return dp[0][0][cols - 1]









    #USING TABULATION WITH SPACE OPTIMIZATION
    def cherryPickup_tabuSpaceOpt(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # dp for the last row
        front = [[0] * cols for _ in range(cols)]

        for j1 in range(cols):
            for j2 in range(cols):
                if j1 == j2:
                    front[j1][j2] = grid[rows - 1][j1]
                else:
                    front[j1][j2] = grid[rows - 1][j1] + grid[rows - 1][j2]

        # iterate from 2nd last row up to first row
        for i in range(rows - 2, -1, -1):
            curr = [[0] * cols for _ in range(cols)]
            for j1 in range(cols):
                for j2 in range(cols):
                    maxi = float("-inf")
                    for new_j1 in [-1, 0, 1]:
                        for new_j2 in [-1, 0, 1]:
                            nj1, nj2 = j1 + new_j1, j2 + new_j2
                            if 0 <= nj1 < cols and 0 <= nj2 < cols:
                                if j1 == j2:
                                    ans = grid[i][j1] + front[nj1][nj2]
                                else:
                                    ans = grid[i][j1] + grid[i][j2] + front[nj1][nj2]
                            else:
                                ans = float("-inf")
                            maxi = max(maxi, ans)
                    curr[j1][j2] = maxi            #type:ignore
            front = curr  # move up

        return front[0][cols - 1]

        

obj = Solution()
grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
print(obj.cherryPickup(grid))
print(obj.cherryPickup_memo(grid))
print(obj.cherryPickup_tabu(grid))
print(obj.cherryPickup_tabuSpaceOpt(grid))

# Output : 24