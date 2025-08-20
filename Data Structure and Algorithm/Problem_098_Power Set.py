from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        totalsubsets = 2**n
        result = []

        for num in range(totalsubsets):
            templist = []
            for j in range(n):
                temp =True if num & (1<<j ) !=0 else False
                if temp:
                    templist.append(nums[j])
            result.append(templist)
        return result
obj= Solution()
arr = [1,2,3]
print(obj.subsets(arr))
# output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]