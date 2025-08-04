"""Given a binary array consisting of only 0s and 1s, your task is to find the minimum number of swaps required to group all 1s. If there are no 1s in the array, return -1."""
class Solution:
    def minSwaps(self, arr):
        ones = sum(arr)
        if ones == 0:
            return -1 
        
        curr = sum(arr[:ones])
        max_ones = curr

        for i in range(ones, len(arr)):
            curr = curr + arr[i] - arr[i - ones]
            max_ones = max(max_ones, curr)
        
        return ones - max_ones  

obj = Solution()
arr = [1,0,1,0,1,0]
print(obj.minSwaps(arr))