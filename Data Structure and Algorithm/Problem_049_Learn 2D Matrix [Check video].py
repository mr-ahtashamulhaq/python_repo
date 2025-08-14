"""Print Upper Triangle, Lower Triangle, and Sum of a Square Matrix

Print the upper triangular part of the matrix (including the main diagonal) while replacing all elements below the diagonal with "*" (asterisks).

Print the lower triangular part of the matrix (including the main diagonal) while replacing all elements above the diagonal with "*" (asterisks).

Compute and return the sum of all elements in the matrix."""

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(matrix)
col = len(matrix[0])
for i in range(rows):
    for j in range(col):
        if j>=i:
            print(matrix [i][j], end = " ")
        else:
            print("*",end = " ")
    print()

print()
for i in range(rows):
    for j in range(col):
        if j<=i:
            print(matrix [i][j], end = " ")
        else:
            print("*",end = " ")
    print()

print()
sum = 0
for i in range(rows):
    for j in range(col):
        sum += matrix[i][j]
print(f"Sum is {sum}")

#      Output : 
#       1 2 3 
#       * 5 6 
#       * * 9 

#       1 * * 
#       4 5 * 
#       7 8 9 

#       Sum is 45