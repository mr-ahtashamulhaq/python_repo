"""You are given a list numbers that contains integers. You need to return two lists, one of even numbers and other of odd numbers."""
#User function Template for python3
def evenOdd(arr):
    even = []
    odd = []

    for i in arr:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return (even, odd)
arr = [2,3,4,5,6,7,8,9]
print(evenOdd(arr))