"""Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular."""
#User function Template for python3

class Solution:
    def rotateArr(self, arr, d):

        for i in range(d):
            arr.append(arr.pop(0))
        return arr

obj = Solution()
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
k = 3
print(obj.rotateArr(arr,k))
