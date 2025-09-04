"""Given a binary heap implementation of Priority Queue. Extract the maximum element from the queue i.e. remove it from the Queue and return it's value. """
class Solution:
    def heapify_down(self, arr, ind):
        n = len(arr)

        largest_ind = ind

        left_child_ind = 2 * ind +1
        right_child_ind = 2 * ind +2
        if left_child_ind < n and arr[left_child_ind] > arr[largest_ind] :
            largest_ind = left_child_ind

        if right_child_ind < n and arr[right_child_ind] > arr[largest_ind] :
                largest_ind = right_child_ind
        if ind != largest_ind:
            arr[ind] , arr[largest_ind] = arr[largest_ind] , arr[ind]
            self.heapify_down(arr, largest_ind)
    def extractMax(self, arr):
        n = len(arr)
        element = arr[0]
        arr[0] , arr[n - 1] = arr[n - 1] ,arr[0]
        arr.pop()
        self.heapify_down(arr , 0)
        return element
    
    def build_max_heap(self,arr):
        n = len(arr)

        for i in range((n//2) -1 , -1 ,-1):
            self.heapify_down(arr , i)
        return self.extractMax(arr)
obj = Solution()
arr = [4, 2, 8, 16, 24, 2, 6, 5]
print(obj.build_max_heap(arr))
print(arr)

# 24
# Output after pop : [16, 5, 8, 4, 2, 2, 6]