"""Design a data structure that implements a Min Heap supporting the following operations:

insert(val) → Insert an integer val into the heap.
extrtctMin() → Remove and return the minimum element from the heap. If the heap is empty, return None.
getMin() → Return the minimum element in the heap without removing it. If the heap is empty, return None.
changeKey(index, newVal) → Change the value at index index to newVal.
If newVal is smaller than the current value, adjust the heap upwards.
If newVal is larger, adjust the heap downwards.
heapSize() → Return the number of elements in the heap."""
class Solution:
    def __init__(self):
         self.arr = []
         self.count = 0

    def heapify_down(self, arr, ind):
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
            self.heapify_down(arr, smallest_ind)
    
    def heapify_up(self, arr, ind):
        parent_ind = (ind-1) // 2

        if ind > 0  and arr[parent_ind] > arr[ind]:
            arr[ind] , arr[parent_ind] = arr[parent_ind] , arr[ind]
            self.heapify_up(arr, parent_ind)

    def initializeheap(self):
         self.arr.clear()
         self.count = 0

    def insert(self , key):
        self.arr.append(key)
        self.heapify_up(self.arr , self.count)
        self.count +=1
    
    def changeKey(self, index, new_val):
        if new_val < self.arr[index] :
            self.arr[index] = new_val
            self.heapify_up(self.arr, index)
        else:
            self.arr[index] = new_val
            self.heapify_down(self.arr, index)

    def extractMin(self):
        if self.count == 0:
            return None

        element = self.arr[0]
        self.arr[0] , self.arr[self.count - 1] = self.arr[self.count - 1] ,self.arr[0]
        self.count -=1
        self.arr.pop()
        if self.count > 0:
            self.heapify_down(self.arr, 0)
        return element

    def isEmpty(self):
        return True if self.count ==0  else False
    
    def getMin(self):
        return self.arr[0] if self.count > 0 else None
    
    def heapSize(self):
        return self.count
    

heap = Solution()
heap.insert(10)
heap.insert(5)
heap.insert(20)
heap.insert(3)

print("Heap:", heap.arr)
print("Extract Min:", heap.extractMin())
print("Heap after extract:", heap.arr)
print("Min Element:", heap.getMin())
print("Heap Size:", heap.heapSize())
print("Is Empty:", heap.isEmpty())       

heap.changeKey(1, 2)
print("After changeKey(1, 2):", heap.arr) 

# Heap: [3, 5, 20, 10]
# Extract Min: 3
# Heap after extract: [5, 10, 20]
# Min Element: 5
# Heap Size: 3
# Is Empty: False
# After changeKey(1, 2): [2, 5, 20]