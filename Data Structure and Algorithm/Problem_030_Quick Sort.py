"""Implement Quick Sort, a Divide and Conquer algorithm, to sort an array, arr[] in ascending order.
Given an array arr[], with starting index low and ending index high, complete the functions partition() and quickSort().
Use the last element as the pivot, so that all elements less than or equal to the pivot come before it, and elements greater than the pivot follow it.

Note: low and high are inclusive."""
class Solution:
    def quickSort(self, arr, low, high):
        # code here 
        if low < high:
            p_ind = self.partition(arr, low, high)
            self.quickSort(arr, low, p_ind - 1)
            self.quickSort(arr, p_ind + 1, high)

    def partition(self, arr, low, high):
        # code here
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j


obj = Solution()
arr = [3, 7, 1, 5, 3, 9, 6, 8]
obj.quickSort(arr, 0, len(arr) - 1)
print(arr) 
# Output:  [1, 3, 3, 5, 6, 7, 8, 9]