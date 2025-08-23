"""Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input."""
from typing import List
class Solution:
        #Helper function
        def backtracking(self,ind, total , subset,candidates,target,result):
            if total == target:
                result.append(subset.copy())
                return
            
            elif total > target:
                return
            
            if ind >= len(candidates):
                return

            subset.append(candidates[ind])
            sum = total + candidates[ind]
            self.backtracking(ind, sum , subset,candidates,target,result)
            
            subset.pop()
            sum = total
            self.backtracking(ind+1, sum , subset,candidates,target,result)

        #main function
        def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

            
            result = []
            self.backtracking(0,0,[],candidates,target,result)
            return result

obj = Solution()
nums = [2,5,6]
K = 10
print(obj.combinationSum(nums, K))
# Output : [[2, 2, 2, 2, 2], [2, 2, 6], [5, 5]]