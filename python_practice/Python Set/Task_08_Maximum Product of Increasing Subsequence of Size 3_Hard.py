"""Given a sequence of non-negative integers, find the subsequence of length 3 having maximum product, with the elements of the subsequence being in increasing order."""
from itertools import combinations

def max_product_triplet(arr):
    max_product = -1
    result = ()

    for i, j, k in combinations(range(len(arr)), 3):
        a, b, c = arr[i], arr[j], arr[k]
        if a < b < c:
            product = a * b * c
            if product > max_product:
                max_product = product
                result = (a, b, c)

    if result:
        print("Triplet with max product:", result)
    else:
        print("No such triplet found.")