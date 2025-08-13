"""Given an array arr[] of positive integers.The task is to complete the insertsort() function which is used to implement Insertion Sort."""
class Solution:
    def insertionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(1,n):
            current  = arr[i]
            tocheck  = i-1
            while( (arr[tocheck] > current) and tocheck>=0 ):
                    arr[tocheck + 1] = arr[tocheck]
                    tocheck -=1
            arr[tocheck + 1] =current
        return arr
obj = Solution()
arr = [1,4,2,7,3,9,5]
print(obj.insertionSort(arr))
# Output : [1, 2, 3, 4, 5, 7, 9]