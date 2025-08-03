"""You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list."""
def decrementList(arr):
    for j,i in enumerate(arr):
        arr[j] = i-1
    return arr
arr = [16,45,8,34,9]
print(decrementList(arr))