"""Given an array nums[] of length n and a number k, the task is to find all the subsequences of the array with sum of its elements equal to k.

Note: A subsequence is a subset that can be derived from an array by removing zero or more elements, without changing the order of the remaining elements."""

class Solution:
    def subsets(self, nums, K):
        result = []

        def backtracking(ind, total , subset):
            if total == K:
                result.append(subset.copy())
                return
            
            elif total > K:
                return
            
            if ind >= len(nums):
                return

            subset.append(nums[ind])
            sum = total + nums[ind]
            backtracking(ind+1, sum , subset)

            e = subset.pop()
            sum -=e
            backtracking(ind+1, sum, subset)
        
        backtracking(0,0,[])
        return result
obj = Solution()
nums = [5,4,9]
K = 9
print(obj.subsets(nums, K))
# Output : [[5, 4], [9]]