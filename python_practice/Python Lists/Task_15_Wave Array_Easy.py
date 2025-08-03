"""Given an sorted array arr[] of integers. Sort the array into a wave-like array(In Place). In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5] ..... and so on. If there are multiple solutions, find the lexicographically smallest one."""
class Solution:
    def sortInWave(self, arr):
        stind = 0
        endind = 1
        for i in range(len(arr)//2):
            arr[stind], arr[endind] = arr[endind],arr[stind]
            stind +=2
            endind +=2

        return arr
    
obj = Solution()
arr = [2,4,7,8,9,10]
print(obj.sortInWave(arr))