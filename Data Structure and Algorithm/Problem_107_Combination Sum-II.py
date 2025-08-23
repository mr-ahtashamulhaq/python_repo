"""Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations."""
from typing import List
class Solution:
    def backtracking(self,ind, total , subset,candidates,result):
        if total == 0:
            result.append(subset.copy())
            return
        
        if total < 0:
            return
        
        if ind >= len(candidates):
            return
        
        # Try each candidate from current index onwards
        for i in range(ind,len(candidates)):
            #if current element is same as previous skip it
            if i>ind and candidates[i] == candidates[i-1]:
                continue

            #  if current candidate exceeds target, all remaining candidates will also exceed (array is sorted)
            if candidates[i] > total:
                break

            subset.append(candidates[i])
            remaining_total = total - candidates[i]

            # Include current candidate
            self.backtracking(i+1,remaining_total, subset,candidates,result )
            # Backtrack: remove the candidate
            subset.pop()

        
    def combinationSum2(self, candidates: List[int], target: int):
        result = []
        candidates.sort()
        self.backtracking(0,target,[],candidates,result)
        return result


obj = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(obj.combinationSum2(candidates, target))

# Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]