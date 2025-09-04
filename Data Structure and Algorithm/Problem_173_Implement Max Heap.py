"""Design a data structure that implements a Max Heap supporting the following operations:

insert(val) → Insert an integer val into the heap.
extractMax() → Remove and return the maximum element from the heap. If the heap is empty, return None.
getMax() → Return the maximum element in the heap without removing it. If the heap is empty, return None.
changeKey(index, newVal) → Change the value at index index to newVal.
If newVal is larger than the current value, adjust the heap upwards.
If newVal is smaller, adjust the heap downwards.
heapSize() → Return the number of elements in the heap."""
class Solution:
    def __init__(self):
         self.arr = []
         self.count = 0
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

    def heapify_up(self, arr, ind):
        parent_ind = (ind-1) // 2

        if ind > 0  and arr[parent_ind] < arr[ind]:
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
            self.heapify_down(self.arr, index)
        else:
            self.arr[index] = new_val
            self.heapify_up(self.arr, index)

    def extractMax(self):
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
    
    def getMax(self):
        return self.arr[0] if self.count > 0 else None
    
    def heapSize(self):
        return self.count
    

heap = Solution()
heap.insert(10)
heap.insert(5)
heap.insert(20)
heap.insert(30)

print("Heap:", heap.arr)
print("Extract Max:", heap.extractMax())  
print("Heap after extract:", heap.arr)    
print("Max Element:", heap.getMax())      
print("Heap Size:", heap.heapSize())     

heap.changeKey(1, 50)
print("After changeKey(1, 50):", heap.arr) 

# Heap: [30, 20, 10, 5]
# Extract Max: 30
# Heap after extract: [20, 5, 10]
# Max Element: 20
# Heap Size: 3
# After changeKey(1, 50): [50, 20, 10]