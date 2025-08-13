# Find the second largst element from given array without using sorting
class Solution:
    def second_largest(self,arr):
        largest = float("-inf")
        secondlargest = float("-inf")

        for i in range(len(arr)):
            if arr[i]>largest :
                secondlargest = largest
                largest = arr[i]
                
            elif arr[i]>secondlargest and arr[i] != largest:
                secondlargest = arr[i]
        return secondlargest

obj = Solution()
arr = [1,6,23,2,5,63,1,86,24,105,106]
print(obj.second_largest(arr))

# output : 105