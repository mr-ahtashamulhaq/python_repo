"""Given an unsorted array A of size N and value K. The elements of the array A contain positive integers. You have to print all the elements that are greater than K in the array(including K as well if present in the array A) and print all the elements that are smaller than K in separate lines. 
If the elements greater than K does not present in the array then print "-1". 
Similarly, in case of smaller elements print -1 if elements smaller than k doesn't exist. 

Note that you need to sort the array, if there are duplicates print only first element."""
def print_elements_by_k(A, K):
    A.sort()
    
    seen = set()
    greater_or_equal = []
    smaller = []

    for num in A:
        if num not in seen:
            seen.add(num)
            if num >= K:
                greater_or_equal.append(num)
            elif num < K:
                smaller.append(num)

    if greater_or_equal:
        print(' '.join(map(str, greater_or_equal)))
    else:
        print(-1)

    if smaller:
        print(' '.join(map(str, smaller)))
    else:
        print(-1)

A = [4, 2, 5, 7, 4, 2, 9]
K = 4
print_elements_by_k(A, K)