"""Given an array arr of non-negative integers and an integer target, the task is to count all subsets of the array whose sum is equal to the given target."""
class Solution:
    def subsets(self, nums, K):

        def backtracking(ind, total):
            if total == K:
                return 1
            
            elif total > K:
                return 0
            
            if ind >= len(nums):
                return 0

            sum = total + nums[ind]
            pick = backtracking(ind+1, sum)

            sum = total

            notpick = backtracking(ind+1, sum)
            return pick + notpick
        
        
        return backtracking(0,0)
obj = Solution()
nums = [5,4,9,3,6,7,2]
K = 9
print(obj.subsets(nums, K))
# Output : 5