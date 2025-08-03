"""You are given a list that contains integers. You need to return the sum of the list."""

def listSum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
arr = [12,5,7,8,9,5,3]
print(listSum(arr))