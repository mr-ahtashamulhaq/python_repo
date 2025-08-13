"""Given an array, arr[]. Sort the array using bubble sort algorithm."""
class Solution:
    def bubbleSort(self,arr):
        # code here
        n  = len(arr)
        for i in range(n-1,-1,-1):

            is_swap = False
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1] , arr[j]
                    is_swap = True
                    
            if is_swap == False:
                return

    
obj  = Solution()
arr = [3,7,1,5,3,9,6,8]
obj.bubbleSort(arr)
print(arr)
# Output : [1, 3, 3, 5, 6, 7, 8, 9]