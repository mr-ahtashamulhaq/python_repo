"""You are given a list that contains integers. You need to print the elements of the list with a space between them."""
def listTraversal(arr):
    for i in arr:
        print(i , end = " ")
arr = [12,45,78,43,23]
listTraversal(arr)