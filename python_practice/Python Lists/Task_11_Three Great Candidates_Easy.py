"""The hiring team aims to find 3 candidates who are great collectively. Each candidate has his or her ability expressed as an integer. 3 candidates are great collectively if the product of their abilities is maximum. Given the abilities of some candidates in an array, arr[], return the maximum collective ability from the pool of candidates."""

#User function Template for python3

class Solution:
    def maxProduct(self, arr):
        product = 1
        arr.sort()
        for i in arr[:-4:-1]:
            product *= i
        return product

obj = Solution()
arr = [5,7,3,8,3,10,20,30]
print(obj.maxProduct(arr))