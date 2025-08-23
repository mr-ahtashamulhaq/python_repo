"""Find all valid combinations of 'k' numbers that sum up to 'n' such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order."""
from typing import List
class Solution:

    def solve(self,subset,total,last,n,k,result):

        if total == n and len(subset) == k:
            result.append(subset.copy())
            return
        
        if total > n or len(subset) > k:
            return

        # Try numbers from last to 9 (ascending order, no duplicates)
        for i in range(last, 10):
            subset.append(i)
            self.solve(subset,total + i ,i + 1,n,k,result) # Update sum and next start
            subset.pop() 

    def combinationSum3(self, k, n):
        result = []
        self.solve([], 0, 1, n, k, result)  # Start with sum=0, last=1
        return result
    

obj = Solution()
print(obj.combinationSum3(3,9))
# Output:[[1, 2, 6], [1, 3, 5], [2, 3, 4]]