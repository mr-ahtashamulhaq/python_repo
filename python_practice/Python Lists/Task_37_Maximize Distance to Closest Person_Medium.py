"""Given an array arr[], the task is to find the maximum distance between two occurrences of an element. If no element has two occurrences, then return 0."""
class Solution:
    def maxDistance(self, arr):
        max_dist = 0
        for i in range(len(arr)):
            for j in range(len(arr) - 1, i, -1):
                if arr[i] == arr[j]:
                    dist = j - i
                    if dist > max_dist:
                        max_dist = dist
                    break 
        return max_dist

obj = Solution()
arr = [1, 2, 3, 2, 1, 4, 2]
print(obj.maxDistance(arr))