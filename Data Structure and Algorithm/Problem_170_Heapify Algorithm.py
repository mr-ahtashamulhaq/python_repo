"""
You are given an array `arr` representing a **binary heap** (either max-heap or min-heap). 
Your task is to implement the `heapify` operation for both **max-heap** and **min-heap**.

The heapify operation is used when a single element in the heap is modified, 
and we need to restore the heap property.

For max-heap:
- Each parent node must be greater than or equal to its children.

For min-heap:
- Each parent node must be less than or equal to its children.
"""
class max_heap:
    def heapify_down(self, arr, ind):

        n = len(arr)
        largest_ind  = ind

        left_child_ind = (2*ind) +1
        right_child_ind = (2*ind) +2

        if left_child_ind < n and arr[left_child_ind] > arr[largest_ind]:
            largest_ind = left_child_ind

        if right_child_ind < n and arr[right_child_ind] > arr[largest_ind]:
            largest_ind = right_child_ind

        if ind != largest_ind:
            arr[largest_ind] , arr[ind] = arr[ind] , arr[largest_ind]
            self.heapify_down(arr , largest_ind)

    def heapify_up(self, arr, ind):
            
            parent_ind=  (ind -1 ) //2

            if ind > 0 and arr[parent_ind] < arr[ind]:
                arr[parent_ind] , arr[ind] = arr[ind] , arr[parent_ind]
                self.heapify_up(arr, parent_ind)


    def max_heapify(self , arr , index, val):
        if val < arr[index]:
            arr[index] = val
            self.heapify_down(arr, index)
        else:
            arr[index] = val
            self.heapify_up(arr, index)

class min_heap:
    def heapify_up(self, arr, ind):
        parent_ind = (ind-1) // 2

        if ind > 0  and arr[parent_ind] > arr[ind]:
            arr[ind] , arr[parent_ind] = arr[parent_ind] , arr[ind]
            self.heapify_up(arr, parent_ind)

    
    def heapify_down( self, arr, ind):
        n = len(arr)

        smallest_ind = ind
        left_child = 2 * ind +1
        right_child = 2 * ind +2

        if left_child < n and arr[left_child] < arr[smallest_ind]:
            smallest_ind = left_child
        if right_child < n and arr[right_child] < arr[smallest_ind]:
            smallest_ind = right_child
        
        if ind != smallest_ind:
            arr[ind] , arr[smallest_ind] = arr[smallest_ind] , arr[ind]
            self.heapify_down(arr, smallest_ind)

    def min_heapify(self, arr, index, val):
        if val < arr[index] :
            arr[index] = val
            self.heapify_up(arr, index)
        else:
            arr[index] = val
            self.heapify_down(arr, index)


max_h = max_heap()
min_h = min_heap()


# Test max_heapify
arr = [50, 30, 40, 10, 20, 15, 35]
print(f"Before max_heapify(index=2, val=60): {arr}")
max_h.max_heapify(arr, 2, 60)
print(f"After max_heapify: {arr}\n\n")

#Test min_heapify
print(f"Before min_heapify(index=2, val=3): {arr}")
min_h.min_heapify(arr, 2, 3)
print(f"After min_heapify: {arr}")

# Before max_heapify(index=2, val=60): [50, 30, 40, 10, 20, 15, 35]
# After max_heapify: [60, 30, 50, 10, 20, 15, 35]


# Before min_heapify(index=2, val=3): [60, 30, 50, 10, 20, 15, 35]
# After min_heapify: [3, 30, 60, 10, 20, 15, 35]
