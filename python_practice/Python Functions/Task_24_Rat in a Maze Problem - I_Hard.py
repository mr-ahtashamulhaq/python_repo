"""Consider a rat placed at position (0, 0) in an n x n square matrix mat[][]. The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).

The matrix contains only two possible values:

0: A blocked cell through which the rat cannot travel.
1: A free cell that the rat can pass through.
Your task is to find all possible paths the rat can take to reach the destination, starting from (0, 0) and ending at (n-1, n-1), under the condition that the rat cannot revisit any cell along the same path. Furthermore, the rat can only move to adjacent cells that are within the bounds of the matrix and not blocked.
If no path exists, return an empty list."""

class Solution:
    def findPath(self, mat, n):

        result = []

        visited = [[False]*n for _ in range(n)]

        def move(x, y, path):

            if x < 0 or y < 0 or x >= n or y >= n:
                return
            if mat[x][y] == 0 or visited[x][y]:
                return

            if x == n - 1 and y == n - 1:
                result.append(path)
                return

            visited[x][y] = True

            move(x + 1, y, path + 'D') 
            move(x, y - 1, path + 'L') 
            move(x, y + 1, path + 'R')
            move(x - 1, y, path + 'U')


            visited[x][y] = False

        if mat[0][0] == 1:
            move(0, 0, "")

        return result

mat = [
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
]
sol = Solution()
matsize = 3
print(sol.findPath(mat, matsize))
