"""Given an array of positive integers. Find the maximum length of Bitonic subsequence. 
A subsequence of array is called Bitonic if it is first strictly increasing, then strictly decreasing. Return the maximum length of bitonic subsequence."""
class Solution:
    def longestbitonicsequence(self, arr):
        total = 1
        n = len(arr)

        index = 0
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                total += 1
            else:
                index = i
                break
        else:
            return total

        for j in range(index, n - 1):
            if arr[j] > arr[j + 1]:
                total += 1
            else:
                break

        return total

obj = Solution()
arr = [1, 2, 5, 3, 2]
print(obj.longestbitonicsequence(arr))
