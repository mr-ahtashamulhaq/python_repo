"""Given a array arr of integers, return the sums of all subsets in the list.  Return the sums in any order."""
class Solution:
    def subsetSums(self, arr):
        res = [0]
        for i in range(0, len(arr)):
            l = len(res)
            for j in range(l):
                res.append(arr[i] + res[j])
        return res
    
obj = Solution()
arr = [1,2,1]
print(obj.subsetSums(arr))