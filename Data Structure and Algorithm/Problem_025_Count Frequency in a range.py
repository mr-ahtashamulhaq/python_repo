"""You are given an array arr[] containing positive integers. The elements in the array arr[] range from  1 to n (where n is the size of the array), and some numbers may be repeated or absent. Your have to count the frequency of all numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing)."""
class Solution:
    def frequencyCount(self, arr):
        #  code here
        n = len(arr)
        freq = [0]* n
        for i in arr:
            freq[i-1] +=1
        return freq
            

obj = Solution()
arr = [1,2,2,3,4,5]
print(obj.frequencyCount(arr))
# Output  : [1, 2, 1, 1, 1, 0]