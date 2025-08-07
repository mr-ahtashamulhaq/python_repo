"""You are given an array arr[] containing positive integers. The elements in the array arr[] range from  1 to n (where n is the size of the array), and some numbers may be repeated or absent.
 Your have to count the frequency of all numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing)."""
class Solution:
    def frequencyCount(self, arr):
        result = []
        for i in range(len(arr)):
            occurance  = arr.count(i+1)
            result.append(occurance)
        return result

obj  = Solution()
arr = [2, 3, 2, 3, 5]
print(obj.frequencyCount(arr))