"""Given a binary matrix your task is to find all unique rows of the given matrix in the order of their appearance in the matrix."""
def uniqueRows(matrix):
    seen = set()
    result = []

    for row in matrix:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            result.append(row)

    return result

matrix = [
    [1, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

unique = uniqueRows(matrix)
for row in unique:
    print(*row)