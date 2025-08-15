"""Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order."""
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            if i >0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                k = j+1
                l = n-1

                while k<l:
                    total_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if total_sum < target:
                        k+=1
                    elif total_sum >target:
                        l -=1

                    else:
                        temp = [nums[i], nums[j] , nums[k], nums[l]]
                        result.append(temp)
                        k +=1
                        l -=1

                        while(k<l) and nums[k] == nums[k-1]:
                            k +=1
                        while k<l and nums[l] == nums[l+1]:
                            l -=1
        return result
obj = Solution()
nums = [-1,0,1,2,-1,-4]
target = 2
print(obj.fourSum(nums,target))
# output : [[-1, 0, 1, 2]]