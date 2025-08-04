"""Given an array, arr[] construct a product array, res[] where each element in res[i] is the product of all elements in arr[] except arr[i]. Return this resultant array, res[]."""
#User function Template for python3
class Solution:
    def productExceptSelf(self, arr):
        res = [i - (i-1) for i in arr]

        for i in range(len(arr)):
            print("i", i)
            res[i] = 1
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    continue
                else:
                    res[i] *= arr[j]
        return res

obj = Solution()
arr = [10, 3, 5, 6, 2]
print(obj.productExceptSelf(arr))
