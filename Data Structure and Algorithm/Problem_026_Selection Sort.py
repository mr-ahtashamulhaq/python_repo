"""Given an array arr, use selection sort to sort arr[] in both increasing order and Decreasing order."""
class Solution: 
    def selectionSort(self, arr):
        #Accending Order
        for i in range(len(arr)):
            min_ind = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[min_ind]:
                    min_ind = j
            arr[min_ind],arr[i] = arr[i],arr[min_ind]
            print(arr)


        # Decending Order - Uncomment this and comment Accending part to Run this code
        
        # for i in range(len(arr)):
        #     min_ind = i
        #     for j in range(i+1,len(arr)):
        #         if arr[j] > arr[min_ind]:
        #             min_ind = j
        #     arr[min_ind],arr[i] = arr[i],arr[min_ind]


        return arr
obj  = Solution()
arr = [4,3,1,2]
print(obj.selectionSort(arr))
# Output Accending: [1, 3, 3, 3, 4, 5, 23]
# Output Decending: [23, 5, 4, 3, 3, 3, 1]