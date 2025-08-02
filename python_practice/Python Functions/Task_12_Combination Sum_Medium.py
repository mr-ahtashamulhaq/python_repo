"""Given an array arr[] and a target, your task is to find all unique combinations in the array where the sum is equal to target. The same number may be chosen from the array any number of times to make target.

You can return your answer in any order."""
class Solution:
    def combinationSum(self,arr, target):
        result = []

        def backtrack(start, path, total):

            if total == target:
                result.append(path.copy())
                return
            if total > target:
                return
        
            for i in range(start, len(arr)):

                path.append(arr[i])
                backtrack(i, path, total + arr[i]) 
                path.pop()
                
        backtrack(0, [], 0)
        return result


obj = Solution()
arr = [2,4,6,8]
print(obj.combinationSum(arr,8))

