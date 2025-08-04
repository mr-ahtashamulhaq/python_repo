"""Given a 2d integer array arr[][] of size k*n, where each row is sorted in ascending order. Your task is to find the smallest range [l, r] that includes at least one element from each of the k lists. If more than one such ranges are found, return the first one."""
class Solution:
    def findSmallestRange(self, arr):

        n = len(arr)
        max_sum = -99999

        for r in range(n):
            rotated = arr[-r:] + arr[:-r]

            current_sum = 0
            for i in range(n):
                current_sum += i * rotated[i]
            
            if current_sum > max_sum:
                max_sum = current_sum
            
        return max_sum

obj = Solution()
arr= [1,2,3]
print(obj.findSmallestRange(arr))