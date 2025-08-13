"""Given an array arr[], Sort the array using the 'merge sort' algorithm."""
class Solution:
    # To merge arrays
    def merge_array(self, left, right):
        n = len(left)
        m = len(right)
        i, j = 0, 0
        result = []

        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        if i < n:
            while i < n:
                result.append(left[i])
                i += 1
        if j < m:
            while j < m:
                result.append(right[j])
                j += 1

        return result

    # To Divide and call merge
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_part = self.merge_sort(left_half)
        right_part = self.merge_sort(right_half)

        return self.merge_array(left_part, right_part)


obj = Solution()
arr = [3, 7, 1, 5, 3, 9, 6, 8]
sorted_arr = obj.merge_sort(arr)
print(sorted_arr)  
# Output :  [1, 3, 3, 5, 6, 7, 8, 9]