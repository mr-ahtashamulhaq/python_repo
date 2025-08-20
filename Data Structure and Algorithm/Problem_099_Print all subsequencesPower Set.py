"""Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order."""

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def solve(ind,subset):
            if ind >= len(nums):
                return result.append(subset.copy())
            #Pick nums[ind] and call
            subset.append(nums[ind])
            solve(ind+1,subset)

            #Not pick nums[ind] and call
            subset.pop()
            solve(ind+1 , subset)

        solve(0,[])
        return result

obj = Solution()
arr = [1,2,3]
print(obj.subsets(arr))
# Output :[[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]