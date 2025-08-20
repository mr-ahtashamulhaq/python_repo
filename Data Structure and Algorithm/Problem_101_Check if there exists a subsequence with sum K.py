"""Given an array arr and target sum k, check whether there exists a subsequence such that the sum of all elements in the subsequence equals the given target sum(k)."""
class Solution:
    def subsets(self, nums, K):

        def backtracking(ind, total):
            if total == K:
                return True
            
            elif total > K:
                return False
            
            if ind >= len(nums):
                return False

            sum = total + nums[ind]
            pick = backtracking(ind+1, sum)
            if pick == True:
                return True

            sum = total
            notpick = backtracking(ind+1, sum)
            return notpick
        
        
        return backtracking(0,0)
obj = Solution()
nums = [5,4,9]
K = 9
print(obj.subsets(nums, K))
# Output : True