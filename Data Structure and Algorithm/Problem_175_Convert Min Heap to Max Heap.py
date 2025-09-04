"""You are given an integer array arr representing a Min Heap (i.e., every parent node is smaller than its children).
Your task is to convert this Min Heap into a Max Heap (i.e., every parent node is larger than its children) and return the resulting array.

You must do this in-place and in O(n) time."""
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

obj  = Solution()
arr= [2, 2, 5, 4, 16, 6, 8]
obj.build_max_heap(arr)
print(arr)

#Output : [16, 4, 8, 2, 2, 6, 5]