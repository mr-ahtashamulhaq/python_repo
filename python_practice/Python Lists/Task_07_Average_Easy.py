"""You are given a list arr that contains integers. You need to return average of the non negative integers."""
#User function Template for python3

def nonNegativeAverage(arr):
    sum = 0
    totalpos = 0
    for i in arr:
        if i>0:
            totalpos += 1
            sum +=i
    avg = sum /totalpos
    return avg
arr = [2,7,4,-1,6,-6,5]
print(nonNegativeAverage(arr))