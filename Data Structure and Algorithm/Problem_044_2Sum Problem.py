"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            remaining  = target - nums[i]
            if remaining in dic:
                return [dic[remaining],i]
            dic[nums[i]] = i

obj = Solution()
nums = [2,11,7,15]
target = 9
print(obj.twoSum(nums,target))
# output : [0, 2]