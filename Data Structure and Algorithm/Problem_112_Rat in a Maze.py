"""Consider a rat placed at position (0, 0) in an n x n square matrix mat[][]. The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).

The matrix contains only two possible values:

0: A blocked cell through which the rat cannot travel.
1: A free cell that the rat can pass through.
Your task is to find all possible paths the rat can take to reach the destination, starting from (0, 0) and ending at (n-1, n-1), under the condition that the rat cannot revisit any cell along the same path. Furthermore, the rat can only move to adjacent cells that are within the bounds of the matrix and not blocked.
If no path exists, return an empty list.

Note: Return the final result vector in lexicographically smallest order."""
class Solution:
    def ratInMaze(self, mat):
        # code here

        result = []
        n = len(mat)
        visited = [[False]*n for _ in range(n)]

        if mat[0][0] == 1:
            self.move(0, 0, "",n,visited,result)

        return result
    
    #Helper Function
    def move(self,x, y, path,n,visited,result):

        if x < 0 or y < 0 or x >= n or y >= n:
            return
        
        if mat[x][y] == 0 or visited[x][y]:
            return

        if x == n - 1 and y == n - 1:
            result.append(path)
            return

        visited[x][y] = True

        self.move(x + 1, y, path + 'D',n,visited,result) 
        self.move(x, y - 1, path + 'L',n,visited,result) 
        self.move(x, y + 1, path + 'R',n,visited,result)
        self.move(x - 1, y, path + 'U',n,visited,result)


        visited[x][y] = False


obj = Solution()
mat = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
print(obj.ratInMaze(mat))
# Output : ['DDRDRR', 'DRDDRR']