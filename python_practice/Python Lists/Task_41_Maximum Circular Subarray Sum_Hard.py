"""You are given a circular array arr[] of integers, find the maximum possible sum of a non-empty subarray. In a circular array, the subarray can start at the end and wrap around to the beginning. Return the maximum non-empty subarray sum, considering both non-wrapping and wrapping cases."""
class Solution:
    def maxSubarraySumCircular(self, arr):
        total  = sum(arr)

        max_sum = cur_max = arr[0]
        for x in arr[1::]:
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum , cur_max)
        
        min_sum = cur_min = arr[0]
        for x in arr[1::]:
            cur_min = min(x ,cur_min + x)
            min_sum  = min (cur_min , min_sum)\
            
        if max_sum < 0:
            return max_sum
        return max(max_sum , total - min_sum)
    
obj = Solution()
arr = [8, -8, 9, -9, 10, -11, 12]
print(obj.maxSubarraySumCircular(arr))
