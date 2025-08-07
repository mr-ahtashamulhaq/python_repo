"""Given an array A[] of length N. For each index, i (1<=i<=N), find the difference between the number of distinct elements in the left and right side in the of the current element in the array. """
def distinct_difference_array(A):
    N = len(A)
    result = []

    for i in range(N):
        left = A[:i]
        right = A[i+1:]

        left_distinct = len(set(left))
        right_distinct = len(set(right))

        result.append(left_distinct - right_distinct)

    return result

A = [4, 3, 4, 4, 2]
print(distinct_difference_array(A))  