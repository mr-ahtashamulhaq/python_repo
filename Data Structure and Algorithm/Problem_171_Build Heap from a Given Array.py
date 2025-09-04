"""Given an integer array `arr`, convert it into a **Max-Heap** in-place.

A Max-Heap is a complete binary tree where:
- Each parent node is greater than or equal to its children.
- The array representation of the tree must satisfy the max-heap property.

You need to implement:
1. `heapify_down(arr, ind)` → ensures the subtree rooted at index `ind` satisfies the max-heap property.
2. `build_heap(arr)` → converts the entire array into a max-heap by repeatedly calling `heapify_down`."""
class Solution:
    def heapify_down_max(self, arr, ind):
        n = len(arr)

        largest_ind = ind

        left_child_ind = 2 * ind +1
        right_child_ind = 2 * ind +2

        if left_child_ind < n and arr[left_child_ind] > arr[largest_ind]:
            largest_ind = left_child_ind
        if right_child_ind < n and arr[right_child_ind]  > arr[largest_ind]:
            largest_ind = right_child_ind

        if ind != largest_ind:
            arr[ind] , arr[largest_ind] = arr[largest_ind] , arr[ind]
            self.heapify_down_max(arr, largest_ind)

    def build_max_heap(self,arr):
        n = len(arr)

        for i in range((n//2) -1 , -1 ,-1):
            self.heapify_down_max(arr , i)


    def heapify_down_min(self, arr, ind):
        n = len(arr)

        smallest_ind = ind

        left_child_ind = 2 * ind +1
        right_child_ind = 2 * ind +2
        if left_child_ind < n and arr[left_child_ind] < arr[smallest_ind] :
            smallest_ind = left_child_ind

        if right_child_ind < n and arr[right_child_ind] < arr[smallest_ind] :
                smallest_ind = right_child_ind
        if ind != smallest_ind:
            arr[ind] , arr[smallest_ind] = arr[smallest_ind] , arr[ind]
            self.heapify_down_min (arr, smallest_ind)


    def buil_min_heap(self, arr):
        n  = len(arr)
        for i in range((n//2) - 1 , -1 , -1):
            self.heapify_down_min(arr, i)

        

obj = Solution()
arr = [4, 2, 8, 16, 3, 6, 5,]
obj.build_max_heap(arr)
print(arr)
obj.buil_min_heap(arr)
print(arr)
# [16, 4, 8, 2, 2, 6, 5]
# [2, 2, 5, 4, 16, 6, 8]