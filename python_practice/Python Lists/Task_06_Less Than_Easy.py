"""You are given a number k and a list arr[] that contains integers. You need to return list of numbers that are less than k."""
def lessThan(arr, k):
    ans = []
    for i in arr:
        if i<k :
            ans.append(i)

    return ans
arr = [78,34,2,1,67]
k = 6
print(lessThan(arr,k))